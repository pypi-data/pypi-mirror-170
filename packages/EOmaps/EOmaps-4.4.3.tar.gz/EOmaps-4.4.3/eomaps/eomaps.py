"""A collection of helper-functions to generate map-plots."""

from functools import lru_cache, wraps, partial
from itertools import repeat
from collections import defaultdict
import warnings
import copy
from types import SimpleNamespace
from pathlib import Path
import weakref
from tempfile import TemporaryDirectory, TemporaryFile
import gc
import json

import numpy as np


pd = None


def _register_pandas():
    global pd
    try:
        import pandas as pd
    except ImportError:
        return False

    return True


gpd = None


def _register_geopandas():
    global gpd
    try:
        import geopandas as gpd
    except ImportError:
        return False

    return True


# ------- perform lazy delayed imports
# (for optional dependencies that take long time to import)
xar = None


def _register_xarray():
    global xar
    try:
        import xarray as xar
    except ImportError:
        return False

    return True


ds, mpl_ext = None, None


def _register_datashader():
    global ds
    global mpl_ext

    try:
        import datashader as ds
        from datashader import mpl_ext
    except ImportError:
        return False

    return True


mapclassify = None


def _register_mapclassify():
    global mapclassify
    try:
        import mapclassify
    except ImportError:
        return False

    return True


from scipy.spatial import cKDTree
from pyproj import CRS, Transformer

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.gridspec import GridSpec, GridSpecFromSubplotSpec, SubplotSpec

import matplotlib.path as mpath
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection


from cartopy import crs as ccrs

from .helpers import (
    pairwise,
    cmap_alpha,
    BlitManager,
    LayoutEditor,
    progressbar,
    searchtree,
)
from ._shapes import shapes

from ._containers import (
    data_specs,
    map_objects,
    classify_specs,
    # cb_container,
    wms_container,
    NaturalEarth_features,
)

from ._cb_container import cb_container
from .scalebar import ScaleBar, Compass
from .projections import Equi7Grid_projection
from .reader import read_file, from_file, new_layer_from_file

from .utilities import utilities


if plt.isinteractive():
    if plt.get_backend() == "module://ipympl.backend_nbagg":
        warnings.warn(
            "EOmaps disables matplotlib's interactive mode (e.g. 'plt.ioff()') "
            + "when using the 'ipympl' backend to avoid recursions during callbacks!"
            + "call `plt.show()` or `m.show()` to show the map!"
        )
        plt.ioff()
    else:
        plt.ion()


class Maps(object):
    """
    The base-class for generating plots with EOmaps.

    See Also
    --------
    MapsGrid : Initialize a grid of Maps objects

    Maps.new_layer : get a Maps-object that represents a new layer of a map

    Parameters
    ----------
    crs : int or a cartopy-projection, optional
        The projection of the map.
        If int, it is identified as an epsg-code
        Otherwise you can specify any projection supported by `cartopy.crs`
        A list for easy-accses is available as `Maps.CRS`

        The default is 4326.
    layer : int or str, optional
        The name of the plot-layer assigned to this Maps-object.
        The default is 0.

    Other Parameters:
    -----------------
    parent : eomaps.Maps
        The parent Maps-object to use.
        Any maps-objects that share the same figure must be connected
        to allow shared interactivity!

        By default, also the axis used for plotting is shared between connected
        Maps-objects, but this can be overridden if you explicitly specify
        either a GridSpec or an Axis via `gs_ax`.

        >>> m1 = Maps()
        >>> m2 = Maps(parent=m1)

        Note: Instead of specifying explicit axes, you might want to have a
        look at `eomaps.MapsGrid` objects!
    f : matplotlib.Figure, optional
        Explicitly specify the matplotlib figure instance to use.
        (ONLY useful if you want to add a map to an already existing figure!)

          - If None, a new figure will be created (accessible via m.figure.f)
          - Connected maps-objects will always share the same figure! You do
            NOT need to specify it (just provide the parent and you're fine)!

        The default is None
    gs_ax : matplotlib.axes or matplotlib.gridspec.SubplotSpec, optional
        Explicitly specify the axes (or GridSpec) for plotting.

        Possible values are:

        * None:
            Initialize a new axes (the default)
        * `matplotilb.gridspec.SubplotSpec`:
            Use the SubplotSpec for initializing the axes.
            The SubplotSpec will be divided accordingly in case a colorbar
            is plotted.

                >>> import matplotlib.pyplot as plt
                >>> from matplotlib.gridspec import GridSpec
                >>> f = plt.figure()
                >>> gs = GridSpec(2,2)
                >>> m = Maps()
                >>> ...
                >>> m.plot_map(f_gs=gs[0,0])
        * `matplotilb.Axes`:
            Directly use the provided figure and axes instances for plotting.
            The axes MUST be a geo-axes with `m.crs_plot` projection.

                >>> import matplotlib.pyplot as plt
                >>> f = plt.figure()
                >>> m = Maps()
                >>> ...
                >>> ax = f.add_subplot(projection=m.crs_plot)
                >>> m.plot_map(ax_gs=ax)
    preferred_wms_service : str, optional
        Set the preferred way for accessing WebMap services if both WMS and WMTS
        capabilities are possible.
        The default is "wms"

    kwargs :
        additional kwargs are passed to matplotlib.pyplot.figure()
        - e.g. figsize=(10,5)
    """

    CRS = ccrs
    CRS.Equi7Grid_projection = Equi7Grid_projection

    # mapclassify.CLASSIFIERS
    _classifiers = (
        "BoxPlot",
        "EqualInterval",
        "FisherJenks",
        "FisherJenksSampled",
        "HeadTailBreaks",
        "JenksCaspall",
        "JenksCaspallForced",
        "JenksCaspallSampled",
        "MaxP",
        "MaximumBreaks",
        "NaturalBreaks",
        "Quantiles",
        "Percentiles",
        "StdMean",
        "UserDefined",
    )

    CLASSIFIERS = SimpleNamespace(**dict(zip(_classifiers, _classifiers)))

    def __init__(
        self,
        crs=None,
        parent=None,
        layer=0,
        f=None,
        gs_ax=None,
        preferred_wms_service="wms",
        **kwargs,
    ):
        # share the axes with the parent if no explicit axes is provided
        if parent is not None:
            assert (
                f is None
            ), "You cannot specify the figure for connected Maps-objects!"

        self._f = f
        self._ax = gs_ax
        self._parent = None

        self._BM = None
        self._children = set()  # weakref.WeakSet()
        self._layer = layer

        self.parent = parent  # invoke the setter!

        # preferred way of accessing WMS services (used in the WMS container)
        assert preferred_wms_service in [
            "wms",
            "wmts",
        ], "preferred_wms_service must be either 'wms' or 'wmts' !"
        self._preferred_wms_service = preferred_wms_service

        if isinstance(gs_ax, plt.Axes):
            # set the plot_crs only if no explicit axes is provided
            if crs is not None:
                raise AssertionError(
                    "You cannot set the crs if you already provide an explicit axes!"
                )
            if gs_ax.projection == Maps.CRS.PlateCarree():
                self._crs_plot = 4326
            else:
                self._crs_plot = gs_ax.projection
        else:
            if crs is None or crs == Maps.CRS.PlateCarree():
                crs = 4326

            self._crs_plot = crs

        self._crs_plot_cartopy = self._get_cartopy_crs(self._crs_plot)

        # default classify specs
        self.classify_specs = classify_specs(weakref.proxy(self))

        self.data_specs = data_specs(
            weakref.proxy(self),
            x="lon",
            y="lat",
            crs=4326,
        )

        self._layout_editor = None

        self._figure = map_objects(weakref.proxy(self))
        self._cb = cb_container(weakref.proxy(self))  # accessor for the callbacks

        self._init_figure(gs_ax=gs_ax, plot_crs=crs, **kwargs)
        self._utilities = utilities(weakref.proxy(self))
        self._wms_container = wms_container(weakref.proxy(self))
        self._new_layer_from_file = new_layer_from_file(weakref.proxy(self))

        self._shapes = shapes(weakref.proxy(self))
        self._shape = None

        # the radius is estimated when plot_map is called
        self._estimated_radius = None

        # cache commonly used transformers
        self._transf_plot_to_lonlat = Transformer.from_crs(
            self.crs_plot,
            self.get_crs(4326),
            always_xy=True,
        )
        self._transf_lonlat_to_plot = Transformer.from_crs(
            self.get_crs(4326),
            self.crs_plot,
            always_xy=True,
        )

        # a set to hold references to the compass objects
        self._compass = set()

        # a set holding the callback ID's from added logos
        self._logo_cids = set()

        # keep track of all decorated functions that need to be "undecorated" so that
        # Maps-objects can be garbage-collected
        self._cleanup_functions = set()

        if not hasattr(self.parent, "_wms_legend"):
            self.parent._wms_legend = dict()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.cleanup()
        gc.collect()

    def __getattribute__(self, key):
        if key == "plot_specs":
            raise AttributeError(
                "EOmaps: 'm.plot_specs' has been removed in v4.0!\n For instructions "
                + "on how to quickly port your script to EOmaps >= 4.0, see: \n"
                + r"https://eomaps.readthedocs.io/en/latest/FAQ.html#port-script-from-eomaps-v3-x-to-v4-x"
            )
        elif key == "set_plot_specs":
            raise AttributeError(
                "EOmaps: 'm.set_plot_specs' has been removed in v4.0!\n For instructions "
                + "on how to quickly port your script to EOmaps >= 4.0, see: \n"
                + r"https://eomaps.readthedocs.io/en/latest/FAQ.html#port-script-from-eomaps-v3-x-to-v4-x"
            )
        else:
            return object.__getattribute__(self, key)

    @staticmethod
    def _proxy(obj):
        # create a proxy if the object is not yet a proxy
        if type(obj) is not weakref.ProxyType:
            return weakref.proxy(obj)
        else:
            return obj

    def cleanup(self):
        """
        Cleanup all references to the object so that it can be safely deleted.
        (primarily used internally to clear objects if the figure is closed)

        Note
        ----
        Executing this function will remove ALL attached callbacks
        and delete all assigned datasets & pre-computed values.

        ONLY execute this if you do not need to do anything with the layer
        (except for looking at it)
        """
        # remove the xlim-callback since it contains a reference to self
        if hasattr(self, "_cid_xlim"):
            self.ax.callbacks.disconnect(self._cid_xlim)
            del self._cid_xlim

        # disconnect all callbacks from attached logos
        for cid in self._logo_cids:
            self.figure.f.canvas.mpl_disconnect(cid)
        self._logo_cids.clear()

        # disconnect all click, pick and keypress callbacks
        self.cb._reset_cids()

        # call all additional cleanup functions
        for f in self._cleanup_functions:
            f()
        self._cleanup_functions.clear()

        # remove the children from the parent Maps object
        if self in self.parent._children:
            self.parent._children.remove(self)

    from_file = from_file
    read_file = read_file

    @property
    def layer(self):
        """
        The layer-name associated with this Maps-object.
        """
        return self._layer

    @property
    def shape(self):
        """
        The shape that will be used to represent the dataset if `m.plot_map()` is called

        By default "ellipses" is used for datasets < 500k datapoints and for plots
        where no explicit data is assigned, and otherwise "shade_raster" is used
        for 2D datasets and "shade_points" is used for unstructured datasets.

        """
        if self._shape is None:
            if self.data is not None:
                size = np.size(self.data)
                if size > 500_000:
                    if _register_datashader():
                        if len(self.data.shape) == 2:
                            # shade_raster requires 2D data!
                            self.set_shape.shade_raster()
                        else:
                            # shade_points should work for any dataset
                            self.set_shape.shade_points()
                    else:
                        print(
                            "EOmaps-Warning: you attempt to plot a large dataset"
                            + f"({size} datapoints) but the 'datashader' library could"
                            + " not be imported! The plot might take long to finish!"
                            + "... defaulting to 'ellipses' as plot-shape."
                        )
                        self.set_shape.ellipses()
                else:
                    self.set_shape.ellipses()
            else:
                self.set_shape.ellipses()

        return self._shape

    @property
    def all(self):
        """
        Get a Maps-object on the "all" layer.

        Use it just as any other Maps-object. (It's the same as `Maps(layer="all")`)

        >>> m.all.cb.click.attach.annotate()

        """
        if not hasattr(self, "_all"):
            self._all = self.new_layer("all")
        return self._all

    def show(self):
        """
        Make the layer of this `Maps`-object visible.
        (a shortcut for `m.show_layer(m.layer)`)

        If matploltib is used in non-interactive mode, (e.g. `plt.ioff()`)
        `plt.show()` is called as well!
        """

        self.show_layer(self.layer)

        if not plt.isinteractive():
            plt.show()

    @property
    def ax(self):
        return self._ax

    @property
    @wraps(new_layer_from_file)
    def new_layer_from_file(self):
        return self._new_layer_from_file

    def new_layer(
        self,
        layer=None,
        copy_data_specs=False,
        copy_classify_specs=False,
        copy_shape=True,
    ):
        """
        Create a new Maps-object that shares the same plot-axes.

        Parameters
        ----------
        layer : int, str or None
            The name of the layer at which map-features are plotted.

            - If "all": the corresponding feature will be added to ALL layers
            - If None, the layer of the parent object is used.

            The default is None.
        copy_data_specs, copy_shape, copy_classify_specs : bool
            Indicator if the corresponding properties should be copied to
            the new layer. By default no settings are copied.

        Returns
        -------
        eomaps.Maps
            A connected copy of the Maps-object that shares the same plot-axes.

        See Also
        --------
        copy : general way for copying Maps objects
        """

        if layer is None:
            layer = copy.deepcopy(self.layer)

        m = self.copy(
            data_specs=copy_data_specs,
            classify_specs=copy_classify_specs,
            shape=copy_shape,
            parent=self.parent,
            gs_ax=self.figure.ax,
            layer=layer,
        )

        # re-initialize all sliders and buttons to include the new layer
        self.util._reinit_widgets()
        return m

    def _get_inset_boundary(self, x, y, xy_crs, radius, radius_crs, shape, n=100):
        """
        get inset map boundary


        Parameters
        ----------
        x : TYPE
            DESCRIPTION.
        y : TYPE
            DESCRIPTION.
        xy_crs : TYPE
            DESCRIPTION.
        radius : TYPE
            DESCRIPTION.
        radius_crs : TYPE
            DESCRIPTION.
        shape : TYPE
            DESCRIPTION.
        n : TYPE, optional
            DESCRIPTION. The default is 100.

        Returns
        -------
        boundary : TYPE
            DESCRIPTION.

        """

        shp = self.set_shape._get(shape)

        if shape == "ellipses":
            shp_pts = shp._get_ellipse_points(
                x=np.atleast_1d(x),
                y=np.atleast_1d(y),
                crs=xy_crs,
                radius=radius,
                radius_crs=radius_crs,
                n=n,
            )
            bnd_verts = np.stack(shp_pts[:2], axis=2)[0]

        elif shape == "rectangles":
            shp_pts = shp._get_rectangle_verts(
                x=np.atleast_1d(x),
                y=np.atleast_1d(y),
                crs=xy_crs,
                radius=radius,
                radius_crs=radius_crs,
                n=n,
            )
            bnd_verts = shp_pts[0][0]

        elif shape == "geod_circles":
            shp_pts = shp._get_geod_circle_points(
                x=np.atleast_1d(x),
                y=np.atleast_1d(y),
                crs=xy_crs,
                radius=radius,
                # radius_crs=radius_crs,
                n=n,
            )
            bnd_verts = np.stack(shp_pts[:2], axis=2).squeeze()
        boundary = mpl.path.Path(bnd_verts)

        return boundary, bnd_verts

    def new_inset_map(
        self,
        xy=(45, 45),
        xy_crs=4326,
        radius=5,
        radius_crs=None,
        plot_position=(0.5, 0.5),
        plot_size=0.5,
        inset_crs=4326,
        layer="all",
        boundary=True,
        shape="ellipses",
        indicate_extent=True,
        **kwargs,
    ):
        """
        Create a new (empty) inset-map that shows a zoomed-in view on a given extent.
        The returned Maps-object can then be used to populate the inset-map with
        features, datasets etc.

        See examples below on how to use inset-maps.


        Note
        ----
        - By default NO features are added to the inset-map!
          Use it just like any other Maps-object to add features or plot datasets!
        - Zooming is disabled on inset-maps for now due to issues with zoom-events on
          overlapping axes.
        - Non-rectangular cropping of WebMap services is not yet supported.
          (e.g. use "rectangles" as shape and the native CRS of the WebMap service
          for the inset map.)

        Parameters
        ----------
        xy : tuple, optional
            The center-coordinates of the area to indicate.
            (provided in the xy_crs projection)
            The default is (45., 45.).
        xy_crs : any, optional
            The crs used for specifying the center position of the inset-map.
            (can be any crs definition supported by PyProj)
            The default is 4326 (e.g. lon/lat).
        radius : float or tuple, optional
            The radius of the extent to indicate.
            (provided in units of the radius_crs projection)
            The default is 5.
        radius_crs : None or a crs-definition, optional
            The crs used for specifying the radius. (can be any crs definition
            supported by PyProj)

            - If None:  The crs provided as "xy_crs" is used
            - If shape == "geod_circles", "radius_crs" must be None since the radius
              of a geodesic circle is defined in meters!

            The default is None.
        plot_position : tuple, optional
            The center-position of the inset map in relative units (0-1) with respect to
            the figure size. The default is (.5,.5).
        plot_size : float, optional
            The relative size of the inset-map compared to the figure width.
            The default is 0.5.
        inset_crs : any, optional
            The crs that is used in the inset-map.
            The default is 4326.
        layer : str, optional
            The layer associated with the inset-map.
            Note: If you specify a dedicated layer for the inset-map, the contents
            of the inset-map will only be visible on that specific layer!
            To create different views of an inset-map for different layers,
            simply create a child-layer from the inset-map (see examples below).
            By default the "all" layer is used so that the contents of the inset-map
            are visible independent of the currently visible layer.
            The default is "all".
        boundary: bool or dict, optional
            - If True: indicate the boundary of the inset-map with default colors
              (e.g.: {"ec":"r", "lw":2})
            - If False: don't add edgecolors to the boundary of the inset-map
            - if dict: use the provided values for "ec" (e.g. edgecolor) and
              "lw" (e.g. linewidth)

            The default is True.
        shape : str, optional
            The shape to use. Can be either "ellipses", "rectangles" or "geod_circles".
            The default is "ellipses".
        indicate_extent : bool or dict, optional
            - If True: add a polygon representing the inset-extent to the parent map.
            - If a dict is provided, it will be used to update the appearance of the
              added polygon (e.g. facecolor, edgecolor, linewidth etc.)

            NOTE: you can also use `m_inset.indicate_inset_extent(...)` to manually
            indicate the inset-shape on arbitrary Maps-objects.

        Returns
        -------
        m : eomaps.Maps
            A eomaps.Maps-object of the inset-map.
            (use it just like any other Maps-object)

        See also
        --------
        The following additional methods are defined on `_InsetMaps` objects

        m.indicate_inset_extent :
            Plot a polygon representing the extent of the inset map on another Maps
            object.
        m.set_inset_position :
            Set the (center) position and size of the inset-map.

        Examples
        --------

        Simple example:

        >>> m = Maps()
        >>> m.add_feature.preset.coastline()
        >>> m2 = m.new_inset_map(xy=(45, 45), radius=10,
        >>>                      plot_position=(.3, .5), plot_size=.7)
        >>> m2.add_feature.preset.ocean()

        ... a bit more complexity:

        >>> m = Maps(Maps.CRS.Orthographic())
        >>> m.add_feature.preset.coastline() # add some coastlines
        >>> m2 = m.new_inset_map(xy=(5, 45),
        >>>                      xy_crs=4326,
        >>>                      shape="geod_circles",
        >>>                      radius=1000000,
        >>>                      plot_position=(.3, .4),
        >>>                      plot_size=.5,
        >>>                      inset_crs=3035,
        >>>                      edgecolor="g",
        >>>                      indicate_extent=False)
        >>>
        >>> m2.add_feature.preset.coastline()
        >>> m2.add_feature.preset.ocean()
        >>> m2.add_feature.preset.land()
        >>> m2.set_data([1, 2, 3], [5, 6, 7], [45, 46, 47], crs=4326)
        >>> m2.plot_map()
        >>> m2.add_annotation(ID=1)
        >>> m2.indicate_inset_extent(m, ec="g", fc=(0,1,0,.25))

        Multi-layer inset-maps:

        >>> m = Maps(layer="first")
        >>> m.add_feature.preset.coastline()
        >>> m3 = m.new_layer("second")
        >>> m3.add_feature.preset.ocean()
        >>> # create an inset-map on the "first" layer
        >>> m2 = m.new_inset_map(layer="first")
        >>> m2.add_feature.preset.coastline()
        >>> # create a new layer of the inset-map that will be
        >>> # visible if the "second" layer is visible
        >>> m3 = m2.new_layer(layer="second")
        >>> m3.add_feature.preset.coastline()
        >>> m3.add_feature.preset.land()

        >>> m.util.layer_selector()

        """

        if "edgecolor" in kwargs or "linewidth" in kwargs:
            warnings.warn(
                "EOmaps: 'edgecolor' and 'linewidth' kwargs for `m.new_inset_map()`"
                + " are depreciated! use `boundary=dict(ec='r', lw=1)` instead!",
                category=DeprecationWarning,
                stacklevel=2,
            )

            ec = kwargs.pop("edgecolor", "r")
            lw = kwargs.pop("linewidth", 1)

            boundary = dict(ec=ec, lw=lw)
            boundary.update(kwargs.pop("boundary", dict()))

        m2 = _InsetMaps(
            crs=inset_crs,
            parent=self,
            layer=layer,
            xy=xy,
            radius=radius,
            plot_position=plot_position,
            plot_size=plot_size,
            xy_crs=xy_crs,
            radius_crs=radius_crs,
            boundary=boundary,
            shape=shape,
            indicate_extent=indicate_extent,
        )

        return m2

    @property
    @wraps(cb_container)
    def cb(self):
        return self._cb

    @property
    @wraps(utilities)
    def util(self):
        return self._utilities

    @property
    @wraps(map_objects)
    def figure(self):
        return self._figure

    @staticmethod
    def _get_cartopy_crs(crs):
        if isinstance(crs, Maps.CRS.CRS):  # already a cartopy CRS
            cartopy_proj = crs
        elif crs == 4326:
            cartopy_proj = ccrs.PlateCarree()
        elif isinstance(crs, (int, np.integer)):
            cartopy_proj = ccrs.epsg(crs)
        elif isinstance(crs, CRS):  # pyproj CRS
            for (
                subgrid,
                equi7crs,
            ) in Maps.CRS.Equi7Grid_projection._pyproj_crs_generator():
                if equi7crs == crs:
                    cartopy_proj = Maps.CRS.Equi7Grid_projection(subgrid)
                    break
        else:
            raise AssertionError(f"EOmaps: cannot identify the CRS for: {crs}")
        return cartopy_proj

    def _init_figure(self, gs_ax=None, plot_crs=None, **kwargs):

        if self.parent.figure.f is None:
            self._f = plt.figure(**kwargs)
            newfig = True
        else:
            newfig = False

        if isinstance(gs_ax, plt.Axes):
            # in case an axis is provided, attempt to use it
            ax = gs_ax
            gs = gs_ax.get_gridspec()
            newax = False
        else:
            newax = True
            # create a new axis
            if gs_ax is None:
                gs = GridSpec(
                    nrows=1, ncols=1, left=0.01, right=0.99, bottom=0.05, top=0.95
                )
                gsspec = gs[:]
            elif isinstance(gs_ax, SubplotSpec):
                gsspec = gs_ax
                gs = gsspec.get_gridspec()

            projection = self._get_cartopy_crs(plot_crs)

            ax = self.figure.f.add_subplot(
                gsspec, projection=projection, aspect="equal", adjustable="box"
            )

        self._ax = ax

        self._gridspec = gs

        # initialize the callbacks
        self.cb._init_cbs()

        # set the _ignore_cb_events property on the parent
        # (used to temporarily disconnect all callbacks)
        self.parent._ignore_cb_events = False

        if newax:  # only if a new axis has been created
            self._ax_xlims = (0, 0)
            self._ax_ylims = (0, 0)

            def xlims_change(*args, **kwargs):
                if self._ax_xlims != args[0].get_xlim():
                    self.BM._refetch_bg = True
                    # self.figure.f.stale = True
                    self._ax_xlims = args[0].get_xlim()

            # def ylims_change(*args, **kwargs):
            #     if self._ax_ylims != args[0].get_ylim():
            #         print("y limchange", self.BM._refetch_bg)
            #         self.BM._refetch_bg = True
            #         self._ax_ylims = args[0].get_ylim()

            # do this only on xlims and NOT on ylims to avoid recursion
            # (plot aspect ensures that y changes if x changes)
            self._cid_xlim = self.figure.ax.callbacks.connect(
                "xlim_changed", xlims_change
            )
            # self.figure.ax.callbacks.connect("ylim_changed", ylims_change)

        if newfig:  # only if a new figure has been initialized
            # attach a callback that is executed when the figure is closed
            self._cid_onclose = self.figure.f.canvas.mpl_connect(
                "close_event", self._on_close
            )
            # attach a callback that is executed if the figure canvas is resized
            self._cid_resize = self.figure.f.canvas.mpl_connect(
                "resize_event", self._on_resize
            )

        # if we haven't attached an axpicker so far, do it!
        if self.parent._layout_editor is None:
            self.parent._layout_editor = LayoutEditor(self.parent, modifier="alt+l")

        if newfig:
            # we only need to call show if a new figure has been created!
            if (
                plt.isinteractive()
                or plt.get_backend() == "module://ipympl.backend_nbagg"
            ):
                # make sure to call show only if we use an interactive backend...
                # or within the ipympl backend (otherwise it will block subsequent code!)
                plt.show()

    def _on_resize(self, event):
        # make sure the background is re-fetched if the canvas has been resized
        # (required for peeking layers after the canvas has been resized
        #  and for webagg and nbagg backends to correctly re-draw the layer)
        self.BM._refetch_bg = True

    def _on_close(self, event):
        # reset attributes that might use up a lot of memory when the figure is closed
        for m in [self.parent, *self.parent._children]:

            if hasattr(m, "_props"):
                m._props.clear()
                del m._props

            if hasattr(m, "tree"):
                del m.tree

            if hasattr(m.figure, "coll"):
                m.figure.coll = None

            m.data_specs.delete()
            m.cleanup()

        # delete the tempfolder containing the memmaps
        if hasattr(self.parent, "_tmpfolder"):
            self.parent._tmpfolder.cleanup()

        # run garbage-collection to immediately free memory
        gc.collect

    @property
    def _ignore_cb_events(self):
        return self.parent._persistent_ignore_cb_events

    @_ignore_cb_events.setter
    def _ignore_cb_events(self, val):
        self.parent._persistent_ignore_cb_events = val

    @property
    def BM(self):
        """The Blit-Manager used to dynamically update the plots"""
        m = weakref.proxy(self)
        if self.parent._BM is None:
            self.parent._BM = BlitManager(m)
            self.parent._BM._bg_layer = m.parent.layer
        return self.parent._BM

    def _add_child(self, m):
        self.parent._children.add(m)

    @property
    def parent(self):
        """
        The parent-object to which this Maps-object is connected to.
        If None, `self` is returned!
        """
        if self._parent is None:
            return weakref.proxy(self)
        else:
            return self._parent

    @parent.setter
    def parent(self, parent):
        assert parent is not self, "EOmaps: A Maps-object cannot be its own parent!"
        assert self._parent is None, "EOmaps: There is already a parent Maps object!"

        if parent is not None:
            self._parent = self._proxy(parent)
        else:
            # None cannot be weak-referenced!
            self._parent = None

        if parent not in [self, None]:
            # add the child to the topmost parent-object
            self.parent._add_child(self)

    def join_limits(self, *args):
        """
        Join the x- and y- limits of the axes (e.g. on zoom)

        Parameters
        ----------
        *args :
            the axes to join.
        """
        for m in args:
            if m is not self:
                self._join_axis_limits(weakref.proxy(m))

    def _join_axis_limits(self, m):
        if self.figure.ax.projection != m.figure.ax.projection:
            warnings.warn(
                "EOmaps: joining axis-limits is only possible for "
                + "axes with the same projection!"
            )
            return

        self.figure.ax._EOmaps_joined_action = False
        m.figure.ax._EOmaps_joined_action = False

        # Declare and register callbacks
        def child_xlims_change(event_ax):
            if event_ax._EOmaps_joined_action is not m.figure.ax:
                m.figure.ax._EOmaps_joined_action = event_ax
                m.figure.ax.set_xlim(event_ax.get_xlim())
            event_ax._EOmaps_joined_action = False

        def child_ylims_change(event_ax):
            if event_ax._EOmaps_joined_action is not m.figure.ax:
                m.figure.ax._EOmaps_joined_action = event_ax
                m.figure.ax.set_ylim(event_ax.get_ylim())
            event_ax._EOmaps_joined_action = False

        def parent_xlims_change(event_ax):
            if event_ax._EOmaps_joined_action is not self.figure.ax:
                self.figure.ax._EOmaps_joined_action = event_ax
                self.figure.ax.set_xlim(event_ax.get_xlim())
            event_ax._EOmaps_joined_action = False

        def parent_ylims_change(event_ax):
            if event_ax._EOmaps_joined_action is not self.figure.ax:
                self.figure.ax._EOmaps_joined_action = event_ax
                self.figure.ax.set_ylim(event_ax.get_ylim())

            event_ax._EOmaps_joined_action = False

        self.figure.ax.callbacks.connect("xlim_changed", child_xlims_change)
        self.figure.ax.callbacks.connect("ylim_changed", child_ylims_change)

        m.figure.ax.callbacks.connect("xlim_changed", parent_xlims_change)
        m.figure.ax.callbacks.connect("ylim_changed", parent_ylims_change)

    def copy(
        self,
        data_specs=False,
        classify_specs=True,
        shape=True,
        **kwargs,
    ):
        """
        Create a (deep)copy of the Maps object that shares selected specifications.

        -> useful to quickly create plots with similar configurations

        Parameters
        ----------
        data_specs, classify_specs, shape : bool or "shared", optional
            Indicator if the corresponding properties should be copied.

            - if True: ALL corresponding properties are copied

            By default, "classify_specs" and the "shape" are copied.

        kwargs :
            Additional kwargs passed to `m = Maps(**kwargs)`
            (e.g. crs, f, gs_ax, orientation, layer)
        Returns
        -------
        copy_cls : eomaps.Maps object
            a new Maps class.
        """

        copy_cls = Maps(**kwargs)

        if data_specs is True:
            data_specs = list(self.data_specs.keys())
            copy_cls.set_data_specs(
                **{key: copy.deepcopy(val) for key, val in self.data_specs}
            )

        if shape is True:
            if self.shape is not None:
                getattr(copy_cls.set_shape, self.shape.name)(**self.shape._initargs)

        if classify_specs is True:
            classify_specs = list(self.classify_specs.keys())
            copy_cls.set_classify_specs(
                scheme=self.classify_specs.scheme, **self.classify_specs
            )

        return copy_cls

    @property
    def data(self):
        return self.data_specs.data

    @data.setter
    def data(self, val):
        # for downward-compatibility
        self.data_specs.data = val

    @property
    @wraps(shapes)
    def set_shape(self):
        return self._shapes

    def set_data_specs(
        self,
        data=None,
        x=None,
        y=None,
        crs=None,
        encoding=None,
        cpos="c",
        cpos_radius=None,
        **kwargs,
    ):
        """
        Set the properties of the dataset you want to plot.

        Use this function to update multiple data-specs in one go
        Alternatively you can set the data-specifications via

            >>> m.data_specs.< property > = ...`

        Parameters
        ----------
        data : array-like
            The data of the Maps-object.
            Accepted inputs are:

            - a pandas.DataFrame with the coordinates and the data-values
            - a pandas.Series with only the data-values
            - a 1D or 2D numpy-array with the data-values
            - a 1D list of data values

        x, y : str, optional
            Specify the coordinates associated with the provided data.
            Accepted inputs are:

            - a string (corresponding to the column-names of the `pandas.DataFrame`)

              - ONLY if "data" is provided as a pandas.DataFrame!

            - a pandas.Series
            - a 1D or 2D numpy-array
            - a 1D list

            The default is "lon" and "lat".
        crs : int, dict or str
            The coordinate-system of the provided coordinates.
            Can be one of:

            - PROJ string
            - Dictionary of PROJ parameters
            - PROJ keyword arguments for parameters
            - JSON string with PROJ parameters
            - CRS WKT string
            - An authority string [i.e. 'epsg:4326']
            - An EPSG integer code [i.e. 4326]
            - A tuple of ("auth_name": "auth_code") [i.e ('epsg', '4326')]
            - An object with a `to_wkt` method.
            - A :class:`pyproj.crs.CRS` class

            (see `pyproj.CRS.from_user_input` for more details)

            The default is 4326 (e.g. geographic lon/lat crs)
        parameter : str, optional
            ONLY relevant if a pandas.DataFrame that specifyes both the coordinates
            and the data-values is provided as `data`!

            The name of the column that should be used as parameter.

            If None, the first column (despite of the columns assigned as "x" and "y")
            will be used. The default is None.
        encoding : dict or False, optional
            A dict containing the encoding information in case the data is provided as
            encoded values (useful to avoid decoding large integer-encoded datasets).

            If provided, the data will be decoded "on-demand" with respect to the
            provided "scale_factor" and "add_offset" according to the formula:

            >>> actual_value = encoding["add_offset"] + encoding["scale_factor"] * value

            Note: Colorbars and pick-callbakcs will use the encoding-information to
            display the actual data-values!

            If False, no value-transformation is performed.
            The default is False
        cpos : str, optional
            Indicator if the provided x-y coordinates correspond to the center ("c"),
            upper-left corner ("ul"), lower-left corner ("ll") etc.  of the pixel.
            If any value other than "c" is provided, a "cpos_radius" must be set!
            The default is "c".
        cpos_radius : int or tuple, optional
            The pixel-radius (in the input-crs) that will be used to set the
            center-position of the provided data.
            If a number is provided, the pixels are treated as squares.
            If a tuple (rx, ry) is provided, the pixels are treated as rectangles.
            The default is None.

        Examples
        --------

        - using a single `pandas.DataFrame`

          >>> data = pd.DataFrame(dict(lon=[...], lat=[...], a=[...], b=[...]))
          >>> m.set_data(data, x="lon", y="lat", parameter="a", crs=4326)

        - using individual `pandas.Series`

          >>> lon, lat, vals = pd.Series([...]), pd.Series([...]), pd.Series([...])
          >>> m.set_data(vals, x=lon, y=lat, crs=4326)

        - using 1D lists

          >>> lon, lat, vals = [...], [...], [...]
          >>> m.set_data(vals, x=lon, y=lat, crs=4326)

        - using 1D or 2D numpy.arrays

          >>> lon, lat, vals = np.array([[...]]), np.array([[...]]), np.array([[...]])
          >>> m.set_data(vals, x=lon, y=lat, crs=4326)

        - integer-encoded datasets

          >>> lon, lat, vals = [...], [...], [1, 2, 3, ...]
          >>> encoding = dict(scale_factor=0.01, add_offset=1)
          >>> # colorbars and pick-callbacks will now show values as (1 + 0.01 * value)
          >>> # e.g. the "actual" data values are [0.01, 0.02, 0.03, ...]
          >>> m.set_data(vals, x=lon, y=lat, crs=4326, encoding=encoding)
        """

        # depreciate the use of "xcoord" and "ycoord"... use "x", "y" instead
        if "xcoord" in kwargs:
            if x is None:
                warnings.warn(
                    "EOmaps: using 'xcoord' in 'm.set_data' is depreciated. "
                    + "Use 'x=...' instead!",
                    DeprecationWarning,
                    stacklevel=2,
                )
                x = kwargs.pop("xcoord")
            else:
                raise TypeError("EOmaps: You cannot provide both 'x' and 'xcoord'!")
        if "ycoord" in kwargs:
            if y is None:
                warnings.warn(
                    "EOmaps: using 'ycoord' in 'm.set_data' is depreciated. "
                    + "Use 'y=...' instead!",
                    DeprecationWarning,
                    stacklevel=2,
                )
                y = kwargs.pop("ycoord")
            else:
                raise TypeError("EOmaps: You cannot provide both 'y' and 'ycoord'!")

        if data is not None:
            self.data_specs.data = data

        if x is not None:
            self.data_specs.x = x

        if y is not None:
            self.data_specs.y = y

        if crs is not None:
            self.data_specs.crs = crs

        for key, val in kwargs.items():
            self.data_specs[key] = val

        if encoding is not None:
            self.data_specs.encoding = encoding

        if cpos is not None:
            self.data_specs.cpos = cpos

        if cpos_radius is not None:
            self.data_specs.cpos_radius = cpos_radius

    set_data = set_data_specs

    def _get_mcl_subclass(self, s):
        # get a subclass that inherits the docstring from the corresponding
        # mapclassify classifier

        class scheme:
            @wraps(s)
            def __init__(_, *args, **kwargs):
                pass

            def __new__(cls, **kwargs):
                if "y" in kwargs:
                    print(
                        "EOmaps: The values (e.g. the 'y' parameter) are "
                        + "assigned internally... only provide additional "
                        + "parameters that specify the classification scheme!"
                    )
                    kwargs.pop("y")

                self.classify_specs._set_scheme_and_args(scheme=s.__name__, **kwargs)

        scheme.__doc__ = s.__doc__
        return scheme

    @property
    def set_classify(self):
        from textwrap import dedent

        assert _register_mapclassify(), (
            "EOmaps: Missing dependency: 'mapclassify' \n ... please install"
            + " (conda install -c conda-forge mapclassify) to use data-classifications."
        )

        s = SimpleNamespace(
            **{
                i: self._get_mcl_subclass(getattr(mapclassify, i))
                for i in mapclassify.CLASSIFIERS
            }
        )
        s.__doc__ = dedent(
            """
            Interface to the classifiers provided by the 'mapclassify' module.

            To set a classification scheme for a given Maps-object, simply use:

            >>> m.set_classify.<SCHEME>(...)

            Where `<SCHEME>` is the name of the desired classification and additional
            parameters are passed in the call. (check docstrings for more info!)


            Note
            ----
            The following calls have the same effect:

            >>> m.set_classify.Quantiles(k=5)
            >>> m.set_classify_specs(scheme="Quantiles", k=5)

            Using `m.set_classify()` is the same as using `m.set_classify_specs()`!
            However, `m.set_classify()` will provide autocompletion and proper
            docstrings once the Maps-object is initialized which greatly enhances
            the usability.

            """
        )

        return s

    def set_classify_specs(self, scheme=None, **kwargs):
        """
        Set classification specifications for the data.
        (classification is performed by the `mapclassify` module)

        Note
        ----
        The following calls have the same effect:

        >>> m.set_classify.Quantiles(k=5)
        >>> m.set_classify_specs(scheme="Quantiles", k=5)

        Using `m.set_classify()` is the same as using `m.set_classify_specs()`!
        However, `m.set_classify()` will provide autocompletion and proper
        docstrings once the Maps-object is initialized which greatly enhances
        the usability.

        Parameters
        ----------
        scheme : str
            The classification scheme to use.
            (the list is accessible via `m.classify_specs.SCHEMES`)

            E.g. one of (possible kwargs in brackets):

                - BoxPlot (hinge)
                - EqualInterval (k)
                - FisherJenks (k)
                - FisherJenksSampled (k, pct, truncate)
                - HeadTailBreaks ()
                - JenksCaspall (k)
                - JenksCaspallForced (k)
                - JenksCaspallSampled (k, pct)
                - MaxP (k, initial)
                - MaximumBreaks (k, mindiff)
                - NaturalBreaks (k, initial)
                - Quantiles (k)
                - Percentiles (pct)
                - StdMean (multiples)
                - UserDefined (bins)

        kwargs :
            kwargs passed to the call to the respective mapclassify classifier
            (dependent on the selected scheme... see above)
        """

        assert _register_mapclassify(), (
            "EOmaps: Missing dependency: 'mapclassify' \n ... please install"
            + " (conda install -c conda-forge mapclassify) to use data-classifications."
        )

        self.classify_specs._set_scheme_and_args(scheme, **kwargs)

    def _set_cpos(self, x, y, radiusx, radiusy, cpos):
        # use x = x + ...   instead of x +=  to allow casting from int to float
        if cpos == "c":
            pass
        elif cpos == "ll":
            x = x + radiusx
            y = y + radiusy
        elif cpos == "ul":
            x = x + radiusx
            y = y - radiusy
        elif cpos == "lr":
            x = x - radiusx
            y = y + radiusy
        elif cpos == "ur":
            x = x - radiusx
            y = y - radiusx

        return x, y

    @property
    def crs_plot(self):
        """
        The crs used for plotting.
        """
        return self._crs_plot_cartopy

    def get_crs(self, crs):
        """
        get the pyproj CRS instance of a given crs specification

        Parameters
        ----------
        crs : "in", "out" or a crs definition
            the crs to return
            if "in" : the crs defined in m.data_specs.crs
            if "out" or "plot" : the crs used for plotting

        Returns
        -------
        crs : pyproj.CRS
            the pyproj CRS instance

        """
        if crs == "in":
            crs = self.data_specs.crs
        elif crs == "out" or crs == "plot":
            crs = self.crs_plot

        if not hasattr(self, "_crs_cache"):
            self._crs_cache = dict()

        h = hash(crs)
        if h in self._crs_cache:
            crs = self._crs_cache[h]
        else:
            crs = CRS.from_user_input(crs)
            self._crs_cache[h] = crs
        return crs

    def _identify_data(self, data=None, x=None, y=None, parameter=None):
        """
        Identify the way how the data has been provided and convert to the
        internal structure.
        """

        if data is None:
            data = self.data_specs.data
        if x is None:
            x = self.data_specs.x
        if y is None:
            y = self.data_specs.y
        if parameter is None:
            parameter = self.data_specs.parameter

        # check other types before pandas to avoid unnecessary import
        if data is not None and not isinstance(data, (list, tuple, np.ndarray)):
            if _register_pandas() and isinstance(data, pd.DataFrame):

                if parameter is not None:
                    # get the data-values
                    z_data = data[parameter].values
                else:
                    z_data = np.repeat(np.nan, len(data))

                # get the index-values
                ids = data.index.values

                if isinstance(x, str) and isinstance(y, str):
                    # get the data-coordinates
                    xorig = data[x].values
                    yorig = data[y].values
                else:
                    assert isinstance(x, (list, np.ndarray, pd.Series)), (
                        "'x' must be either a column-name, or explicit values "
                        " specified as a list, a numpy-array or a pandas"
                        + f" Series object if you provide the data as '{type(data)}'"
                    )
                    assert isinstance(y, (list, np.ndarray, pd.Series)), (
                        "'y' must be either a column-name, or explicit values "
                        " specified as a list, a numpy-array or a pandas"
                        + f" Series object if you provide the data as '{type(data)}'"
                    )

                    xorig = np.asanyarray(x)
                    yorig = np.asanyarray(y)

                return z_data, xorig, yorig, ids, parameter

        # identify all other types except for pandas.DataFrames

        # lazily check if pandas was used
        pandas_series_data = False
        for iname, i in zip(("x", "y", "data"), (x, y, data)):
            if iname == "data" and i is None:
                # allow empty datasets
                continue

            if not isinstance(i, (list, np.ndarray)):
                if _register_pandas() and not isinstance(i, pd.Series):
                    raise AssertionError(
                        f"{iname} values must be a list, numpy-array or pandas.Series"
                    )
                else:
                    if iname == "data":
                        pandas_series_data = True

        # get the data-coordinates
        xorig = np.asanyarray(x)
        yorig = np.asanyarray(y)

        if data is not None:
            # get the data-values
            z_data = np.asanyarray(data)
        else:
            if xorig.shape == yorig.shape:
                z_data = np.full(xorig.shape, np.nan)
            elif (
                (xorig.shape != yorig.shape)
                and (len(xorig.shape) == 1)
                and (len(yorig.shape) == 1)
            ):
                z_data = np.full((xorig.shape[0], yorig.shape[0]), np.nan)

        # get the index-values
        if pandas_series_data is True:
            # use actual index values if pd.Series was passed as "data"
            ids = data.index.values
        else:
            # use numeric index values for all other types
            ids = np.arange(z_data.size)

        return z_data, xorig, yorig, ids, parameter

    def _prepare_data(
        self,
        data=None,
        in_crs=None,
        plot_crs=None,
        radius=None,
        radius_crs=None,
        cpos=None,
        cpos_radius=None,
        parameter=None,
        x=None,
        y=None,
        buffer=None,
        assume_sorted=True,
    ):
        if in_crs is None:
            in_crs = self.data_specs.crs
        if cpos is None:
            cpos = self.data_specs.cpos
        if cpos_radius is None:
            cpos_radius = self.data_specs.cpos_radius

        props = dict()
        # get coordinate transformation from in_crs to plot_crs
        # make sure to re-identify the CRS with pyproj to correctly skip re-projection
        # in case we use in_crs == plot_crs

        crs1 = CRS.from_user_input(in_crs)
        crs2 = CRS.from_user_input(self._crs_plot)

        # identify the provided data and get it in the internal format
        z_data, xorig, yorig, ids, parameter = self._identify_data(
            data=data, x=x, y=y, parameter=parameter
        )

        if cpos is not None and cpos != "c":
            # fix position of pixel-center in the input-crs
            assert (
                cpos_radius is not None
            ), "you must specify a 'cpos_radius if 'cpos' is not 'c'"
            if isinstance(cpos_radius, (list, tuple)):
                rx, ry = cpos_radius
            else:
                rx = ry = cpos_radius

            xorig, yorig = self._set_cpos(xorig, yorig, rx, ry, cpos)

        # transform center-points to the plot_crs
        if len(xorig.shape) == len(z_data.shape):
            assert xorig.shape == z_data.shape and yorig.shape == z_data.shape, (
                f"EOmaps: The data-shape {z_data.shape} and coordinate-shape "
                + f"x={xorig.shape}, y={yorig.shape} do not match!"
            )

        # invoke the shape-setter to make sure a shape is set
        used_shape = self.shape

        # --------- sort by coordinates
        # this is required to avoid glitches in "raster" and "shade_raster"
        # since QuadMesh requires sorted coordinates!
        # (currently only implemented for 1D coordinates and 2D data)
        if assume_sorted is False:
            if used_shape.name in ["raster", "shade_raster"]:
                if (
                    len(xorig.shape) == 1
                    and len(yorig.shape) == 1
                    and len(z_data.shape) == 2
                ):

                    xs, ys = np.argsort(xorig), np.argsort(yorig)
                    np.take(xorig, xs, out=xorig, mode="wrap")
                    np.take(yorig, ys, out=yorig, mode="wrap")
                    np.take(
                        np.take(z_data, xs, 0),
                        indices=ys,
                        axis=1,
                        out=z_data,
                        mode="wrap",
                    )
                else:
                    print(
                        "EOmaps: using 'assume_sorted=False' is only possible"
                        + "if you use 1D coordinates + 2D data!"
                        + "...continuing without sorting."
                    )
            else:
                print(
                    "EOmaps: using 'assume_sorted=False' is only relevant for "
                    + "the shapes ['raster', 'shade_raster']! "
                    + "...continuing without sorting."
                )

        if crs1 == crs2:
            if used_shape.name in ["raster"]:
                # convert 1D data to 2D (required for QuadMeshes)
                if (
                    len(xorig.shape) == 1
                    and len(yorig.shape) == 1
                    and len(z_data.shape) == 2
                ):

                    xorig, yorig = np.meshgrid(xorig, yorig, copy=False)
                    z_data = z_data.T

            x0, y0 = xorig, yorig

        else:
            transformer = Transformer.from_crs(
                crs1,
                crs2,
                always_xy=True,
            )
            # convert 1D data to 2D to make sure re-projection is correct
            if (
                len(xorig.shape) == 1
                and len(yorig.shape) == 1
                and len(z_data.shape) == 2
            ):
                xorig, yorig = np.meshgrid(xorig, yorig, copy=False)
                z_data = z_data.T

            x0, y0 = transformer.transform(xorig, yorig)

        props["xorig"] = xorig
        props["yorig"] = yorig
        props["ids"] = ids
        props["z_data"] = z_data
        props["x0"] = x0
        props["y0"] = y0

        # convert the data to 1D for shapes that accept unstructured data
        if used_shape.name not in ["shade_raster", "raster"]:
            self._1Dprops(props)

        return props

    def _classify_data(
        self,
        z_data=None,
        cmap=None,
        vmin=None,
        vmax=None,
        classify_specs=None,
    ):

        assert _register_mapclassify(), (
            "EOmaps: Missing dependency: 'mapclassify' \n ... please install"
            + " (conda install -c conda-forge mapclassify) to use data-classifications."
        )

        if z_data is None:
            z_data = self._props["z_data"]

        if isinstance(cmap, str):
            cmap = plt.get_cmap(cmap)

        # evaluate classification
        if classify_specs is not None and classify_specs.scheme is not None:
            classified = True

            if classify_specs.scheme == "UserDefined" and hasattr(
                classify_specs, "bins"
            ):
                classifybins = np.array(classify_specs.bins)
                binmask = (classifybins > np.nanmin(z_data)) & (
                    classifybins < np.nanmax(z_data)
                )
                if np.any(binmask):
                    classifybins = classifybins[binmask]
                    warnings.warn(
                        "EOmaps: classification bins outside of value-range..."
                        + " bins have been updated!"
                    )

                    classify_specs.bins = classifybins

            mapc = getattr(mapclassify, classify_specs.scheme)(
                z_data[~np.isnan(z_data)], **classify_specs
            )
            bins = np.unique([mapc.y.min(), *mapc.bins])
            nbins = len(bins)
            norm = mpl.colors.BoundaryNorm(bins, nbins)
            colors = cmap(np.linspace(0, 1, nbins))

            # initialize the classified colormap
            cbcmap = LinearSegmentedColormap.from_list(
                "cmapname", colors=colors, N=len(colors)
            )
            if cmap._rgba_bad:
                cbcmap.set_bad(cmap._rgba_bad)
            if cmap._rgba_over:
                cbcmap.set_over(cmap._rgba_over)
            if cmap._rgba_under:
                cbcmap.set_under(cmap._rgba_under)

        else:
            classified = False
            bins = None
            cbcmap = cmap
            norm = mpl.colors.Normalize(vmin, vmax)

        return cbcmap, norm, bins, classified

    def _add_colorbar(
        self,
        ax_cb=None,
        ax_cb_plot=None,
        z_data=None,
        label=None,
        bins=None,
        histbins=256,
        cmap="viridis",
        norm=None,
        classified=False,
        vmin=None,
        vmax=None,
        tick_precision=3,
        density=False,
        orientation="vertical",
        log=False,
        tick_formatter=None,
        show_outline=False,
    ):

        if ax_cb is None:
            ax_cb = self.figure.ax_cb
        if ax_cb_plot is None:
            ax_cb_plot = self.figure.ax_cb_plot

        if z_data is None:
            z_data = self._props["z_data"]
        z_data = z_data.ravel()

        if label is None:
            label = self.data_specs["parameter"]

        if tick_formatter is None:
            tick_formatter = partial(
                self._default_cb_tick_formatter, precision=tick_precision
            )

        if orientation == "horizontal":
            cb_orientation = "vertical"

            if log:
                ax_cb_plot.set_xscale("log")

        elif orientation == "vertical":
            cb_orientation = "horizontal"

            if log:
                ax_cb_plot.set_yscale("log")

        # TODO deepcopy is required to avoid issues with datashader?
        norm = copy.deepcopy(norm)
        n_cmap = cm.ScalarMappable(cmap=cmap, norm=norm)
        valid_zdata = z_data[np.isfinite(z_data)]

        # skip drawing the colorbar in case no data is available
        # and show a notification that there's no data instead
        # (relevant for dynamic colorbars if you pan to a region without data)
        if self.data is not None and len(valid_zdata) == 0:
            ax_cb.set_visible(False)
            ax_cb_plot.set_visible(False)
            if ax_cb not in self.BM._hidden_axes:
                self.BM._hidden_axes.add(ax_cb)
            if ax_cb_plot not in self.BM._hidden_axes:
                self.BM._hidden_axes.add(ax_cb_plot)

            if not hasattr(self, "_cb_nodata_txt"):
                axpos = ax_cb_plot.get_position()
                self._cb_nodata_txt = self.ax.text(
                    (axpos.x1 + axpos.x0) / 2,
                    (axpos.y1 + axpos.y0) / 2,
                    "... no dynamic colorbar data ...",
                    transform=self.figure.f.transFigure,
                    horizontalalignment="center",
                    verticalalignment="center",
                    fontsize=8,
                    bbox=dict(
                        facecolor="lightcoral",
                        edgecolor="k",
                        linewidth=0.35,
                        alpha=0.5,
                        boxstyle="round,pad=.35",
                    ),
                )
                self.BM.add_bg_artist(self._cb_nodata_txt, self.layer)

            return
        else:
            # remove the no-data indicator if it is still here
            if hasattr(self, "_cb_nodata_txt"):
                self.BM.remove_bg_artist(self._cb_nodata_txt)
                self._cb_nodata_txt.remove()
                del self._cb_nodata_txt

        n_cmap.set_array(valid_zdata)
        cb = plt.colorbar(
            n_cmap,
            cax=ax_cb,
            label=label,
            extend="neither",
            spacing="proportional",
            orientation=cb_orientation,
        )
        # plot the histogram
        # (only if the axis has a finite size)
        if ax_cb_plot.bbox.width > 0 and ax_cb_plot.bbox.height > 0:
            ax_cb_plot.set_axis_on()
            h = ax_cb_plot.hist(
                z_data.clip(vmin, vmax) if (vmin or vmax) else z_data,
                orientation=orientation,
                bins=bins if (classified and histbins == "bins") else histbins,
                color="k",
                align="mid",
                range=(vmin, vmax) if (vmin and vmax) else None,
                density=density,
            )
            if show_outline:
                if show_outline is True:
                    show_outline = dict(color="k", lw=1)

                if orientation == "vertical":
                    ax_cb_plot.step(h[1], [h[0][0], *h[0]], **show_outline)
                elif orientation == "horizontal":
                    ax_cb_plot.step([h[0][0], *h[0]], h[1], **show_outline)

        else:
            ax_cb_plot.set_axis_off()

        if bins is None:
            # identify position of color-splits in the colorbar
            if isinstance(n_cmap.cmap, LinearSegmentedColormap):
                # for LinearSegmentedcolormap N is the number of quantizations!
                splitpos = np.linspace(vmin, vmax, n_cmap.cmap.N)
            else:
                # for ListedColormap N is the number of colors
                splitpos = np.linspace(vmin, vmax, n_cmap.cmap.N + 1)
        else:
            splitpos = bins

        # color the histogram patches
        for patch in list(ax_cb_plot.patches):
            # the list is important!! since otherwise we change ax.patches
            # as we iterate over it... which is not a good idea...
            if orientation == "horizontal":
                minval = np.atleast_1d(patch.get_y())[0]
                width = patch.get_width()
                height = patch.get_height()
                maxval = minval + height
            elif orientation == "vertical":
                minval = np.atleast_1d(patch.get_x())[0]
                width = patch.get_width()
                height = patch.get_height()
                maxval = minval + width

            # ----------- take care of histogram-bins that have split colors
            # identify bins that extend beyond a color-change
            splitbins = [
                minval,
                *splitpos[(splitpos > minval) & (maxval > splitpos)],
                maxval,
            ]

            if len(splitbins) > 2:
                patch.remove()
                # add in-between patches
                for b0, b1 in pairwise(splitbins):
                    if orientation == "horizontal":
                        pi = mpl.patches.Rectangle(
                            (0, b0),
                            width,
                            (b1 - b0),
                            facecolor=cmap(norm((b0 + b1) / 2)),
                        )
                    elif orientation == "vertical":
                        pi = mpl.patches.Rectangle(
                            (b0, 0),
                            (b1 - b0),
                            height,
                            facecolor=cmap(norm((b0 + b1) / 2)),
                        )

                    ax_cb_plot.add_patch(pi)
            else:
                patch.set_facecolor(cmap(norm((minval + maxval) / 2)))

        # setup appearance of histogram
        if orientation == "horizontal":
            ax_cb_plot.invert_xaxis()

            ax_cb_plot.tick_params(
                left=False,
                labelleft=False,
                bottom=False,
                top=False,
                labelbottom=True,
                labeltop=False,
            )
            ax_cb_plot.grid(axis="x", dashes=[5, 5], c="k", alpha=0.5)
            # add a line that indicates 0 histogram level
            ax_cb_plot.plot(
                [1, 1], [0, 1], "k--", alpha=0.5, transform=ax_cb_plot.transAxes
            )
            # make sure lower x-limit is 0
            if log is False:
                ax_cb_plot.xaxis.set_major_locator(plt.MaxNLocator(5))
                ax_cb_plot.set_xlim(None, 0)

        elif orientation == "vertical":
            ax_cb_plot.tick_params(
                left=False,
                labelleft=True,
                bottom=False,
                top=False,
                labelbottom=False,
                labeltop=False,
            )
            ax_cb_plot.grid(axis="y", dashes=[5, 5], c="k", alpha=0.5)
            # add a line that indicates 0 histogram level
            ax_cb_plot.plot(
                [0, 1], [0, 0], "k--", alpha=0.5, transform=ax_cb_plot.transAxes
            )
            # make sure lower y-limit is 0
            if log is False:
                ax_cb_plot.yaxis.set_major_locator(plt.MaxNLocator(5))
                ax_cb_plot.set_ylim(0)

        cb.outline.set_visible(False)

        # ensure that ticklabels are correct if a classification is used
        if classified:
            cb.set_ticks([i for i in bins if i >= vmin and i <= vmax])

            if orientation == "vertical":
                labelsetfunc = "set_xticklabels"
            elif orientation == "horizontal":
                labelsetfunc = "set_yticklabels"

            getattr(cb.ax, labelsetfunc)(
                [
                    np.format_float_positional(i, precision=tick_precision, trim="-")
                    for i in bins
                    if i >= vmin and i <= vmax
                ]
            )
        else:
            cb.set_ticks(cb.get_ticks())

        if tick_formatter:
            if orientation == "vertical":
                cb.ax.xaxis.set_major_formatter(tick_formatter)
            elif orientation == "horizontal":
                cb.ax.yaxis.set_major_formatter(tick_formatter)

        # format position of scientific exponent for colorbar ticks
        if cb_orientation == "vertical":
            ot = ax_cb.yaxis.get_offset_text()
            ot.set_horizontalalignment("center")
            ot.set_position((1, 0))

        # make sure axis limits are correct
        if orientation == "vertical":
            limsetfunc = ax_cb.set_xlim
        else:
            limsetfunc = ax_cb.set_ylim

        limsetfunc(vmin, vmax)

        return cb

    def _add_cb_extend_arrows(self, cb, orientation, extend_frac=0.025, which="auto"):
        """
        Add a new axis that holds extension-triangles for the colorbar.

        Parameters
        ----------
        cb : matplotilb.colorbar
            the colorbar to use
        orientation : str
            "vertical" or "horizontal"
        extend_frac : float, optional
            the fraction of the axis to use for the extension-triangles.
            (NOTE: triangles will be drawn OUTSIDE the axes!!)
            The default is 0.03.
        which : str
            Indicator which triangles should be drawn
            (one of "auto", "upper", "lower" or "both").
            The default is "auto" in which case only relevant arrows are drawn
            (e.g. "upper" is only drawn if there are values > vmax).
        """

        if which == "auto":
            a = cb.mappable.get_array()
            vmin, vmax = cb.mappable.norm.vmin, cb.mappable.norm.vmax

            if (a > vmax).any():
                which = "upper"
            if (a < vmin).any():
                if which == "upper":
                    which = "both"
                else:
                    which = "lower"

            if which == "auto":
                # (no extension arrows necessary)
                return

        # get the bounding box of the current colorbar axis
        bbox = self.figure.ax_cb.bbox.transformed(self.figure.f.transFigure.inverted())

        if orientation == "horizontal":
            if which == "both":
                which = "left right"
            elif which == "upper":
                which = "right"
            elif which == "lower":
                which = "left"

            frac = extend_frac * (bbox.width)
            axcb2 = self.figure.f.add_axes(
                (bbox.x0 - frac / 2, bbox.y0, bbox.width + frac, bbox.height),
                zorder=-99,
                label="ax_cb_extend",
            )
            axcb2.get_shared_y_axes().join(axcb2, self.figure.ax_cb)
            # set the limits to (0, 1) so we can directly use the fractions
            axcb2.set_xlim(0, 1)

        else:
            if which == "both":
                which = "top bottom"
            elif which == "upper":
                which = "top"
            elif which == "lower":
                which = "bottom"
            frac = extend_frac * (bbox.height)
            axcb2 = self.figure.f.add_axes(
                (bbox.x0, bbox.y0 - frac / 2, bbox.width, bbox.height + frac),
                zorder=-99,
            )
            axcb2.get_shared_x_axes().join(axcb2, self.figure.ax_cb)
            # set the limits to (0, 1) so we can directly use the fractions
            axcb2.set_ylim(0, 1)

        axcb2.set_axis_off()

        # get the coordinates of the colorbar in units of axcb2

        bbox_transf = self.figure.ax_cb.bbox.transformed(axcb2.transAxes.inverted())

        x0, x1, y0, y1 = bbox_transf.x0, bbox_transf.x1, bbox_transf.y0, bbox_transf.y1

        # make sure the arrow overlapps a little bit with the parent cb-axes
        # to avoid gaps between the arrow and the colorbar
        ovx, ovy = bbox_transf.width * 0.1, bbox_transf.height * 0.1

        points = dict(
            left=[[0, 0.5], [x0, 1], [x0 + ovx, 1], [x0 + ovx, 0], [x0, 0], [0, 0.5]],
            right=[[1, 0.5], [x1, 1], [x1 - ovx, 1], [x1 - ovx, 0], [x1, 0], [1, 0.5]],
            top=[[0.5, 1], [0, y1], [0, y1 - ovy], [1, y1 - ovy], [1, y1], [0.5, 1]],
            bottom=[
                [0.5, 0],
                [0, y0],
                [0, y0 + ovy],
                [1, y0 + ovy],
                [1, y0],
                [0.5, ovy],
            ],
        )

        cmap = self.figure.coll.cmap
        colors = dict(
            left=cmap.get_under(),
            right=cmap.get_over(),
            top=cmap.get_over(),
            bottom=cmap.get_under(),
        )

        patches = []
        use_colors = []
        for w in which.split(" "):
            p = points[w]
            Path = mpath.Path
            path_data = [
                (Path.MOVETO, p[0]),
                *[(Path.LINETO, pi) for pi in p[1:-1]],
                (Path.CLOSEPOLY, p[-1]),
            ]
            codes, verts = zip(*path_data)
            path = mpath.Path(verts, codes)
            patches.append(mpatches.PathPatch(path))
            use_colors.append(colors[w])
        collection = PatchCollection(patches, fc=use_colors, ec="none", lw=0)

        axcb2.add_collection(collection)
        return axcb2

    def _update_cb_extend_pos(self):
        if not hasattr(self, "_colorbar"):
            return
        # update the position of the axis holding the colorbar extension arrows
        # TODO the colorbar should be merged into a single artist
        #      to avoid having to update the axes separately!
        [
            layer,
            cbgs,
            ax_cb,
            ax_cb_plot,
            ax_cb_extend,
            extend_frac,
            orientation,
            cb,
        ] = self._colorbar

        if ax_cb_extend is None:
            return

        bbox = ax_cb.bbox.transformed(self.figure.f.transFigure.inverted())
        if orientation == "horizontal":
            frac = extend_frac * (bbox.width)
            ax_cb_extend.set_position(
                (bbox.x0 - frac / 2, bbox.y0, bbox.width + frac, bbox.height),
            )
        elif orientation == "vertical":
            frac = extend_frac * (bbox.height)
            ax_cb_extend.set_position(
                (bbox.x0, bbox.y0 - frac / 2, bbox.width, bbox.height + frac),
            )
        else:
            raise TypeError(f"'{orientation}' is not a valid colorbar orientation!")

    @property
    @wraps(NaturalEarth_features)
    def add_feature(self):
        return NaturalEarth_features(weakref.proxy(self))

    def _clip_gdf(self, gdf, how="crs"):
        """
        Clip the shapes of a GeoDataFrame with respect to the boundaries
        of the crs (or the plot-extent).

        Parameters
        ----------
        gdf : geopandas.GeoDataFrame
            The GeoDataFrame containing the geometries.
        how : str, optional
            Identifier how the clipping should be performed.

            If a suffix "_invert" is added to the string, the polygon will be
            inverted (via a symmetric-difference to the clip-shape)

            - clipping with geopandas:
              - "crs" : use the actual crs boundary polygon
              - "crs_bounds" : use the boundary-envelope of the crs
              - "extent" : use the current plot-extent

            - clipping with gdal (always uses the crs domain as clip-shape):
              - "gdal_Intersection"
              - "gdal_SymDifference"
              - "gdal_Difference"
              - "gdal_Union"

            The default is "crs".

        Returns
        -------
        gdf
            A GeoDataFrame with the clipped geometries
        """
        assert _register_geopandas(), (
            "EOmaps: Missing dependency `geopandas`!\n"
            + "please install '(conda install -c conda-forge geopandas)'"
            + "to use `m.add_gdf()`."
        )

        if how.startswith("gdal"):
            methods = ["SymDifference", "Intersection", "Difference", "Union"]
            # "SymDifference", "Intersection", "Difference"
            method = how.split("_")[1]
            assert method in methods, "EOmaps: '{how}' is not a valid clip-method"
            try:
                from osgeo import gdal
                from shapely import wkt
            except ImportError:
                raise ImportError(
                    "EOmaps: Missing dependency: 'osgeo'\n"
                    + "...clipping with gdal requires 'osgeo.gdal'"
                )

            e = self.ax.projection.domain
            e2 = gdal.ogr.CreateGeometryFromWkt(e.wkt)
            if not e2.IsValid():
                e2 = e2.MakeValid()

            gdf = gdf.to_crs(self.crs_plot)
            clipgeoms = []
            for g in gdf.geometry:
                g2 = gdal.ogr.CreateGeometryFromWkt(g.wkt)

                if g2 is None:
                    continue

                if not g2.IsValid():
                    g2 = g2.MakeValid()

                i = getattr(g2, method)(e2)

                if how.endswith("_invert"):
                    i = i.SymDifference(e2)

                gclip = wkt.loads(i.ExportToWkt())
                clipgeoms.append(gclip)

            gdf = gpd.GeoDataFrame(geometry=clipgeoms, crs=self.crs_plot)

            return gdf

        if how == "crs" or how == "crs_invert":
            clip_shp = gpd.GeoDataFrame(
                geometry=[self.ax.projection.domain], crs=self.crs_plot
            ).to_crs(gdf.crs)
        elif how == "extent" or how == "extent_invert":
            self.BM.update()
            x0, x1, y0, y1 = self.ax.get_extent()
            clip_shp = self._make_rect_poly(x0, y0, x1, y1, self.crs_plot).to_crs(
                gdf.crs
            )
        elif how == "crs_bounds" or how == "crs_bounds_invert":
            x0, x1, y0, y1 = self.ax.get_extent()
            clip_shp = self._make_rect_poly(
                *self.crs_plot.boundary.bounds, self.crs_plot
            ).to_crs(gdf.crs)
        else:
            raise TypeError(f"EOmaps: '{how}' is not a valid clipping method")

        clip_shp = clip_shp.buffer(0)  # use this to make sure the geometry is valid

        # add 1% of the extent-diameter as buffer
        bnd = clip_shp.boundary.bounds
        d = np.sqrt((bnd.maxx - bnd.minx) ** 2 + (bnd.maxy - bnd.miny) ** 2)
        clip_shp = clip_shp.buffer(d / 100)

        # clip the geo-dataframe with the buffered clipping shape
        clipgdf = gdf.clip(clip_shp)

        if how.endswith("_invert"):
            clipgdf = clipgdf.symmetric_difference(clip_shp)

        return clipgdf

    def add_gdf(
        self,
        gdf,
        picker_name=None,
        pick_method="contains",
        val_key=None,
        layer=None,
        temporary_picker=None,
        clip=False,
        reproject="gpd",
        verbose=False,
        **kwargs,
    ):
        """
        Plot a `geopandas.GeoDataFrame` on the map.

        Parameters
        ----------
        gdf : geopandas.GeoDataFrame, str or pathlib.Path
            A GeoDataFrame that should be added to the plot.

            If a string (or pathlib.Path) is provided, it is identified as the path to
            a file that should be read with `geopandas.read_file(gdf)`.

        picker_name : str or None
            A unique name that is used to identify the pick-method.

            If a `picker_name` is provided, a new pick-container will be
            created that can be used to pick geometries of the GeoDataFrame.

            The container can then be accessed via:
            >>> m.cb.pick__<picker_name>
            or
            >>> m.cb.pick[picker_name]
            and it can be used in the same way as `m.cb.pick...`

        pick_method : str or callable
            if str :
                The operation that is executed on the GeoDataFrame to identify
                the picked geometry.
                Possible values are:

                - "contains":
                  pick a geometry only if it contains the clicked point
                  (only works with polygons! (not with lines and points))
                - "centroids":
                  pick the closest geometry with respect to the centroids
                  (should work with any geometry whose centroid is defined)

                The default is "centroids"

            if callable :
                A callable that is used to identify the picked geometry.
                The call-signature is:

                >>> def picker(artist, mouseevent):
                >>>     # if the pick is NOT successful:
                >>>     return False, dict()
                >>>     ...
                >>>     # if the pick is successful:
                >>>     return True, dict(ID, pos, val, ind)

                The default is "contains"

        val_key : str
            The dataframe-column used to identify values for pick-callbacks.
            The default is None.
        layer : int, str or None
            The name of the layer at which the dataset will be plotted.

            - If "all": the corresponding feature will be added to ALL layers
            - If None, the layer assigned to the Maps-object is used (e.g. `m.layer`)

            The default is None.
        temporary_picker : str, optional
            The name of the picker that should be used to make the geometry
            temporary (e.g. remove it after each pick-event)
        clip : str or False
            This feature can help with re-projection issues for non-global crs.
            (see example below)

            Indicator if geometries should be clipped prior to plotting or not.

            - if "crs": clip with respect to the boundary-shape of the crs
            - if "crs_bounds" : clip with respect to a rectangular crs boundary
            - if "extent": clip with respect to the current extent of the plot-axis.
            - if the 'gdal' python-bindings are installed, you can use gdal to clip
              the shapes with respect to the crs-boundary. (slower but more robust)
              The following logical operations are supported:

              - "gdal_SymDifference" : symmetric difference
              - "gdal_Intersection" : intersection
              - "gdal_Difference" : difference
              - "gdal_Union" : union

            If a suffix "_invert" is added to the clip-string (e.g. "crs_invert"
            or "gdal_Intersection_invert") the obtained (clipped) polygons will be
            inverted.


            >>> mg = MapsGrid(2, 3, crs=3035)
            >>> mg.m_0_0.add_feature.preset.ocean(use_gpd=True)
            >>> mg.m_0_1.add_feature.preset.ocean(use_gpd=True, clip="crs")
            >>> mg.m_0_2.add_feature.preset.ocean(use_gpd=True, clip="extent")
            >>> mg.m_1_0.add_feature.preset.ocean(use_gpd=False)
            >>> mg.m_1_1.add_feature.preset.ocean(use_gpd=False, clip="crs")
            >>> mg.m_1_2.add_feature.preset.ocean(use_gpd=False, clip="extent")

        reproject : str, optional
            Similar to "clip" this feature mainly addresses issues in the way how
            re-projected geometries are displayed in certain coordinate-systems.
            (see example below)

            - if "gpd": geopandas is used to re-project the geometries
            - if "cartopy": cartopy is used to re-project the geometries
              (slower but generally more robust than "gpd")

            >>> mg = MapsGrid(2, 1, crs=Maps.CRS.Stereographic())
            >>> mg.m_0_0.add_feature.preset.ocean(reproject="gpd")
            >>> mg.m_1_0.add_feature.preset.ocean(reproject="cartopy")

            The default is "gpd"
        verbose : bool, optional
            Indicator if a progressbar should be printed when re-projecting
            geometries with "use_gpd=False".
            The default is False.
        kwargs :
            all remaining kwargs are passed to `geopandas.GeoDataFrame.plot(**kwargs)`

        Returns
        -------
        new_artists : matplotlib.Artist
            The matplotlib-artists added to the plot

        """
        assert pick_method in ["centroids", "contains"], (
            f"EOmaps: '{pick_method}' is not a valid GeoDataFrame pick-method! "
            + "... use one of ['contains', 'centroids']"
        )

        assert _register_geopandas(), (
            "EOmaps: Missing dependency `geopandas`!\n"
            + "please install '(conda install -c conda-forge geopandas)'"
            + "to use `m.add_gdf()`."
        )

        if isinstance(gdf, (str, Path)):
            gdf = gpd.read_file(gdf)

        try:
            # explode the GeoDataFrame to avoid picking multi-part geometries
            gdf = gdf[gdf.is_valid].explode(index_parts=False)
        except Exception:
            # geopandas sometimes has problems exploding geometries...
            # if it does not work, just continue with the Multi-geometries!
            print("EOmaps: Exploding geometries did not work!")
            pass

        if clip:
            gdf = self._clip_gdf(gdf, clip)
        if reproject == "gpd":
            gdf = gdf.to_crs(self.crs_plot)
        elif reproject == "cartopy":
            # optionally use cartopy's re-projection routines to re-project
            # geometries

            cartopy_crs = self._get_cartopy_crs(gdf.crs)
            if self.ax.projection != cartopy_crs:
                # TODO this results in problems and sometimes masks way too much!!
                # select only polygons that actually intersect with the CRS-boundary
                # mask = gdf.buffer(1).intersects(
                #     gpd.GeoDataFrame(
                #         geometry=[self.ax.projection.domain], crs=self.ax.projection
                #     )
                #     .to_crs(gdf.crs)
                #     .geometry[0]
                # )
                # gdf = gdf.copy()[mask]

                geoms = gdf.geometry
                if len(geoms) > 0:
                    proj_geoms = []

                    if verbose:
                        for g in progressbar(geoms, "EOmaps: re-projecting... ", 20):
                            proj_geoms.append(
                                self.ax.projection.project_geometry(g, cartopy_crs)
                            )
                    else:
                        for g in geoms:
                            proj_geoms.append(
                                self.ax.projection.project_geometry(g, cartopy_crs)
                            )

                    gdf.geometry = proj_geoms
                    gdf.set_crs(self.ax.projection, allow_override=True)
                gdf = gdf[~gdf.is_empty]
        else:
            raise AssertionError(
                f"EOmaps: '{reproject}' is not a valid reproject-argument."
            )
        # plot gdf and identify newly added collections
        # (geopandas always uses collections)
        colls = [id(i) for i in self.ax.collections]
        artists, prefixes = [], []
        for geomtype, geoms in gdf.groupby(gdf.geom_type):
            gdf.plot(ax=self.ax, aspect=self.ax.get_aspect(), **kwargs)
            artists = [i for i in self.ax.collections if id(i) not in colls]
            for i in artists:
                prefixes.append(f"_{i.__class__.__name__.replace('Collection', '')}")

        if picker_name is not None:
            if pick_method is not None:
                if isinstance(pick_method, str):
                    if pick_method == "contains":

                        def picker(artist, mouseevent):
                            try:
                                query = getattr(gdf, pick_method)(
                                    gpd.points_from_xy(
                                        [mouseevent.xdata], [mouseevent.ydata]
                                    )[0]
                                )
                                if query.any():
                                    return True, dict(
                                        ID=gdf.index[query][0],
                                        ind=query.values.nonzero()[0][0],
                                        val=(
                                            gdf[query][val_key].iloc[0]
                                            if val_key
                                            else None
                                        ),
                                    )
                                else:
                                    return False, dict()
                            except:
                                return False, dict()

                    elif pick_method == "centroids":
                        tree = cKDTree(
                            list(map(lambda x: (x.x, x.y), gdf.geometry.centroid))
                        )

                        def picker(artist, mouseevent):
                            try:
                                dist, ind = tree.query(
                                    (mouseevent.xdata, mouseevent.ydata), 1
                                )

                                ID = gdf.index[ind]
                                val = gdf.iloc[ind][val_key] if val_key else None
                                pos = tree.data[ind].tolist()
                            except:
                                return False, dict()

                            return True, dict(ID=ID, pos=pos, val=val, ind=ind)

                elif callable(pick_method):
                    picker = pick_method
                else:
                    print(
                        "EOmaps: I don't know what to do with the provided pick_method"
                    )

                if len(artists) > 1:
                    warnings.warn(
                        "EOmaps: Multiple geometry types encountered in `m.add_gdf`. "
                        + "The pick containers are re-named to"
                        + f"{[picker_name + prefix for prefix in prefixes]}"
                    )
                else:
                    prefixes = [""]

                for artist, prefix in zip(artists, prefixes):
                    # make the newly added collection pickable
                    self.cb.add_picker(picker_name + prefix, artist, picker=picker)

                    # attach the re-projected GeoDataFrame to the pick-container
                    self.cb.pick[picker_name + prefix].data = gdf

        if layer is None:
            layer = self.layer

        if temporary_picker is not None:
            if temporary_picker == "default":
                for art, prefix in zip(artists, prefixes):
                    self.cb.pick.add_temporary_artist(art)
            else:
                for art, prefix in zip(artists, prefixes):
                    self.cb.pick[temporary_picker].add_temporary_artist(art)
        else:
            for art, prefix in zip(artists, prefixes):
                self.BM.add_bg_artist(art, layer)
        return artists

    def add_marker(
        self,
        ID=None,
        xy=None,
        xy_crs=None,
        radius=None,
        shape="ellipses",
        buffer=1,
        n=100,
        layer=None,
        **kwargs,
    ):
        """
        add a marker to the plot

        Parameters
        ----------
        ID : any
            The index-value of the pixel in m.data.
        xy : tuple
            A tuple of the position of the pixel provided in "xy_crs".
            If None, xy must be provided in the coordinate-system of the plot!
            The default is None
        xy_crs : any
            the identifier of the coordinate-system for the xy-coordinates
        radius : float or "pixel", optional
            - If float: The radius of the marker.
            - If "pixel": It will represent the dimensions of the selected pixel.
              (check the `buffer` kwarg!)

            The default is None in which case "pixel" is used if a dataset is
            present and otherwise a shape with 1/10 of the axis-size is plotted
        radius_crs : str or a crs-specification
            The crs specification in which the radius is provided.
            Either "in", "out", or a crs specification (e.g. an epsg-code,
            a PROJ or wkt string ...)
            The default is "in" (e.g. the crs specified via `m.data_specs.crs`).
            (only relevant if radius is NOT specified as "pixel")
        shape : str, optional
            Indicator which shape to draw. Currently supported shapes are:
            - geod_circles
            - ellipses
            - rectangles

            The default is "circle".
        buffer : float, optional
            A factor to scale the size of the shape. The default is 1.
        n : int
            The number of points to calculate for the shape.
            The default is 100.
        layer : str, int or None
            The name of the layer at which the marker should be drawn.
            If None, the layer associated with the used Maps-object (e.g. m.layer)
            is used. The default is None.
        kwargs :
            kwargs passed to the matplotlib patch.
            (e.g. `zorder`, `facecolor`, `edgecolor`, `linewidth`, `alpha` etc.)

        Examples
        --------

            >>> m.add_marker(ID=1, buffer=5)
            >>> m.add_marker(ID=1, radius=2, radius_crs=4326, shape="rectangles")
            >>> m.add_marker(xy=(45, 35), xy_crs=4326, radius=20000, shape="geod_circles")
        """

        if ID is not None:
            assert xy is None, "You can only provide 'ID' or 'pos' not both!"
        else:
            if isinstance(radius, str) and radius != "pixel":
                raise TypeError(f"I don't know what to do with radius='{radius}'")

        if xy is not None:
            ID = None
            if xy_crs is not None:
                # get coordinate transformation
                transformer = Transformer.from_crs(
                    self.get_crs(xy_crs),
                    self.crs_plot,
                    always_xy=True,
                )
                # transform coordinates
                xy = transformer.transform(*xy)

        kwargs.setdefault("permanent", True)

        # add marker
        marker = self.cb.click._cb.mark(
            ID=ID,
            pos=xy,
            radius=radius,
            ind=None,
            shape=shape,
            buffer=buffer,
            n=n,
            layer=layer,
            **kwargs,
        )

        try:
            # this will fail if no initial draw was performed!
            self.BM._draw_animated(artists=[marker])
        except Exception:
            self.BM.update()

        return marker

    def add_annotation(
        self,
        ID=None,
        xy=None,
        xy_crs=None,
        text=None,
        **kwargs,
    ):
        """
        add an annotation to the plot

        Parameters
        ----------
        ID : str, int, float or array-like
            The index-value of the pixel in m.data.
        xy : tuple of float or array-like
            A tuple of the position of the pixel provided in "xy_crs".
            If None, xy must be provided in the coordinate-system of the plot!
            The default is None.
        xy_crs : any
            the identifier of the coordinate-system for the xy-coordinates
        text : callable or str, optional
            if str: the string to print
            if callable: A function that returns the string that should be
            printed in the annotation with the following call-signature:

                >>> def text(m, ID, val, pos, ind):
                >>>     # m   ... the Maps object
                >>>     # ID  ... the ID
                >>>     # pos ... the position
                >>>     # val ... the value
                >>>     # ind ... the index of the clicked pixel
                >>>
                >>>     return "the string to print"

            The default is None.

        **kwargs
            kwargs passed to m.cb.annotate

        Examples
        --------

        >>> m.add_annotation(ID=1)
        >>> m.add_annotation(xy=(45, 35), xy_crs=4326)

        NOTE: You can provide lists to add multiple annotations in one go!

        >>> m.add_annotation(ID=[1, 5, 10, 20])
        >>> m.add_annotation(xy=([23.5, 45.8, 23.7], [5, 6, 7]), xy_crs=4326)

        The text can be customized by providing either a string

        >>> m.add_annotation(ID=1, text="some text")

        or a callable that returns a string with the following signature:

        >>> def addtxt(m, ID, val, pos, ind):
        >>>     return f"The ID {ID} at position {pos} has a value of {val}"
        >>> m.add_annotation(ID=1, text=addtxt)

        **Customizing the appearance**

        For the full set of possibilities, see:
        https://matplotlib.org/stable/tutorials/text/annotations.html

        >>> m.add_annotation(xy=[7.10, 45.16], xy_crs=4326,
        >>>                  text="blubb", xytext=(30,30),
        >>>                  horizontalalignment="center", verticalalignment="center",
        >>>                  arrowprops=dict(ec="g",
        >>>                                  arrowstyle='-[',
        >>>                                  connectionstyle="angle",
        >>>                                  ),
        >>>                  bbox=dict(boxstyle='circle,pad=0.5',
        >>>                            fc='yellow',
        >>>                            alpha=0.3
        >>>                            )
        >>>                  )

        """

        if ID is not None:
            assert xy is None, "You can only provide 'ID' or 'pos' not both!"
            mask = np.isin(self._props["ids"], ID)
            xy = (self._props["xorig"][mask], self._props["yorig"][mask])
            val = self._props["z_data"][mask]
            ind = np.where(mask)[0]
            ID = np.atleast_1d(ID)
            xy_crs = self.data_specs.crs
        else:
            val = repeat(None)
            ind = repeat(None)
            ID = repeat(None)

        assert (
            xy is not None
        ), "EOmaps: you must provide either ID or xy to position the annotation!"

        xy = (np.atleast_1d(xy[0]), np.atleast_1d(xy[1]))

        if xy_crs is not None:
            # get coordinate transformation
            transformer = Transformer.from_crs(
                CRS.from_user_input(xy_crs),
                self.crs_plot,
                always_xy=True,
            )
            # transform coordinates
            xy = transformer.transform(*xy)

        kwargs.setdefault("permanent", True)

        if isinstance(text, str) or callable(text):
            text = repeat(text)
        else:
            try:
                iter(text)
            except TypeError:
                text = repeat(text)

        for x, y, texti, vali, indi, IDi in zip(xy[0], xy[1], text, val, ind, ID):

            # add marker
            self.cb.click._cb.annotate(
                ID=IDi,
                pos=(x, y),
                val=vali,
                ind=indi,
                text=texti,
                **kwargs,
            )
        self.BM.update(clear=False)

    def add_compass(
        self, pos=None, scale=10, style="compass", patch=None, txt="N", pickable=True
    ):
        """
        Add a "compass" or "north-arrow" to the map.

        Note
        ----
        You can use the mouse to pick the compass and move it anywhere on the map.
        (the directions are dynamically updated if you pan/zoom or pick the compass)

        - If you press the "delete" key while clicking on the compass, it is removed.
          (same as calling `compass.remove()`)
        - If you press the "d" key while clicking on the compass, it will be
          disconnected from pick-events (same as calling `compass.set_pickable(False)`)


        Parameters
        ----------
        pos : tuple or None, optional
            The relative position of the compass with respect to the axis.
            (0,0) - lower left corner, (1,1) - upper right corner
            Note that you can also move the compass with the mouse!
        scale : float, optional
            A scale-factor for the size of the compass. The default is 10.
        style : str, optional

            - "north arrow" : draw only a north-arrow
            - "compass": draw a compass with arrows in all 4 directions

            The default is "compass".
        patch : False, str or tuple, optional
            The color of the background-patch.
            (can be any color specification supported by matplotlib)
            The default is "w".
        txt : str, optional
            Indicator which directions should be indicated.
            - "NESW" : add letters for all 4 directions
            - "NE" : add only letters for North and East (same for other combinations)
            - None : don't add any letters
            The default is "N".
        pickable : bool, optional
            Indicator if the compass should be static (False) or if it can be dragged
            with the mouse (True). The default is True

        Returns
        -------
        compass : eomaps.Compass
            A compass-object that can be used to manually adjust the style and position
            of the compass or remove it from the map.

        """

        c = Compass(weakref.proxy(self))
        c(pos=pos, scale=scale, style=style, patch=patch, txt=txt, pickable=pickable)
        # store a reference to the object (required for callbacks)!
        self._compass.add(c)
        return c

    @wraps(ScaleBar.__init__)
    def add_scalebar(
        self,
        lon=None,
        lat=None,
        azim=0,
        preset=None,
        scale=None,
        autoscale_fraction=0.25,
        auto_position=(0.75, 0.25),
        scale_props=None,
        patch_props=None,
        label_props=None,
    ):

        s = ScaleBar(
            m=self,
            preset=preset,
            scale=scale,
            autoscale_fraction=autoscale_fraction,
            auto_position=auto_position,
            scale_props=scale_props,
            patch_props=patch_props,
            label_props=label_props,
        )

        if lon is None or lat is None:
            s._auto_position = auto_position
            lon, lat = s._get_autopos(auto_position)
        else:
            # don't auto-reposition if lon/lat has been provided
            s._auto_position = None

        s._add_scalebar(lon, lat, azim)
        s._make_pickable()

        return s

    if wms_container is not None:

        @property
        @wraps(wms_container)
        def add_wms(self):
            return self._wms_container

    def add_line(
        self,
        xy,
        xy_crs=4326,
        connect="geod",
        n=None,
        del_s=None,
        mark_points=None,
        layer=None,
        **kwargs,
    ):
        """
        Draw a line by connecting a set of anchor-points.

        The points can be connected with either "geodesic-lines", "straight lines" or
        "projected straight lines with respect to a given crs" (see `connect` kwarg).

        Parameters
        ----------
        xy : list, set or numpy.ndarray
            The coordinates of the anchor-points that define the line.
            Expected shape:  [(x0, y0), (x1, y1), ...]
        xy_crs : any, optional
            The crs of the anchor-point coordinates.
            (can be any crs definition supported by PyProj)
            The default is 4326 (e.g. lon/lat).
        connect : str, optional
            The connection-method used to draw the segments between the anchor-points.

            - "geod": Connect the anchor-points with geodesic lines
            - "straight": Connect the anchor-points with straight lines
            - "straight_crs": Connect the anchor-points with straight lines in the
              `xy_crs` projection and reproject those lines to the plot-crs.

            The default is "geod".
        n : int, list or None optional
            The number of intermediate points to use for each line-segment.

            - If an integer is provided, each segment is equally divided into n parts.
            - If a list is provided, it is used to specify "n" for each line-segment
              individually.

              (NOTE: The number of segments is 1 less than the number of anchor-points!)

            If both n and del_s is None, n=100 is used by default!

            The default is None.
        del_s : int, float or None, optional
            Only relevant if `connect="geod"`!

            The target-distance in meters between the subdivisions of the line-segments.

            - If a number is provided, each segment is equally divided.
            - If a list is provided, it is used to specify "del_s" for each line-segment
              individually.

              (NOTE: The number of segments is 1 less than the number of anchor-points!)

            The default is None.
        mark_points : str, dict or None, optional
            Set the marker-style for the anchor-points.

            - If a string is provided, it is identified as a matploltib "format-string",
              e.g. "r." for red dots, "gx" for green x markers etc.
            - if a dict is provided, it will be used to set the style of the markers
              e.g.: dict(marker="o", facecolor="orange", edgecolor="g")

            See https://matplotlib.org/stable/gallery/lines_bars_and_markers/marker_reference.html
            for more details

            The default is "o"

        layer : str, int or None
            The name of the layer at which the line should be drawn.
            If None, the layer associated with the used Maps-object (e.g. m.layer)
            is used. Use "all" to add the line to all layers!
            The default is None.
        kwargs :
            additional keyword-arguments passed to plt.plot(), e.g.
            "c" (or "color"), "lw" (or "linewidth"), "ls" (or "linestyle"),
            "markevery", etc.

            See https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html
            for more details.

        Returns
        -------
        out_d_int : list
            Only relevant for `connect="geod"`! (An empty ist is returned otherwise.)
            A list of the subdivision distances of the line-segments (in meters).
        out_d_tot : list
            Only relevant for `connect="geod"` (An empty ist is returned otherwise.)
            A list of total distances of the line-segments (in meters).

        """

        if layer is None:
            layer = self.layer

        # intermediate and total distances
        out_d_int, out_d_tot = [], []

        if len(xy) <= 1:
            print("you must provide at least 2 points")

        if n is not None:
            assert del_s is None, "EOmaps: Provide either `del_s` or `n`, not both!"
            del_s = 0  # pyproj's geod uses 0 as identifier!

            if not isinstance(n, int):
                assert len(n) == len(xy) - 1, (
                    "EOmaps: The number of subdivisions per line segment (n) must be"
                    + " 1 less than the number of points!"
                )

        elif del_s is not None:
            assert n is None, "EOmaps: Provide either `del_s` or `n`, not both!"
            n = 0  # pyproj's geod uses 0 as identifier!

            assert connect in ["geod"], (
                "EOmaps: Setting a fixed subdivision-distance (e.g. `del_s`) is only "
                + "possible for `geod` lines! Use `n` instead!"
            )

            if not isinstance(del_s, (int, float, np.number)):
                assert len(del_s) == len(xy) - 1, (
                    "EOmaps: The number of subdivision-distances per line segment "
                    + "(`del_s`) must be 1 less than the number of points!"
                )
        else:
            # use 100 subdivisions by default
            n = 100
            del_s = 0

        t_xy_plot = Transformer.from_crs(
            self.get_crs(xy_crs), self.crs_plot, always_xy=True
        )
        xplot, yplot = t_xy_plot.transform(*zip(*xy))

        if connect == "geod":
            # connect points via geodesic lines
            if xy_crs != 4326:
                t = Transformer.from_crs(
                    self.get_crs(xy_crs), self.get_crs(4326), always_xy=True
                )
                x, y = t.transform(*zip(*xy))
            else:
                x, y = zip(*xy)

            geod = self.crs_plot.get_geod()

            if n is None or isinstance(n, int):
                n = repeat(n)

            if del_s is None or isinstance(del_s, (int, float, np.number)):
                del_s = repeat(del_s)

            xs, ys = [], []
            for (x0, x1), (y0, y1), ni, di in zip(pairwise(x), pairwise(y), n, del_s):

                npts, d_int, d_tot, lon, lat, _ = geod.inv_intermediate(
                    x0, y0, x1, y1, del_s=di, npts=ni, initial_idx=0, terminus_idx=0
                )

                out_d_int.append(d_int)
                out_d_tot.append(d_tot)

                lon, lat = lon.tolist(), lat.tolist()
                xi, yi = self._transf_lonlat_to_plot.transform(lon, lat)
                xs += xi
                ys += yi
            (art,) = self.ax.plot(xs, ys, **kwargs)

        elif connect == "straight":
            (art,) = self.ax.plot(xplot, yplot, **kwargs)

        elif connect == "straight_crs":
            # draw a straight line that is defined in a given crs

            x, y = zip(*xy)
            if isinstance(n, int):
                # use same number of points for all segments
                xs = np.linspace(x[:-1], x[1:], n).T.ravel()
                ys = np.linspace(y[:-1], y[1:], n).T.ravel()
            else:
                # use different number of points for individual segments
                from itertools import chain

                xs = list(
                    chain(
                        *(np.linspace(a, b, ni) for (a, b), ni in zip(pairwise(x), n))
                    )
                )
                ys = list(
                    chain(
                        *(np.linspace(a, b, ni) for (a, b), ni in zip(pairwise(y), n))
                    )
                )

            x, y = t_xy_plot.transform(xs, ys)

            (art,) = self.ax.plot(x, y, **kwargs)
        else:
            raise TypeError(f"EOmaps: '{connect}' is not a valid connection-method!")

        self.BM.add_bg_artist(art, layer)

        if mark_points:
            zorder = kwargs.get("zorder", 10)

            if isinstance(mark_points, dict):
                # only use zorder of the line if no explicit zorder is provided
                mark_points["zorder"] = mark_points.get("zorder", zorder)

                art2 = self.ax.scatter(xplot, yplot, **mark_points)

            elif isinstance(mark_points, str):
                # use matplotlib's single-string style identifiers,
                # (e.g. "r.", "go", "C0x" etc.)
                (art2,) = self.ax.plot(xplot, yplot, mark_points, zorder=zorder, lw=0)

            self.BM.add_bg_artist(art2, layer)

        return out_d_int, out_d_tot

    @wraps(plt.savefig)
    def savefig(self, *args, **kwargs):
        # clear all cached background layers before saving to make sure they
        # are re-drawn with the correct dpi-settings
        self.BM._bg_layers = dict()
        self.figure.f.savefig(*args, **kwargs)
        # redraw after the save to ensure that backgrounds are correctly cached
        self.redraw()

    def _shade_map(
        self,
        pick_distance=100,
        verbose=0,
        layer=None,
        dynamic=False,
        set_extent=True,
        assume_sorted=True,
        **kwargs,
    ):
        """
        Plot the dataset using the (very fast) "datashader" library.
        (requires `datashader`... use `conda install -c conda-forge datashader`)

        - This method is intended for extremely large datasets
          (up to millions of datapoints)!

        A dynamically updated "shaded" map will be generated.
        Note that the datapoints in this case are NOT represented by the shapes
        defined as `m.set_shape`!

        - By default, the shading is performed using a "mean"-value aggregation hook

        kwargs :
            kwargs passed to `datashader.mpl_ext.dsshow`

        """
        assert _register_datashader(), (
            "EOmaps: Missing dependency: 'datashader' \n ... please install"
            + " (conda install -c conda-forge datashader) to use the plot-shapes "
            + "'shade_points' and 'shade_raster'"
        )

        cmap = kwargs.pop("cmap", "viridis")
        vmin = kwargs.pop("vmin", None)
        vmax = kwargs.pop("vmin", None)

        # remove previously fetched backgrounds for the used layer
        if layer in self.BM._bg_layers and dynamic is False:
            del self.BM._bg_layers[layer]
            # self.BM._refetch_bg = True

        if verbose:
            print("EOmaps: Preparing the data")
        # ---------------------- prepare the data
        props = self._prepare_data(assume_sorted=assume_sorted)
        if len(props["z_data"]) == 0:
            print("EOmaps: there was no data to plot")
            return

        # remember props for later use
        self._props = props

        z_finite = np.isfinite(props["z_data"])

        # get the name of the used aggretation reduction
        aggname = self.shape.aggregator.__class__.__name__
        if aggname in ["first", "last", "max", "min", "mean", "mode"]:
            # set vmin/vmax in case the aggregation still represents data-values
            if vmin is None:
                vmin = np.min(props["z_data"][z_finite])
            if vmax is None:
                vmax = np.max(props["z_data"][z_finite])
        else:
            # set vmin/vmax for aggregations that do NOT represent data values

            # allow vmin/vmax = None (e.g. autoscaling)
            if "count" in aggname:
                # if the reduction represents a count, don't count empty pixels
                if vmin and vmin <= 0:
                    print("EOmaps: setting vmin=1 to avoid counting empty pixels...")
                    vmin = 1

        if verbose:
            print("EOmaps: Classifying...")

        # ---------------------- classify the data
        cbcmap, norm, bins, classified = self._classify_data(
            vmin=vmin,
            vmax=vmax,
            cmap=cmap,
            classify_specs=self.classify_specs,
        )

        self.classify_specs._cbcmap = cbcmap
        self.classify_specs._norm = norm
        self.classify_specs._bins = bins
        self.classify_specs._classified = classified

        # in case the aggregation does not represent data-values
        # (e.g. count, std, var ... ) use an automatic "linear" normalization
        if aggname in ["first", "last", "max", "min", "mean", "mode"]:
            kwargs.setdefault("norm", self.classify_specs._norm)
            kwargs.setdefault("vmin", vmin)
            kwargs.setdefault("vmax", vmax)

            # clip the data to properly account for vmin and vmax
            # (do this only if we don't intend to use the full dataset!)
            # if vmin or vmax:
            #     props["z_data"] = props["z_data"].clip(vmin, vmax)
        else:
            kwargs.setdefault("norm", "linear")
            kwargs.setdefault("vmin", vmin)
            kwargs.setdefault("vmax", vmax)

        if verbose:
            print("EOmaps: Plotting...")

        zdata = props["z_data"]
        if len(zdata) == 0:
            print("EOmaps: there was no data to plot")
            return

        plot_width, plot_height = int(self.ax.bbox.width), int(self.ax.bbox.height)

        # get rid of unnecessary dimensions in the numpy arrays
        zdata = zdata.squeeze()
        props["x0"] = props["x0"].squeeze()
        props["y0"] = props["y0"].squeeze()

        # the shape is always set after _prepare data!
        if self.shape.name == "shade_raster":
            assert (
                _register_xarray()
            ), "EOmaps: missing dependency `xarray` for 'shade_raster'"
            if len(zdata.shape) == 2:
                if (zdata.shape == props["x0"].shape) and (
                    zdata.shape == props["y0"].shape
                ):
                    # use a curvilinear QuadMesh
                    self.shape.glyph = ds.glyphs.QuadMeshCurvilinear("x", "y", "val")
                    # 2D coordinates and 2D raster

                    df = xar.Dataset(
                        data_vars=dict(val=(["xx", "yy"], zdata)),
                        # dims=["x", "y"],
                        coords=dict(
                            x=(["xx", "yy"], props["x0"]), y=(["xx", "yy"], props["y0"])
                        ),
                    )

                elif (
                    ((zdata.shape[1],) == props["x0"].shape)
                    and ((zdata.shape[0],) == props["y0"].shape)
                    and (props["x0"].shape != props["y0"].shape)
                ):
                    raise AssertionError(
                        "EOmaps: it seems like you need to transpose your data! \n"
                        + f"the dataset has a shape of {zdata.shape}, but the "
                        + f"coordinates suggest ({props['x0'].shape}, {props['x0'].shape})"
                    )
                elif (zdata.T.shape == props["x0"].shape) and (
                    zdata.T.shape == props["y0"].shape
                ):
                    raise AssertionError(
                        "EOmaps: it seems like you need to transpose your data! \n"
                        + f"the dataset has a shape of {zdata.shape}, but the "
                        + f"coordinates suggest {props['x0'].shape}"
                    )

                elif ((zdata.shape[0],) == props["x0"].shape) and (
                    (zdata.shape[1],) == props["y0"].shape
                ):
                    # use a rectangular QuadMesh
                    self.shape.glyph = ds.glyphs.QuadMeshRectilinear("x", "y", "val")

                    # 1D coordinates and 2D data
                    df = xar.DataArray(
                        data=zdata,
                        dims=["x", "y"],
                        coords=dict(x=props["x0"], y=props["y0"]),
                    )
                    df = xar.Dataset(dict(val=df))
            else:
                # first convert 1D inputs to 2D, then reproject the grid and use
                # a curvilinear QuadMesh to display the data
                assert _register_pandas(), (
                    "EOmaps: missing dependency 'pandas' to convert 1D"
                    + "datasets to 2D as required for 'shade_raster'"
                )

                # use pandas to convert to 2D
                df = (
                    pd.DataFrame(
                        dict(
                            x=props["xorig"].ravel(),
                            y=props["yorig"].ravel(),
                            val=zdata.ravel(),
                        ),
                        copy=False,
                    )
                    .set_index(["x", "y"])
                    .to_xarray()
                )
                xg, yg = np.meshgrid(df.x, df.y)

                # transform the grid from input-coordinates to the plot-coordinates
                crs1 = CRS.from_user_input(self.data_specs.crs)
                crs2 = CRS.from_user_input(self._crs_plot)
                if crs1 != crs2:
                    transformer = Transformer.from_crs(
                        crs1,
                        crs2,
                        always_xy=True,
                    )
                    xg, yg = transformer.transform(xg, yg)

                # use a curvilinear QuadMesh
                self.shape.glyph = ds.glyphs.QuadMeshCurvilinear("x", "y", "val")

                df = xar.Dataset(
                    data_vars=dict(val=(["xx", "yy"], df.val.values.T)),
                    coords=dict(x=(["xx", "yy"], xg), y=(["xx", "yy"], yg)),
                )

            # once the data is shaded, convert to 1D for further processing
            self._1Dprops(props)

        else:
            assert (
                _register_pandas()
            ), f"EOmaps: missing dependency 'pandas' for {self.shape.name}"

            df = pd.DataFrame(
                dict(x=props["x0"].ravel(), y=props["y0"].ravel(), val=zdata.ravel()),
                copy=False,
            )

        if set_extent is True:
            # convert to a numpy-array to support 2D indexing with boolean arrays
            x, y = np.asarray(df.x), np.asarray(df.y)
            xf, yf = np.isfinite(x), np.isfinite(y)
            x_range = (np.nanmin(x[xf]), np.nanmax(x[xf]))
            y_range = (np.nanmin(y[yf]), np.nanmax(y[yf]))
        else:
            # update here to ensure bounds are set
            self.BM.update()
            x0, x1, y0, y1 = self.ax.get_extent()
            x_range = (x0, x1)
            y_range = (y0, y1)

        coll = mpl_ext.dsshow(
            df,
            glyph=self.shape.glyph,
            aggregator=self.shape.aggregator,
            shade_hook=self.shape.shade_hook,
            agg_hook=self.shape.agg_hook,
            # norm="eq_hist",
            # norm=plt.Normalize(vmin, vmax),
            cmap=cbcmap,
            ax=self.ax,
            plot_width=plot_width,
            plot_height=plot_height,
            # x_range=(x0, x1),
            # y_range=(y0, y1),
            # x_range=(df.x.min(), df.x.max()),
            # y_range=(df.y.min(), df.y.max()),
            x_range=x_range,
            y_range=y_range,
            **kwargs,
        )

        self.figure.coll = coll
        if verbose:
            print("EOmaps: Indexing for pick-callbacks...")

        if pick_distance is not None:
            # self.tree = cKDTree(np.stack([props["x0"], props["y0"]], axis=1))
            self.tree = searchtree(m=self._proxy(self), pick_distance=pick_distance)

            self.cb.pick._set_artist(coll)
            self.cb.pick._init_cbs()
            self.cb.pick._pick_distance = pick_distance
            self.cb._methods.append("pick")

        if dynamic is True:
            self.BM.add_artist(coll)
        else:
            self.BM.add_bg_artist(coll, layer)

        if dynamic is True:
            self.BM.update(clear=False)

    @staticmethod
    def _1Dprops(props):

        # convert all arrays in props to a proper 1D representation that will be used
        # to index and identify points

        # Note: _prepare_data already converts datasets to 1D if
        #       a shape that accepts non-rectangular datasets is used!

        # Note: both ravel and meshgrid return views!
        n_coord_shape = len(props["xorig"].shape)

        props["x0"], props["y0"] = (
            props["x0"].ravel(),
            props["y0"].ravel(),
        )
        props["xorig"], props["yorig"] = (
            props["xorig"].ravel(),
            props["yorig"].ravel(),
        )

        # in case 2D data and 1D coordinate arrays are provided, use a meshgrid
        # to identify the coordinates
        if n_coord_shape == 1 and len(props["z_data"].shape) == 2:

            props["x0"], props["y0"] = [
                i
                for i in np.broadcast_arrays(
                    *np.meshgrid(props["x0"], props["y0"], copy=False, sparse=True)
                )
            ]

            props["xorig"], props["yorig"] = [
                i
                for i in np.broadcast_arrays(
                    *np.meshgrid(
                        props["xorig"], props["yorig"], copy=False, sparse=True
                    )
                )
            ]

            # props["x0"], props["y0"] = [
            #     np.ravel(i) for i in np.meshgrid(props["x0"], props["y0"], copy=False)
            # ]
            # props["xorig"], props["yorig"] = [
            #     np.ravel(i)
            #     for i in np.meshgrid(props["xorig"], props["yorig"], copy=False)
            # ]

            # transpose since 1D coordinates are expected to be provided as (y, x)
            # and NOT as (x, y)
            props["z_data"] = props["z_data"].T.ravel()

        else:
            props["z_data"] = props["z_data"].ravel()

    def _memmap_props(self, dir=None):
        # memory-map all datasets in the self._props dict to free memory while
        # keeping all callbacks etc. responsive.
        if not hasattr(self.parent, "_tmpfolder"):
            if isinstance(dir, (str, Path)):
                self.parent._tmpfolder = TemporaryDirectory(dir=dir)
            else:
                self.parent._tmpfolder = TemporaryDirectory()

        memmaps = dict()

        for key, data in self._props.items():
            # don't memmap x0 and y0 since they are needed to identify points
            # (e.g. they would be loaded to memory as soon as a point is clicked)
            if key in ["x0", "y0"]:
                continue
            file = TemporaryFile(
                prefix=key + "__", suffix=".dat", dir=self.parent._tmpfolder.name
            )

            # filename = path.join(tmpfolder.name, f'{key}.dat')
            args = dict(filename=file, dtype="float32", shape=data.shape)

            fp = np.memmap(**args, mode="w+")

            fp[:] = data[:]  # write the data to the memmap object
            fp.flush()  # flush the data to disk

            # replace the file in memory with the memmap
            memmaps[key] = np.memmap(**args, mode="r")

        for key, val in memmaps.items():
            self._props[key] = val

    def make_dataset_pickable(
        self,
        pick_distance=100,
    ):
        """
        Make the associated dataset pickable **without plotting** it first.

        After executing this function, `m.cb.pick` callbacks can be attached to the
        `Maps` object.

        NOTE
        ----
        This function is ONLY necessary if you want to use pick-callbacks **without**
        actually plotting the data**! Otherwise a call to `m.plot_map()` is sufficient!

        - Each `Maps` object can always have only one pickable dataset.
        - The used data is always the dataset that was assigned in the last call to
          `m.plot_map()` or `m.make_dataset_pickable()`.
        - To get multiple pickable datasets, use an individual layer for each of the
          datasets (e.g. first `m2 = m.new_layer()` and then assign the data to `m2`)

        Parameters
        ----------
        pick_distance : int
            The search-area surrounding the clicked pixel used to identify the datapoint
            (e.g. a rectangle with a edge-size of `pick_distance * estimated radius`).

            The default is 100.

        Examples
        --------

        >>> m = Maps()
        >>> m.add_feature.preset.coastline()
        >>> ...
        >>> # a dataset that should be pickable but NOT visible...
        >>> # (e.g. in this case 100 points along the diagonal)
        >>> m2 = m.new_layer()
        >>> m2.set_data(*np.linspace([0, -180,-90,], [100, 180, 90], 100).T)
        >>> m2.make_dataset_pickable()
        >>> m2.cb.pick.attach.annotate()  # get an annotation for the invisible dataset
        >>> # ...call m2.plot_map() to make the dataset visible...
        """

        # if self.data is None:
        #     print("EOmaps: you must set the data first!")
        #     return

        if hasattr(self.figure, "coll") and self.figure.coll:
            print(
                "EOmaps: There is already a collection assigned to this Maps-object"
                + "... make sure to use a new layer for the pickable dataset!"
            )
            return

        # ---------------------- prepare the data
        props = self._prepare_data()
        self._props = props
        # use the axis as Artist to execute pick-events on any click on the axis

        x0, x1 = self._props["x0"].min(), self._props["x0"].max()
        y0, y1 = self._props["y0"].min(), self._props["y0"].max()

        # use a transparent rectangle of the data-extent as artist for picking
        (art,) = self.ax.fill([x0, x1, x1, x0], [y0, y0, y1, y1], fc="none", ec="none")

        self.figure.coll = art

        if pick_distance is not None:
            self.tree = searchtree(m=self._proxy(self), pick_distance=pick_distance)
            self.cb.pick._set_artist(art)
            self.cb.pick._init_cbs()
            self.cb.pick._pick_distance = pick_distance
            self.cb._methods.append("pick")

    def _plot_map(
        self,
        pick_distance=100,
        layer=None,
        dynamic=False,
        set_extent=True,
        assume_sorted=True,
        **kwargs,
    ):

        if "coastlines" in kwargs:
            kwargs.pop("coastlines")
            warnings.warn(
                "EOmaps: the 'coastlines' kwarg for 'plot_map' is depreciated!"
                + "Instead use "
                + "\n    m.add_feature.preset.ocean()"
                + "\n    m.add_feature.preset.coastline()"
                + " instead!"
            )

        ax = self.figure.ax

        cmap = kwargs.pop("cmap", "viridis")
        vmin = kwargs.pop("vmin", None)
        vmax = kwargs.pop("vmax", None)

        for key in ("array", "norm"):
            assert (
                key not in kwargs
            ), f"The key '{key}' is assigned internally by EOmaps!"

        try:
            # remove previously fetched backgrounds for the used layer
            if layer in self.BM._bg_layers and dynamic is False:
                del self.BM._bg_layers[layer]
                # self.BM._refetch_bg = True

            # if self.data is None:
            #     return

            # ---------------------- prepare the data
            props = self._prepare_data(assume_sorted=assume_sorted)

            # remember props for later use
            self._props = props

            if vmin is None and self.data is not None:
                vmin = np.nanmin(props["z_data"])
            if vmax is None and self.data is not None:
                vmax = np.nanmax(props["z_data"])

            # clip the data to properly account for vmin and vmax
            # (do this only if we don't intend to use the full dataset!)
            # if vmin or vmax:
            #     props["z_data"] = props["z_data"].clip(vmin, vmax)

            # ---------------------- classify the data
            cbcmap, norm, bins, classified = self._classify_data(
                vmin=vmin,
                vmax=vmax,
                cmap=cmap,
                classify_specs=self.classify_specs,
            )

            self.classify_specs._cbcmap = cbcmap
            self.classify_specs._norm = norm
            self.classify_specs._bins = bins
            self.classify_specs._classified = classified

            # ------------- plot the data

            # don't pass the array if explicit facecolors are set
            if (
                ("color" in kwargs and kwargs["color"] is not None)
                or ("facecolor" in kwargs and kwargs["facecolor"] is not None)
                or ("fc" in kwargs and kwargs["fc"] is not None)
            ):
                args = dict(array=None, cmap=None, norm=None, **kwargs)
            else:
                args = dict(array=props["z_data"], cmap=cbcmap, norm=norm, **kwargs)

            if self.shape.name in ["raster"]:
                # if input-data is 1D, try to convert data to 2D (required for raster)
                # TODO make an explicit data-conversion function for 2D-only shapes
                if len(props["xorig"].shape) == 2 and len(props["yorig"].shape) == 2:
                    coll = self.shape.get_coll(
                        props["xorig"], props["yorig"], "in", **args
                    )
                elif (
                    _register_pandas()
                    and isinstance(self.data, pd.DataFrame)
                    and isinstance(self.data_specs.x, str)
                    and isinstance(self.data_specs.y, str)
                    and len(props["z_data"].shape) == 1
                ):

                    df = (
                        pd.DataFrame(
                            dict(
                                x=props["xorig"].ravel(),
                                y=props["yorig"].ravel(),
                                val=props["z_data"].ravel(),
                            ),
                            copy=False,
                        ).set_index(["x", "y"])
                    )["val"].unstack("y")

                    xg, yg = np.meshgrid(df.index.values, df.columns.values)

                    if args["array"] is not None:
                        args["array"] = df.values.T

                    coll = self.shape.get_coll(xg, yg, "in", **args)

                else:
                    raise AssertionError(
                        "EOmaps: using 'raster' is only possible if "
                        + "you provide coordinates and data as 2D "
                        + "arrays or as a 1D pandas.DataFrame (which "
                        + "will be converted to 2D internally)"
                    )

                # convert values to 1D for callbacks etc.
                self._1Dprops(props)

            else:
                # convert input to 1D
                coll = self.shape.get_coll(
                    props["xorig"].ravel(), props["yorig"].ravel(), "in", **args
                )

            coll.set_clim(vmin, vmax)
            ax.add_collection(coll)

            self.figure.coll = coll

            if pick_distance is not None:
                self.tree = searchtree(m=self._proxy(self), pick_distance=pick_distance)

                self.cb.pick._set_artist(coll)
                self.cb.pick._init_cbs()
                self.cb.pick._pick_distance = pick_distance
                self.cb._methods.append("pick")

            if dynamic is True:
                self.BM.add_artist(coll)
            else:
                self.BM.add_bg_artist(coll, layer)

            if set_extent:
                # set the image extent
                # get the extent of the added collection
                b = self.figure.coll.get_datalim(ax.transData)
                ymin, ymax = ax.projection.y_limits
                xmin, xmax = ax.projection.x_limits
                # set the axis-extent
                ax.set_xlim(max(b.xmin, xmin), min(b.xmax, xmax))
                ax.set_ylim(max(b.ymin, ymin), min(b.ymax, ymax))

            self.figure.f.canvas.draw_idle()

        except Exception as ex:
            raise ex

    def plot_map(
        self,
        pick_distance=100,
        layer=None,
        dynamic=False,
        set_extent=True,
        memmap=False,
        assume_sorted=True,
        **kwargs,
    ):
        """
        Actually generate the map-plot based on the data provided as `m.data` and the
        specifications defined in "data_specs" and "classify_specs".

        NOTE
        ----
        Each call to plot_map will replace the collection used for picking!
        (only the last collection remains interactive on multiple calls to `m.plot_map()`)

        If you need multiple responsive datasets, use a new layer for each dataset!
        (e.g. via `m2 = m.new_layer()`)

        Parameters
        ----------
        pick_distance : int, float, str or None

            - If None, NO pick-callbacks will be assigned ('m.cb.pick' will not work!!)
              (useful for very large datasets to speed up plotting and save memory)
            - If a number is provided, it will be used to determine the search-area
              used to identify clicked pixels (e.g. a rectangle with a edge-size of
              `pick_distance * estimated radius`).
            - If a string is provided, it will be directly assigned as pick-radius
              (without multiplying by the estimated radius). This is useful for datasets
              whose radius cannot be determined (e.g. singular points etc.)

              The provided number is identified as radius in the plot-crs!

              The string must be convertible to a number, e.g. `float("40.5")`

            The default is 100.
        layer : int, str or None
            The layer at which the dataset will be plotted.
            ONLY relevant if `dynamic = False`!

            - If "all": the corresponding feature will be added to ALL layers
            - If None, the layer assigned to the Maps object is used (e.g. `m.layer`)

            The default is None.
        dynamic : bool
            If True, the collection will be dynamically updated.
        set_extent : bool
            Set the plot-extent to the data-extent.

            - if True: The plot-extent will be set to the extent of the data-coordinates
            - if False: The plot-extent is kept as-is

            The default is True
        memmap : bool, str or pathlib.Path
            Use memory-mapping to save some memory by storing intermediate datasets
            (e.g. projected coordinates, indexes & the data) in a temporary folder on
            disc rather than keeping everything in memory.
            This causes a slight performance penalty when identifying clicked points but
            it can provide a reduction in memory-usage for very large datasets
            (or for a very large number of interactive layers).

            - If None: memory-mapping is only used if "shade_raster" or "shade_points"
              is used as plot-shape.
            - if False: memory-mapping is disabled
            - if True: memory-mapping is used with an automatically located tempfolder
            - if str or pathlib.Path: memory-mapping is used and the provided folder
              is used as location for the temporary files (stored in a temp-subfolder).

            NOTE: The tempfolder and all files will be deleted if the figure is closed,
            the Maps-object is deleted or the kernel is interrupted!

            The location of the tempfolder is accessible via `m._tempfolder`

            The default is False.
        assume_sorted : bool, optional
            ONLY relevant for the shapes "raster" and "shade_raster"
            (and only if coordinates are provided as 1D arrays and data is a 2D array)

            Sort values with respect to the coordinates prior to plotting
            (required for QuadMesh if unsorted coordinates are provided)

            The default is True.


        Other Parameters:
        -----------------
        vmin, vmax : float, optional
            Min- and max. values assigned to the colorbar. The default is None.
        zorder : float
            The zorder of the artist (e.g. the stacking level of overlapping artists)
            The default is 1
        kwargs
            kwargs passed to the initialization of the matpltolib collection
            (dependent on the plot-shape) [linewidth, edgecolor, facecolor, ...]

            For "shade_points" or "shade_raster" shapes, kwargs are passed to
            `datashader.mpl_ext.dsshow`
        """

        if layer is None:
            layer = self.layer

        useshape = self.shape  # invoke the setter to set the default shape

        # make sure the colormap is properly set and transparencys are assigned
        cmap = kwargs.setdefault("cmap", "viridis")
        if "alpha" in kwargs and kwargs["alpha"] < 1:
            kwargs["cmap"] = cmap_alpha(
                cmap,
                kwargs["alpha"],
            )

        # make sure zorder is set to 1 by default
        # (by default shading would use 0 while ordinary collections use 1)
        kwargs.setdefault("zorder", 1)

        if useshape.name.startswith("shade"):
            self._shade_map(
                pick_distance=pick_distance,
                layer=layer,
                dynamic=dynamic,
                set_extent=set_extent,
                assume_sorted=assume_sorted,
                **kwargs,
            )
        else:
            self._plot_map(
                pick_distance=pick_distance,
                layer=layer,
                dynamic=dynamic,
                set_extent=set_extent,
                assume_sorted=assume_sorted,
                **kwargs,
            )

        # after plotting, use memory-mapping to store datasets required by
        # callbacks etc. so that we don't need to keep them in memory.
        if memmap:
            self._memmap_props(dir=memmap)

        if hasattr(self, "_data_mask") and not np.all(self._data_mask):
            print("EOmaps: Warning: some datapoints could not be drawn!")

        x0, y0, x1, y1 = self.crs_plot.boundary.bounds

        if (
            np.any(self._props["x0"] < x0)
            or np.any(self._props["x0"] > x1)
            or np.any(self._props["y0"] < y0)
            or np.any(self._props["y0"] > y1)
        ):
            print("EOmaps: Warning: some points are outside the CRS bounds!")

    def _remove_colorbar(self):
        if hasattr(self, "_ax_cb"):
            self._ax_cb.cla()
            self._ax_cb.remove()
            del self._ax_cb
        if hasattr(self, "_ax_cb_plot"):
            self._ax_cb_plot.cla()
            self._ax_cb_plot.remove()
            del self._ax_cb_plot
        # if hasattr(self, "_cb_gridspec"):
        #     del self._cb_gridspec

        del self._colorbar

        self.redraw()

    def _redraw_colorbar(self):
        # redraw for interactively updated colorbars

        if hasattr(self.figure, "coll") and self.figure.coll:
            if not hasattr(self, "_ds_data"):
                self._ds_data = self.figure.coll.get_ds_data()
        else:
            return

        # TODO requires numpy > 1.10.0
        if np.allclose(self._ds_data, self.figure.coll.get_ds_data(), equal_nan=True):
            return
        else:
            self._ds_data = self.figure.coll.get_ds_data()

        # redraw a dynamic_shade_indicator colorbar
        if hasattr(self, "_colorbar") and hasattr(self, "_cb_kwargs"):
            if self._cb_kwargs["dynamic_shade_indicator"] is True:

                # remove the axes but NOT the gridspec definition (self._cb_gridspec)
                # (It will be used to initialize new axes!)
                if hasattr(self, "_ax_cb"):
                    self._ax_cb.remove()
                    del self._ax_cb
                if hasattr(self, "_ax_cb_plot"):
                    self._ax_cb_plot.remove()
                    del self._ax_cb_plot

                del self._colorbar
                try:
                    self.BM._draw_animated(artists=[self.figure.coll])
                except Exception:
                    pass
                self.add_colorbar(**self._cb_kwargs)

    def _decode_values(self, val):
        """
        Decode data-values with respect to the provided "scale_factor" and "add_offset"
        using the formula:

            `actual_value = add_offset + scale_factor * encoded_value`

        The encoding is defined in `m.data_specs.encoding`

        Parameters
        ----------
        val : array-like
            The encoded data-values

        Returns
        -------
        decoded_values
            The decoded data values
        """

        encoding = self.data_specs.encoding
        if encoding is not None:
            try:
                scale_factor = encoding.get("scale_factor", None)
                add_offset = encoding.get("add_offset", None)

                if scale_factor:
                    val *= scale_factor
                if add_offset:
                    val += add_offset

                return val
            except:
                return val
        else:
            return val

    def _default_cb_tick_formatter(self, x, pos, precision=None):
        """
        A formatter to format the tick-labels of the colorbar for encoded datasets.
        (used in xaxis.set_major_formatter() )
        """
        # if precision=None the shortest representation of the number is used
        return np.format_float_positional(self._decode_values(x), precision)

    def add_colorbar(
        self,
        gs=0.2,
        orientation="horizontal",
        label=None,
        density=False,
        histbins=256,
        tick_precision=3,
        top=0.05,
        bottom=0.1,
        left=0.1,
        right=0.05,
        histogram_size=9,
        layer=None,
        log=False,
        tick_formatter=None,
        dynamic_shade_indicator=False,
        add_extend_arrows="auto",
        extend_frac=0.025,
        show_outline=False,
    ):
        """
        Add a colorbar to an existing figure.

        The colorbar always represents the data of the associated Maps-object
        that was assigned in the last call to `m.plot_map()`.

        By default, the colorbar will only be visible on the layer of the associated
        Maps-object (you can override this by providing an explicit "layer"-name).

        To change the position of the colorbar after it has been created, use:

            >>> cb = m.add_colorbar()
            >>> m.figure.set_colorbar_position(pos=[.1, .05, .8, .2], ratio=10, cb=cb)

        Parameters
        ----------
        gs : float or matpltolib.gridspec.SubplotSpec
            The relative size of the colorbar (or an explicit GridSpec definition)

            - if float: The fraction of the the parent axes to use for the colorbar.
              (The colorbar will "steal" some space from the parent axes.)
            - if SubplotSpec : A SubplotSpec instance that will be used to initialize
              the colorbar.

            The default is 0.2.
        orientation : str
            The orientation of the colorbar ("horizontal" or "vertical")
            The default is "horizontal"
        label : str or None
            The label of the colorbar.
            If None, the parameter-name (e.g. `m.data_specs.parameter`) is used.
            The default is None.
        density : bool or None
            Indicator if the y-axis of the histogram should represent the
            probability-density (True) or the number of counts per bin (False)
            The default is False.
        histbins : int, list, tuple, array or "bins", optional
            - If int: The number of histogram-bins to use for the colorbar.
            - If list, tuple or numpy-array: the bins to use
            - If "bins": use the bins obtained from the classification
              (ONLY possible if a classification scheme is used!)

            The default is 256.
        tick_precision : int or None
            The precision of the tick-labels in the colorbar.
            The default is 3.
        top, bottom, left, right : float
            The padding between the colorbar and the parent axes (as fraction of the
            plot-height (if "horizontal") or plot-width (if "vertical")
            The default is (0.05, 0.1, 0.1, 0.05)
        histogram_size : float
            Set the relative size of the histogram compared to the colorbar, e.g.:

            `<size of histogram> = histogram_size * <size of colorbar>`

            - 0 = NO histogram (e.g. a "plain" colorbar)
            - 1 = histogram and colorbar have the same size
            - 999 = NO colorbar (e.g. a "plain" histogram)

            The default is 9.
        layer : int, str or None, optional
            The layer to put the colorbar on.
            To make the colorbar visible on all layers, use `layer="all"`
            If None, the layer of the associated Maps-object is used.
            The default is None.
        log : bool, optional
            Indicator if the y-axis of the plot should be logarithmic or not.
            The default is False
        dynamic_shade_indicator : bool
            ONLY relevant if data-shading is used! ("shade_raster" or "shade_points")

            - False: The colorbar represents the actual (full) dataset
            - True: The colorbar is dynamically updated and represents the density of
              the shaded pixel values within the current field of view.

            The default is False.
        tick_formatter : callable
            A function that will be used to format the ticks of the colorbar.

            The function will be used with matpltlibs `set_major_formatter`...
            For details, see:
            https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html

            Call-signagure:

            >>> def tick_formatter(x, pos):
            >>>     # x ... the tick-value
            >>>     # pos ... the tick-position
            >>>     return f"{x} m"

            The default is None.
        add_extend_arrows : str or False
            Set if extension-arrows should be drawn. (e.g. to indicate that there are
            some data-values outside the colorbar-range)

            - Can be one of: ("auto", "upper", "lower", "both" or False)
            - If False: NO extension-arrows will be drawn.
            - If "auto": extension-arrows are only drawn if values outside the color
              boundaries are encoundered. The default is "auto"

            Note: The range of the colors is set with `m.plot_map(vmin=..., vmax=...)`
            The default is "auto".
        extend_frac : float or None
            The fraction of the colorbar to use for adding "extension-arrows" to
            indicate out-of-bounds values.
            If None, no extension arrows will be drawn.
            The default is 0.015
        show_outline : bool or dict
            Indicator if an outline should be added to the histogram.
            (e.g. a line encompassing the histogram)

            If a dict is provided, it is passed to `plt.step()` to style the line.
            (e.g. with ordinary matplotlib parameters such as color, lw, ls etc.)
            If True, the following properties are used:

            - {"color": "k", "lw": 1}

            The default is False.

        See Also
        --------
        - m.figure.set_colorbar_position :
            Adjust the position and ratio of existing colorbars

        Notes
        -----
        Here's how the padding looks like as a sketch:

        >>> _________________________________________________________
        >>> |[ - - - - - - - - - - - - - - - - - - - - - - - - - - ]|
        >>> |[ - - - - - - - - - - - - MAP - - - - - - - - - - - - ]|
        >>> |[ - - - - - - - - - - - - - - - - - - - - - - - - - - ]|
        >>> |                                                       |
        >>> |                         (top)                         |
        >>> |                                                       |
        >>> |                  [ -  HISTOGRAM  - ]                  |
        >>> |      (left)       [ - COLORBAR  - ]      (right)      |
        >>> |                                                       |
        >>> |                       (bottom)                        |
        >>> |_______________________________________________________|

        """

        if self.data is None:
            print(
                "EOmaps: There is no data for the colorbar! Use m.set_data(data=...)"
                + "to set the data."
            )
            return

        assert hasattr(
            self.classify_specs, "_bins"
        ), "EOmaps: you need to call `m.plot_map()` before adding a colorbar!"

        if histbins == "bins":
            assert (
                self.classify_specs._classified
            ), "EOmaps: using histbins='bins' is only possible for classified data!"

        if layer is None:
            layer = self.layer

        self._cb_kwargs = dict(
            orientation=orientation,
            label=label,
            density=density,
            histbins=histbins,
            tick_precision=tick_precision,
            layer=layer,
            log=log,
            dynamic_shade_indicator=dynamic_shade_indicator,
            tick_formatter=tick_formatter,
        )

        parent_m_for_cb = None
        if isinstance(gs, (int, float)):
            if hasattr(self, "_colorbar"):
                print(
                    "EOmaps: A colorbar already exists for this Maps-object!\n"
                    + "...use a new layer if you want multiple colorbars or use "
                    + "`m._remove_colorbar() to remove the existing colorbar."
                )
                return

            # check if there is already an existing colorbar in another axis
            # and if we find one, use its specs instead of creating a new one

            if hasattr(self, "_cb_gridspec"):
                parent_m_for_cb = self
            else:
                # check if self is actually just another layer of an existing Maps object
                # that already has a colorbar assigned
                for m in [self.parent, *self.parent._children]:
                    if m is not self and m.ax is self.ax:
                        if hasattr(m, "_cb_gridspec"):
                            parent_m_for_cb = m
                            break

        if parent_m_for_cb:
            try:
                if (
                    parent_m_for_cb._cb_gridspec.nrows == 2
                    and parent_m_for_cb._cb_gridspec.ncols == 1
                ):
                    cb_orientation = "vertical"
                else:
                    cb_orientation = "horizontal"
            except AttributeError:
                print(
                    "EOmaps: could not add colorbar... maybe a colorbar for the"
                    f"layer {layer} already exists?"
                )
                return

        if parent_m_for_cb is None:
            # initialize colorbar axes
            if isinstance(gs, float):
                frac = gs
                gs = self.figure.ax.get_subplotspec()

                # get the original subplot-spec of the axes, and divide it based on
                # the fraction that is intended for the colorbar
                if orientation == "horizontal":
                    gs = GridSpecFromSubplotSpec(
                        4,
                        3,
                        gs,
                        height_ratios=(1, top, frac, bottom),
                        width_ratios=(left, 1, right),
                        wspace=0,
                        hspace=0,
                    )
                    self.figure.ax.set_subplotspec(gs[0, :])
                    gsspec = gs[2, 1]

                elif orientation == "vertical":
                    gs = GridSpecFromSubplotSpec(
                        3,
                        4,
                        gs,
                        width_ratios=(1, top, frac, bottom),
                        height_ratios=(left, 1, right),
                        hspace=0,
                        wspace=0,
                    )
                    self.figure.ax.set_subplotspec(gs[:, 0])
                    gsspec = gs[1, 2]

                else:
                    raise AssertionError("'{orientation}' is not a valid orientation")
            else:
                gsspec = gs

            if orientation == "horizontal":
                # sub-gridspec for the colorbar
                cbgs = GridSpecFromSubplotSpec(
                    nrows=2,
                    ncols=1,
                    subplot_spec=gsspec,
                    hspace=0,
                    wspace=0,
                    height_ratios=[histogram_size, 1],
                )

                # "_add_colorbar" orientation is opposite to the colorbar-orientation!
                cb_orientation = "vertical"

            elif orientation == "vertical":
                # sub-gridspec for the colorbar
                cbgs = GridSpecFromSubplotSpec(
                    nrows=1,
                    ncols=2,
                    subplot_spec=gsspec,
                    hspace=0,
                    wspace=0,
                    width_ratios=[histogram_size, 1],
                )

                # "_add_colorbar" orientation is opposite to the colorbar-orientation!
                cb_orientation = "horizontal"
        else:
            cbgs = parent_m_for_cb._cb_gridspec
            # cbgs = [
            #     parent_m_for_cb.figure.ax_cb.get_gridspec()[0],
            #     parent_m_for_cb.figure.ax_cb_plot.get_gridspec()[1],
            # ]

        ax_cb = self.figure.f.add_subplot(
            cbgs[1],
            frameon=False,
            label="ax_cb",
        )
        ax_cb_plot = self.figure.f.add_subplot(
            cbgs[0],
            frameon=True,
            label="ax_cb_plot",
        )
        # keep the background of the plot-axis but remove the outer frame
        ax_cb_plot.spines["top"].set_visible(False)
        ax_cb_plot.spines["right"].set_visible(False)
        ax_cb_plot.spines["bottom"].set_visible(False)
        ax_cb_plot.spines["left"].set_visible(False)

        # join colorbar and histogram axes
        if cb_orientation == "horizontal":
            ax_cb_plot.get_shared_y_axes().join(ax_cb_plot, ax_cb)
        elif cb_orientation == "vertical":
            ax_cb_plot.get_shared_x_axes().join(ax_cb_plot, ax_cb)

        coll = self.figure.coll

        renorm = False
        vmin = coll.norm.vmin
        vmax = coll.norm.vmax

        if _register_datashader() and isinstance(coll, mpl_ext.ScalarDSArtist):
            aggname = self.shape.aggregator.__class__.__name__
            if aggname in ["first", "last", "max", "min", "mean", "mode"]:
                pass
            else:
                renorm = True

                if not dynamic_shade_indicator:
                    print(
                        "EOmaps: Only dynamic colorbars are possible when using"
                        + f" '{aggname}' as datashader-aggregation reduction method "
                        + "...creating a 'dynamic_shade_indicator' colorbar instead."
                    )
                    dynamic_shade_indicator = True

            if dynamic_shade_indicator:
                try:
                    z_data = coll.get_ds_data().values
                    # z_data = coll.norm(z_data)
                    # z_data = self.classify_specs._norm(z_data)
                except:
                    self.redraw()
                    z_data = coll.get_ds_data().values
                    # z_data = coll.norm(z_data)
                    # z_data = self.classify_specs._norm(z_data)

                if "count" in aggname:
                    # make sure we don't count empty pixels
                    z_data = z_data[~(z_data == 0)]

                # datashader sets None to 0 by default!
                # z_data = z_data[z_data > 0]

                bins = self.classify_specs._bins
                # bins = None

                cmap = self.classify_specs._cbcmap
                # cmap = coll.get_cmap()

                if renorm:
                    z_data = z_data[~np.isnan(z_data)]
                    norm = coll.norm
                    # make sure the norm clips with respect to vmin/vmax
                    # (only clip if either vmin or vmax is not None)
                    # if vmin or vmax:
                    #     z_data = z_data.clip(vmin, vmax)
                    cmap = coll.get_cmap()
                else:
                    norm = self.classify_specs._norm

                def redraw(*args, **kwargs):
                    self._redraw_colorbar()

                # TODO remove cid on figure close
                if not hasattr(self, "_cid_colorbar"):
                    self._cid_colorbar = self.figure.coll.add_callback(redraw)
                    # TODO colorbar not properly updated on layer change after zoom
                    self.BM.on_layer(redraw, layer=self.layer, persistent=True, m=self)
            else:
                z_data = None
                bins = self.classify_specs._bins
                cmap = self.classify_specs._cbcmap
                norm = self.classify_specs._norm

        else:
            if dynamic_shade_indicator:
                print(
                    "EOmaps: using 'dynamic_shade_indicator=True' is only possible "
                    + " with 'shade' shapes (e.g. 'shade_raster' or 'shade_points'"
                )
                dynamic_shade_indicator = False

            z_data = None
            bins = self.classify_specs._bins
            cmap = self.classify_specs._cbcmap
            norm = self.classify_specs._norm

        # reflect changes to the dynamic_shade_indicator in the saved kwargs
        self._cb_kwargs["dynamic_shade_indicator"] = dynamic_shade_indicator

        cb = self._add_colorbar(
            ax_cb=ax_cb,
            ax_cb_plot=ax_cb_plot,
            bins=bins,
            cmap=cmap,
            norm=norm,
            z_data=z_data,
            vmin=vmin,
            vmax=vmax,
            # bins=self.classify_specs._bins,
            # cmap=self.classify_specs._cbcmap,
            # norm=self.classify_specs._norm,
            classified=self.classify_specs._classified,
            orientation=cb_orientation,
            label=label,
            density=density,
            tick_precision=tick_precision,
            histbins=histbins,
            log=log,
            tick_formatter=tick_formatter,
            show_outline=show_outline,
        )

        # hide the colorbar if it is not added to the currently visible layer
        if layer not in [self.BM._bg_layer, "all"]:
            ax_cb.set_visible(False)
            ax_cb_plot.set_visible(False)
            self.BM._hidden_axes.add(ax_cb)
            self.BM._hidden_axes.add(ax_cb_plot)

        self._ax_cb = ax_cb
        self._ax_cb_plot = ax_cb_plot
        self._cb_gridspec = cbgs

        if dynamic_shade_indicator:
            ax_cb_plot.set_ylabel(
                ("logarithmic\n" if log else "")
                + f"shaded pixel\n{'density' if density else 'bin count'}"
            )
            ax_cb_plot.tick_params(labelleft=False, which="both")

        if orientation == "horizontal":
            if vmin and vmax:
                ax_cb_plot.set_xlim(vmin, vmax)
            # else:
            #     ax_cb_plot.autoscale_view(tight=True)

        if orientation == "vertical":
            if vmin and vmax:
                ax_cb_plot.set_ylim(vmin, vmax)
            # else:
            #     ax_cb_plot.autoscale_view(tight=True)

        self.BM.add_bg_artist(self._ax_cb, layer)
        self.BM.add_bg_artist(self._ax_cb_plot, layer)

        if add_extend_arrows is not False:
            ax_cb_extend = self._add_cb_extend_arrows(
                cb, orientation, extend_frac=extend_frac, which=add_extend_arrows
            )
        else:
            ax_cb_extend = None

        # remember colorbar for later (so that we can update its position etc.)
        self._colorbar = [
            layer,
            cbgs,
            ax_cb,
            ax_cb_plot,
            ax_cb_extend,
            extend_frac,
            orientation,
            cb,
        ]

        return [
            layer,
            cbgs,
            ax_cb,
            ax_cb_plot,
            ax_cb_extend,
            extend_frac,
            orientation,
            cb,
        ]

    def indicate_masked_points(self, radius=1.0, **kwargs):
        """
        Add circles to the map that indicate masked points.
        (e.g. points resulting in very distorted shapes etc.)

        Parameters
        ----------
        radius : float, optional
            The radius to use for plotting the indicators for the masked
            points. The unit of the radius is map-pixels! The default is 1.
        **kwargs :
            additional kwargs passed to `m.plot_map(**kwargs)`.

        Returns
        -------
        m : eomaps.Maps
            A (connected) copy of the maps-object with the data set to the masked pixels.
        **kwargs
            additional kwargs passed to `m.plot_map(**kwargs)`
        """
        if not hasattr(self, "_data_mask"):
            print("EOmaps: There are no masked points to indicate!")
            return

        mask = np.broadcast_to(self._data_mask, self._props["z_data"].shape)

        if len(self._props["z_data"][~mask]) == 0:
            print("EOmaps: There are no masked points to indicate!")
            return

        kwargs.setdefault("ec", "r")

        self.ax.scatter(
            self._props["x0"][~mask],
            self._props["y0"][~mask],
            cmap=self.classify_specs._cbcmap,
            c=self._props["z_data"][~mask],
            **kwargs,
        )

    @staticmethod
    def _make_rect_poly(x0, y0, x1, y1, crs=None, npts=100):
        """
        return a geopandas.GeoDataFrame with a rectangle in the given crs

        Parameters
        ----------
        x0, y0, y1, y1 : float
            the boundaries of the shape
        npts : int, optional
            The number of points used to draw the polygon-lines. The default is 100.
        crs : any, optional
            a coordinate-system identifier.  (e.g. output of `m.get_crs(crs)`)
            The default is None.

        Returns
        -------
        gdf : geopandas.GeoDataFrame
            the geodataframe with the shape and crs defined

        """

        assert _register_geopandas(), (
            "EOmaps: Missing dependency `geopandas`!\n"
            + "please install '(conda install -c conda-forge geopandas)'"
        )

        from shapely.geometry import Polygon

        xs, ys = np.linspace([x0, y0], [x1, y1], npts).T
        x0, y0, x1, y1, xs, ys = np.broadcast_arrays(x0, y0, x1, y1, xs, ys)
        verts = np.column_stack(((x0, ys), (xs, y1), (x1, ys[::-1]), (xs[::-1], y0))).T

        gdf = gpd.GeoDataFrame(geometry=[Polygon(verts)])
        gdf.set_crs(crs, inplace=True)

        return gdf

    def indicate_extent(self, x0, y0, x1, y1, crs=4326, npts=100, **kwargs):
        """
        Indicate a rectangular extent in a given crs on the map.
        (the rectangle is drawn as a polygon where each line is divided by "npts"
        points to ensure correct re-projection of the shape to other crs)

        Parameters
        ----------
        x0, y0, y1, y1 : float
            the boundaries of the shape
        npts : int, optional
            The number of points used to draw the polygon-lines.
            (e.g. to correctly display curvature in projected coordinate-systems)
            The default is 100.
        crs : any, optional
            a coordinate-system identifier.
            The default is 4326 (e.g. lon/lat).
        kwargs :
            additional keyword-arguments passed to `m.add_gdf()`.

        """

        assert _register_geopandas(), (
            "EOmaps: Missing dependency `geopandas`!\n"
            + "please install '(conda install -c conda-forge geopandas)'"
            + "to use `m.indicate_extent()`."
        )

        gdf = self._make_rect_poly(x0, y0, x1, y1, self.get_crs(crs), npts)
        self.add_gdf(gdf, **kwargs)

    def add_logo(self, filepath=None, position="lr", size=0.12, pad=0.1):
        """
        Add a small image (png, jpeg etc.) to the map whose position is dynamically
        updated if the plot is resized or zoomed.

        Parameters
        ----------
        filepath : str, optional
            if str: The path to the image-file.
            The default is None in which case an EOmaps logo is added to the map.
        position : str, optional
            The position of the logo.
            - "ul", "ur" : upper left, upper right
            - "ll", "lr" : lower left, lower right
            The default is "lr".
        size : float, optional
            The size of the logo as a fraction of the axis-width.
            The default is 0.15.
        pad : float, tuple optional
            Padding between the axis-edge and the logo as a fraction of the logo-width.
            If a tuple is passed, (x-pad, y-pad)
            The default is 0.1.
        """

        if filepath is None:
            filepath = Path(__file__).parent / "logo.png"

        im = mpl.image.imread(filepath)

        def getpos(pos):
            s = size
            if isinstance(pad, tuple):
                pwx, pwy = (s * pad[0], s * pad[1])
            else:
                pwx, pwy = (s * pad, s * pad)

            if position == "lr":
                p = dict(rect=[pos.x1 - s - pwx, pos.y0 + pwy, s, s], anchor="SE")
            elif position == "ll":
                p = dict(rect=[pos.x0 + pwx, pos.y0 + pwy, s, s], anchor="SW")
            elif position == "ur":
                p = dict(rect=[pos.x1 - s - pwx, pos.y1 - s - pwy, s, s], anchor="NE")
            elif position == "ul":
                p = dict(rect=[pos.x0 + pwx, pos.y1 - s - pwy, s, s], anchor="NW")
            return p

        figax = self.figure.f.add_axes(**getpos(self.ax.get_position()))
        figax.set_navigate(False)
        figax.set_axis_off()
        art = figax.imshow(im, aspect="equal", zorder=999)
        self.BM.add_artist(art)

        def setlim(*args, **kwargs):
            figax.set_position(getpos(self.ax.get_position())["rect"])

        def update_decorator(f):
            # use this so that we can "undecorate" the function with the
            # __wrapped__ property
            @wraps(f)
            def newf(*args, **kwargs):
                ret = f(*args, **kwargs)
                setlim()
                return ret

            return newf

        toolbar = self.figure.f.canvas.toolbar
        if toolbar is not None:
            toolbar._update_view = update_decorator(toolbar._update_view)
            toolbar.release_zoom = update_decorator(toolbar.release_zoom)
            toolbar.release_pan = update_decorator(toolbar.release_pan)

        def cleanup():

            toolbar._update_view = toolbar._update_view.__wrapped__
            toolbar.release_zoom = toolbar.release_zoom.__wrapped__
            toolbar.release_pan = toolbar.release_pan.__wrapped__

        if toolbar is not None:
            self._cleanup_functions.add(cleanup)

        self._logo_cids.add(self.figure.f.canvas.mpl_connect("resize_event", setlim))

    def show_layer(self, name):
        """
        Display the selected layer on the map.

        See Also
        --------
        - Maps.util.layer_selector
        - Maps.util.layer_slider

        Parameters
        ----------
        name : str or int, optional
            The name of the layer to activate.
            The default is None.
        """
        layers = self._get_layers()

        if name not in layers:
            lstr = " - " + "\n - ".join(map(str, layers))

            raise AssertionError(
                f"EOmaps: The layer '{name}' does not exist...\n"
                + f"Use one of: \n{lstr}"
            )

        # invoke the bg_layer setter of the blit-manager
        self.BM.bg_layer = name
        # self.BM.canvas.draw_idle()
        self.BM.update()

    def redraw(self):
        """
        Force a re-draw of all cached background layers.
        This will make sure that actions not managed by EOmaps are also properly drawn.

        - Use this at the very end of your code to trigger a final re-draw!

        Note
        ----
        Don't use this in an interactive context since it will trigger a re-draw
        of all background-layers!

        To make an artist dynamically updated if you interact with the map, use:

        >>> m.BM.add_artist(artist)
        """

        self.BM._refetch_bg = True
        self.BM.canvas.draw()

    @wraps(GridSpec.update)
    def subplots_adjust(self, **kwargs):
        self.parent.figure.gridspec.update(**kwargs)
        # after changing margins etc. a redraw is required
        # to fetch the updated background!

        # make sure the position of the axis holding the colorbar-extension-arrows
        # is properly updated
        self._update_cb_extend_pos()
        self.redraw()

    def _get_layers(self, exclude=None):
        # return a list of all (empty and non-empty) layer-names
        layers = set((m.layer for m in (self.parent, *self.parent._children)))
        # add layers that are not yet activated (but have an activation
        # method defined...)
        layers = layers.union(set(self.BM._on_layer_activation))
        # add all (possibly still invisible) layers with artists defined
        layers = layers.union(set(self.BM._bg_artists))

        if exclude:
            for l in exclude:
                if l in layers:
                    layers.remove(l)

        # sort the layers
        layers = sorted(layers, key=lambda x: str(x))

        return layers

    def fetch_layers(self, layers=None, verbose=True):
        """
        Fetch (and cache) the layers of a map.

        This is particularly useful if you want to use sliders or buttons to quickly
        switch between the layers (e.g. once the backgrounds are cached, switching
        layers will be fast).

        Note: After zooming or re-sizing the map, the cache is cleared and
        you need to call this function again.

        Parameters
        ----------
        layers : list or None, optional
            A list of layer-names that should be fetched.
            If None, all layers (except the "all" layer) are fetched.
            The default is None.
        verbose : bool
            Indicator if status-messages should be printed or not.
            The default is True.

        See Also
        --------
        m.cb.keypress.attach.fetch_layers : use a keypress callback to fetch layers

        """

        active_layer = self.BM._bg_layer
        all_layers = self._get_layers()

        if layers is None:
            layers = all_layers
            if "all" in layers:
                layers.remove("all")  # don't explicitly fetch the "all" layer
        else:
            if not set(layers).issubset(all_layers):
                raise AssertionError(
                    "EOmaps: Unable to fetch the following layers:\n - "
                    + "\n - ".join(set(layers).difference(all_layers))
                )

        nlayers = len(layers)
        assert nlayers > 0, "EOmaps: There are no layers to fetch."

        for i, l in enumerate(layers):
            if verbose:
                print("EOmaps: fetching layer", f"{i + 1}/{nlayers}:", l)
            self.show_layer(l)

        self.show_layer(active_layer)
        self.BM.update()

    def get_layout(self, filepath=None, override=False):
        """
        Get the positions of all axes within the current plot.

        To re-apply a layout, use:

            >>> l = m.get_layout()
            >>> m.set_layout(l)

        Note
        ----
        The returned list is only a snapshot of the current layout.
        It can only be re-applied to a given figure if the order at which the axes are
        created remains the same!

        Parameters
        ----------
        filepath : str or pathlib.Path, optional
            If provided, a json-file will be created at the specified destination that
            can be used in conjunction with `m.set_layout(...)` to apply the layout:

            >>> m.get_layout(filepath=<FILEPATH>, override=True)
            >>> m.apply_layout_layout(<FILEPATH>)

            You can also manually read-in the layout-dict via:
            >>> import json
            >>> layout = json.load(<FILEPATH>)

        Returns
        -------
        layout : dict or None
            A dict of the positons of all axes, e.g.: {1:(x0, y0, width height), ...}
        """

        layout = dict()
        for i, ax in enumerate(self.figure.f.axes):
            layout[str(i)] = ax.get_position().bounds

        if filepath is not None:
            filepath = Path(filepath)
            assert (
                not filepath.exists() or override
            ), f"The file {filepath} already exists! Use override=True to relace it."
            with open(filepath, "w") as file:
                json.dump(layout, file)
            print("EOmaps: Layout saved to:\n       ", filepath)

        return layout

    def apply_layout(self, layout):
        """
        Set the positions of all axes within the current plot based on a previously
        defined layout.

        To apply a layout, use:

            >>> l = m.get_layout()
            >>> m.set_layout(l)

        To save a layout to disc and apply it at a later stage, use
            >>> m.get_layout(filepath=<FILEPATH>)
            >>> m.set_layout(<FILEPATH>)


        Note
        ----
        The returned list is only a snapshot of the current layout.
        It can only be re-applied to a given figure if the order at which the axes are
        created remains the same!

        Parameters
        ----------
        layout : dict, str or pathlib.Path
            If a dict is provided, it is directly used to define the layout.

            If a string or a pathlib.Path object is provided, it will be used to
            read a previously dumped layout (e.g. with `m.get_layout(filepath)`)

        """
        if isinstance(layout, (str, Path)):
            with open(layout, "r") as file:
                layout = json.load(file)

        nl = len(layout)
        na = len(self.figure.f.axes)
        assert nl == na, (
            f"EOmaps: Layout specifies dimensions for {nl} axes but there are {na} "
            + "axes present in the figure!"
        )

        for i, ax in enumerate(self.figure.f.axes):
            ax.set_position(layout[str(i)])

        self.redraw()

    def edit_layout(self, filepath=None):
        """
        Activate the "layout-editor" to quickly re-arrange the positions of subplots.

        - This is the same as pressing "alt + d" on the keyboard!
        - To exit the editor, press "escape" or "alt + d" on the keyboard!

        Parameters
        ----------
        filepath : str, pathlib.Path or None, optional
            A path to a file that will be used to store the layout after you exit
            the layout-editor.
            This file can then be used to apply the layout to the map with

            >>> m.apply_layout(filepath=filepath)

            NOTE: The file will be overwritten if it already exists!!
            The default is None.

        """
        self._layout_editor._make_draggable(filepath=filepath)


class _InsetMaps(Maps):
    # a subclass of Maps that includes some special functions for inset maps

    def __init__(
        self,
        parent,
        crs=4326,
        layer="all",
        xy=(45, 45),
        xy_crs=4326,
        radius=5,
        radius_crs=None,
        plot_position=(0.5, 0.5),
        plot_size=0.5,
        shape="ellipses",
        indicate_extent=True,
        boundary=True,
        **kwargs,
    ):

        possible_shapes = ["ellipses", "rectangles", "geod_circles"]
        assert (
            shape in possible_shapes
        ), f"EOmaps: the inset shape can only be one of {possible_shapes}"

        if shape == "geod_circles":
            assert radius_crs is None, (
                "EOmaps: Using 'radius_crs' is not possible if 'geod_circles' is "
                + "used as shape! (the radius for `geod_circles` is always in meters!)"
            )

        if radius_crs is None:
            radius_crs = xy_crs

        extent_kwargs = dict(ec="r", lw=1, fc="none")
        boundary_kwargs = dict(ec="r", lw=2)

        if isinstance(boundary, dict):
            assert (
                len(set(boundary.keys()).difference({"ec", "lw"})) == 0
            ), "EOmaps: only 'ec' and 'lw' keys are allowed for the 'boundary' dict!"

            boundary_kwargs.update(boundary)
            # use same edgecolor for boundary and indicator by default
            extent_kwargs["ec"] = boundary["ec"]

        if isinstance(indicate_extent, dict):
            extent_kwargs.update(indicate_extent)

        x, y = xy
        plot_x, plot_y = plot_position

        # setup a gridspec at the desired position
        gs = GridSpec(
            1,
            1,
            left=plot_x - plot_size / 2,
            bottom=plot_y - plot_size / 2,
            top=plot_y + plot_size / 2,
            right=plot_x + plot_size / 2,
        )[0]

        # initialize a new maps-object with a new axis
        super().__init__(crs=crs, parent=parent, gs_ax=gs, layer=layer, **kwargs)

        # get the boundary of a ellipse in the inset_crs
        bnd, bnd_verts = self._get_inset_boundary(
            x, y, xy_crs, radius, radius_crs, shape
        )

        # set the map boundary
        self.ax.set_boundary(bnd)
        # set the plot-extent to the envelope of the shape
        (x0, y0), (x1, y1) = bnd_verts.min(axis=0), bnd_verts.max(axis=0)
        self.ax.set_extent((x0, x1, y0, y1), crs=self.ax.projection)

        # TODO turn off navigation until the matpltolib pull-request on
        # zoom-events in overlapping axes is resolved
        # https://github.com/matplotlib/matplotlib/pull/22347
        self.ax.set_navigate(False)

        # set style of the inset-boundary
        if boundary is not False:
            self.ax.spines["geo"].set_edgecolor(boundary_kwargs["ec"])
            self.ax.spines["geo"].set_lw(boundary_kwargs["lw"])

        self._inset_props = dict(
            xy=xy, xy_crs=xy_crs, radius=radius, radius_crs=radius_crs, shape=shape
        )

        if indicate_extent is not False:
            self.indicate_inset_extent(self.parent, **extent_kwargs)

    def plot_map(self, *args, **kwargs):
        set_extent = kwargs.pop("set_extent", False)
        super().plot_map(*args, **kwargs, set_extent=set_extent)

    # add a convenience-method to add a boundary-polygon to a map
    def indicate_inset_extent(self, m, n=100, **kwargs):
        """
        Add a polygon to a  map that indicates the extent of the inset-map.

        Parameters
        ----------
        m : eomaps.Maps
            The Maps-object that will be used to draw the marker.
            (e.g. the map on which the extent of the inset should be indicated)
        n : int
            The number of points used to represent the polygon.
            The default is 100.
        kwargs :
            additional keyword-arguments passed to `m.add_marker`
            (e.g. "facecolor", "edgecolor" etc.)
        """

        if not any((i in kwargs for i in ["fc", "facecolor"])):
            kwargs["fc"] = "none"
        if not any((i in kwargs for i in ["ec", "edgecolor"])):
            kwargs["ec"] = "r"
        if not any((i in kwargs for i in ["lw", "linewidth"])):
            kwargs["lw"] = 1

        m.add_marker(
            shape=self._inset_props["shape"],
            xy=self._inset_props["xy"],
            xy_crs=self._inset_props["xy_crs"],
            radius=self._inset_props["radius"],
            radius_crs=self._inset_props["radius_crs"],
            n=n,
            **kwargs,
        )

    # add a convenience-method to set the position based on the center of the axis
    def set_inset_position(self, x=None, y=None, size=None):
        """
        Set the (center) position and size of the inset-map.

        Parameters
        ----------
        x, y : int or float, optional
            The center position in relative units (0-1) with respect to the figure.
            If None, the existing position is used.
            The default is None.
        size : float, optional
            The relative radius (0-1) of the inset in relation to the figure width.
            If None, the existing size is used.
            The default is None.
        """

        y0, y1, x0, x1 = self.figure.gridspec.get_grid_positions(self.figure.f)

        if self.figure.cb_gridspec is not None:
            y0cb, y1cb, x0cb, x1cb = self.figure.cb_gridspec.get_grid_positions(
                self.figure.f
            )

            x0 = min(*x0, *x0cb)
            x1 = max(*x1, *x1cb)
            y0 = min(*y0, *y0cb)
            y1 = max(*y1, *y1cb)

        if size is None:
            size = abs(x1 - x0)

        if x is None:
            x = (x0 + x1) / 2
        if y is None:
            y = (y0 + y1) / 2

        self.figure.gridspec.update(
            left=x - size / 2,
            bottom=y - size / 2,
            right=x + size / 2,
            top=y + size / 2,
        )

        self.redraw()


class MapsGrid:
    """
    Initialize a grid of Maps objects

    Parameters
    ----------
    r : int, optional
        The number of rows. The default is 2.
    c : int, optional
        The number of columns. The default is 2.
    crs : int or a cartopy-projection, optional
        The projection that will be assigned to all Maps objects.
        (you can still change the projection of individual Maps objects later!)
        See the doc of "Maps" for details.
        The default is 4326.
    m_inits : dict, optional
        A dictionary that is used to customize the initialization the Maps-objects.

        The keys of the dictionaries are used as names for the Maps-objects,
        (accessible via `mgrid.m_<name>` or `mgrid[m_<name>]`) and the values are used to
        identify the position of the axes in the grid.

        Possible values are:
        - a tuple of (row, col)
        - an integer representing (row + col)

        Note: If either `m_inits` or `ax_inits` is provided, ONLY objects with the
        specified properties are initialized!

        The default is None in which case a unique Maps-object will be created
        for each grid-cell (accessible via `mgrid.m_<row>_<col>`)
    ax_inits : dict, optional
        Completely similar to `m_inits` but instead of `Maps` objects, ordinary
        matplotlib axes will be initialized. They are accessible via `mg.ax_<name>`.

        Note: If you iterate over the MapsGrid object, ONLY the initialized Maps
        objects will be returned!
    figsize : (float, float)
        The width and height of the figure.
    layer : int or str
        The default layer to assign to all Maps-objects of the grid.
        The default is 0.
    kwargs
        Additional keyword-arguments passed to the `matplotlib.gridspec.GridSpec()`
        function that is used to initialize the grid.

    Attributes
    ----------
    f : matplotlib.figure
        The matplotlib figure object
    gridspec : matplotlib.GridSpec
        The matplotlib GridSpec instance used to initialize the axes.
    m_<identifier> : eomaps.Maps objects
        The individual Maps-objects can be accessed via `mgrid.m_<identifier>`
        The identifiers are hereby `<row>_<col>` or the keys of the `m_inits`
        dictionary (if provided)
    ax_<identifier> : matplotlib.axes
        The individual (ordinary) matplotlib axes can be accessed via
        `mgrid.ax_<identifier>`. The identifiers are hereby the keys of the
        `ax_inits` dictionary (if provided).
        Note: if `ax_inits` is not specified, NO ordinary axes will be created!


    Methods
    -------
    join_limits :
        join the axis-limits of maps that share the same projection
    share_click_events :
        share click-callback events between the Maps-objects
    share_pick_events :
        share pick-callback events between the Maps-objects
    create_axes :
        create a new (ordinary) matplotlib axes
    add_<...> :
        call the underlying `add_<...>` method on all Maps-objects of the grid
    set_<...> :
        set the corresponding property on all Maps-objects of the grid
    subplots_adjust :
        Dynamically adjust the layout of the subplots, e.g:

        >>> mg.subplots_adjust(left=0.1, right=0.9,
        >>>                    top=0.8, bottom=0.1,
        >>>                    wspace=0.05, hspace=0.25)

    Examples
    --------
    To initialize a 2 by 2 grid with a large map on top, a small map
    on the bottom-left and an ordinary matplotlib plot on the bottom-right, use:

    >>> m_inits = dict(top = (0, slice(0, 2)),
    >>>                bottom_left=(1, 0))
    >>> ax_inits = dict(bottom_right=(1, 1))

    >>> mg = MapsGrid(2, 2, m_inits=m_inits, ax_inits=ax_inits)
    >>> mg.m_top.plot_map()
    >>> mg.m_bottom_left.plot_map()
    >>> mg.ax_bottom_right.plot([1,2,3])

    Returns
    -------
    eomaps.MapsGrid
        Accessor to the Maps objects "m_{row}_{column}".

    Notes
    -----

    - To perform actions on all Maps-objects of the grid, simply iterate over
      the MapsGrid object!
    """

    def __init__(
        self,
        r=2,
        c=2,
        crs=None,
        m_inits=None,
        ax_inits=None,
        figsize=None,
        layer=0,
        **kwargs,
    ):

        self._Maps = []
        self._names = defaultdict(list)

        self._wms_container = wms_container(self)

        gskwargs = dict(bottom=0.01, top=0.99, left=0.01, right=0.99)
        gskwargs.update(kwargs)
        self.gridspec = GridSpec(nrows=r, ncols=c, **gskwargs)

        if m_inits is None and ax_inits is None:
            if isinstance(crs, list):
                crs = np.array(crs).reshape((r, c))
            else:
                crs = np.broadcast_to(crs, (r, c))

            self._custom_init = False
            for i in range(r):
                for j in range(c):
                    crsij = crs[i, j]
                    if isinstance(crsij, np.generic):
                        crsij = crsij.item()

                    if i == 0 and j == 0:
                        # use crs[i, j].item() to convert to native python-types
                        # (instead of numpy-dtypes)  ... check numpy.ndarray.item
                        mij = Maps(
                            crs=crsij,
                            gs_ax=self.gridspec[0, 0],
                            figsize=figsize,
                            layer=layer,
                        )
                        self.parent = mij
                    else:
                        mij = Maps(
                            crs=crsij,
                            parent=self.parent,
                            gs_ax=self.gridspec[i, j],
                            layer=layer,
                        )

                    self._Maps.append(mij)
                    name = f"{i}_{j}"
                    self._names["Maps"].append(name)
                    setattr(self, "m_" + name, mij)
        else:
            self._custom_init = True
            if m_inits is not None:
                if not isinstance(crs, dict):
                    if isinstance(crs, np.generic):
                        crs = crs.item()

                    crs = {key: crs for key in m_inits}

                assert self._test_unique_str_keys(
                    m_inits
                ), "EOmaps: there are duplicated keys in m_inits!"

                for i, [key, val] in enumerate(m_inits.items()):
                    if ax_inits is not None:
                        q = set(m_inits).intersection(set(ax_inits))
                        assert (
                            len(q) == 0
                        ), f"You cannot provide duplicate keys! Check: {q}"

                    if i == 0:
                        mi = Maps(
                            crs=crs[key],
                            gs_ax=self.gridspec[val],
                            figsize=figsize,
                            layer=layer,
                        )
                        self.parent = mi
                    else:
                        mi = Maps(
                            crs=crs[key],
                            parent=self.parent,
                            gs_ax=self.gridspec[val],
                            layer=layer,
                        )

                    name = str(key)
                    self._names["Maps"].append(name)

                    self._Maps.append(mi)
                    setattr(self, f"m_{name}", mi)

            if ax_inits is not None:
                assert self._test_unique_str_keys(
                    ax_inits
                ), "EOmaps: there are duplicated keys in ax_inits!"
                for key, val in ax_inits.items():
                    self.create_axes(val, name=key)

    def new_layer(self, layer=None):
        if layer is None:
            layer = self.parent.layer

        mg = MapsGrid(m_inits=dict())  # initialize an empty MapsGrid
        mg.gridspec = self.gridspec

        for name, m in zip(self._names["Maps"], self._Maps):
            newm = m.new_layer(layer)
            mg._Maps.append(newm)
            mg._names["Maps"].append(name)
            setattr(mg, "m_" + name, newm)

            if m is self.parent:
                mg.parent = newm

        for name in self._names["Axes"]:
            ax = getattr(self, f"ax_{name}")
            mg._names["Axes"].append(name)
            setattr(mg, f"ax_{name}", ax)

        return mg

    def cleanup(self):
        for m in self:
            m.cleanup()

    @staticmethod
    def _test_unique_str_keys(x):
        # check if all keys are unique (as strings)
        seen = set()
        return not any(str(i) in seen or seen.add(str(i)) for i in x)

    def __iter__(self):
        return iter(self._Maps)

    def __getitem__(self, key):
        try:
            if self._custom_init is False:
                if isinstance(key, str):
                    r, c = map(int, key.split("_"))
                elif isinstance(key, (list, tuple)):
                    r, c = key
                else:
                    raise IndexError(f"{key} is not a valid indexer for MapsGrid")

                return getattr(self, f"m_{r}_{c}")
            else:
                if str(key) in self._names["Maps"]:
                    return getattr(self, "m_" + str(key))
                elif str(key) in self._names["Axes"]:
                    return getattr(self, "ax_" + str(key))
                else:
                    raise IndexError(f"{key} is not a valid indexer for MapsGrid")
        except:
            raise IndexError(f"{key} is not a valid indexer for MapsGrid")

    @property
    def _preferred_wms_service(self):
        return self.parent._preferred_wms_service

    def create_axes(self, ax_init, name=None):
        """
        Create (and return) an ordinary matplotlib axes.

        Note: If you intend to use both ordinary axes and Maps-objects, it is
        recommended to use explicit "m_inits" and "ax_inits" dicts in the
        initialization of the MapsGrid to avoid the creation of overlapping axes!

        Parameters
        ----------
        ax_init : set
            The GridSpec speciffications for the axis.
            use `ax_inits = (<row>, <col>)` to get an axis in a given grid-cell
            use `slice(<start>, <stop>)` for `<row>` or `<col>` to get an axis
            that spans over multiple rows/columns.

        Returns
        -------
        ax : matplotlib.axist
            The matplotlib axis instance

        Examples
        --------

        >>> ax_inits = dict(top = (0, slice(0, 2)),
        >>>                 bottom_left=(1, 0))

        >>> mg = MapsGrid(2, 2, ax_inits=ax_inits)
        >>> mg.m_top.plot_map()
        >>> mg.m_bottom_left.plot_map()

        >>> mg.create_axes((1, 1), name="bottom_right")
        >>> mg.ax_bottom_right.plot([1,2,3], [1,2,3])

        """

        if name is None:
            # get all existing axes
            axes = [key for key in self.__dict__ if key.startswith("ax_")]
            name = str(len(axes))
        else:
            assert (
                name.isidentifier()
            ), f"the provided name {name} is not a valid identifier"

        ax = self.f.add_subplot(self.gridspec[ax_init])

        self._names["Axes"].append(name)
        setattr(self, f"ax_{name}", ax)
        return ax

    _doc_prefix = (
        "This will execute the corresponding action on ALL Maps "
        + "objects of the MapsGrid!\n"
    )

    @property
    def children(self):
        return [i for i in self if i is not self.parent]

    @property
    def f(self):
        return self.parent.figure.f

    @wraps(Maps.plot_map)
    def plot_map(self, **kwargs):
        for m in self:
            m.plot_map(**kwargs)

    plot_map.__doc__ = _doc_prefix + plot_map.__doc__

    @property
    @lru_cache()
    @wraps(shapes)
    def set_shape(self):
        s = shapes(self)
        s.__doc__ = self._doc_prefix + s.__doc__

        return s

    @wraps(Maps.set_data_specs)
    def set_data_specs(self, *args, **kwargs):
        for m in self:
            m.set_data_specs(*args, **kwargs)

    set_data_specs.__doc__ = _doc_prefix + set_data_specs.__doc__

    set_data = set_data_specs

    @wraps(Maps.set_classify_specs)
    def set_classify_specs(self, scheme=None, **kwargs):
        for m in self:
            m.set_classify_specs(scheme=scheme, **kwargs)

    set_classify_specs.__doc__ = _doc_prefix + set_classify_specs.__doc__

    @wraps(Maps.add_annotation)
    def add_annotation(self, *args, **kwargs):
        for m in self:
            m.add_annotation(*args, **kwargs)

    add_annotation.__doc__ = _doc_prefix + add_annotation.__doc__

    @wraps(Maps.add_marker)
    def add_marker(self, *args, **kwargs):
        for m in self:
            m.add_marker(*args, **kwargs)

    add_marker.__doc__ = _doc_prefix + add_marker.__doc__

    if wms_container is not None:

        @property
        @wraps(Maps.add_wms)
        def add_wms(self):
            return self._wms_container

    @property
    @wraps(Maps.add_feature)
    def add_feature(self):
        x = NaturalEarth_features(self)
        return x

    @wraps(Maps.add_gdf)
    def add_gdf(self, *args, **kwargs):
        for m in self:
            m.add_gdf(*args, **kwargs)

    add_gdf.__doc__ = _doc_prefix + add_gdf.__doc__

    @wraps(Maps.add_line)
    def add_line(self, *args, **kwargs):
        for m in self:
            m.add_line(*args, **kwargs)

    add_line.__doc__ = _doc_prefix + add_line.__doc__

    @wraps(ScaleBar.__init__)
    def add_scalebar(self, *args, **kwargs):
        for m in self:
            m.add_scalebar(*args, **kwargs)

    add_scalebar.__doc__ = _doc_prefix + add_scalebar.__doc__

    @wraps(Maps.add_colorbar)
    def add_colorbar(self, *args, **kwargs):
        for m in self:
            m.add_colorbar(*args, **kwargs)

    add_colorbar.__doc__ = _doc_prefix + add_colorbar.__doc__

    @wraps(Maps.add_logo)
    def add_logo(self, *args, **kwargs):
        for m in self:
            m.add_logo(*args, **kwargs)

    add_colorbar.__doc__ = _doc_prefix + add_logo.__doc__

    def share_click_events(self):
        """
        Share click events between all Maps objects of the grid
        """
        self.parent.cb.click.share_events(*self.children)
        self.parent.cb._click_move.share_events(*self.children)

    def share_pick_events(self, name="default"):
        """
        Share pick events between all Maps objects of the grid
        """
        if name == "default":
            self.parent.cb.pick.share_events(*self.children)
        else:
            self.parent.cb.pick[name].share_events(*self.children)

    def join_limits(self):
        """
        Join axis limits between all Maps objects of the grid
        (only possible if all maps share the same crs!)
        """
        self.parent.join_limits(*self.children)

    @wraps(Maps.redraw)
    def redraw(self):
        self.parent.redraw()

    @wraps(plt.savefig)
    def savefig(self, *args, **kwargs):

        # clear all cached background layers before saving to make sure they
        # are re-drawn with the correct dpi-settings
        self.parent.BM._bg_layers = dict()

        self.f.savefig(*args, **kwargs)

    @property
    @wraps(Maps.util)
    def util(self):
        return self.parent.util

    @wraps(Maps.subplots_adjust)
    def subplots_adjust(self, **kwargs):
        return self.parent.subplots_adjust(**kwargs)

    @wraps(Maps.get_layout)
    def get_layout(self, *args, **kwargs):
        return self.parent.get_layout(*args, **kwargs)

    @wraps(Maps.apply_layout)
    def apply_layout(self, *args, **kwargs):
        return self.parent.apply_layout(*args, **kwargs)

    @wraps(Maps.edit_layout)
    def edit_layout(self, *args, **kwargs):
        return self.parent.edit_layout(*args, **kwargs)
