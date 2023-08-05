import wx
from wx import aui
from wx.aui import EVT_AUITOOLBAR_TOOL_DROPDOWN

from ..icons import (
    icons8_camera_50,
    icons8_connected_50,
    icons8_move_50,
    icons8_route_50,
)

ID_NAV = wx.NewId()
ID_CONTROLLER = wx.NewId()
ID_CAMERA = wx.NewId()
ID_CAMERA0 = wx.NewId()
ID_CAMERA1 = wx.NewId()
ID_CAMERA2 = wx.NewId()
ID_CAMERA3 = wx.NewId()
ID_CAMERA4 = wx.NewId()
ID_SPOOLER = wx.NewId()

_ = wx.GetTranslation


def register_control_tools(context, gui):
    toolbar = aui.AuiToolBar()

    toolbar.AddTool(
        ID_NAV,
        _("Navigation"),
        icons8_move_50.GetBitmap(),
        kind=wx.ITEM_NORMAL,
        short_help_string=_("Opens Navigation Window"),
    )
    toolbar.Bind(
        wx.EVT_TOOL,
        lambda v: context("window toggle Navigation\n"),
        id=ID_NAV,
    )
    if context.has_feature("modifier/Camera"):
        toolbar.AddTool(
            ID_CAMERA,
            _("Camera"),
            icons8_camera_50.GetBitmap(),
            kind=wx.ITEM_NORMAL,
            short_help_string=_("Opens Camera Window"),
        )

        def on_camera_click(event=None):
            eid = event.GetId()
            context.setting(int, "camera_default", 0)
            if eid == ID_CAMERA0:
                context.camera_default = 0
            elif eid == ID_CAMERA1:
                context.camera_default = 1
            elif eid == ID_CAMERA2:
                context.camera_default = 2
            elif eid == ID_CAMERA3:
                context.camera_default = 3
            elif eid == ID_CAMERA4:
                context.camera_default = 4

            v = context.camera_default
            context("window toggle -m {v} CameraInterface {v}\n".format(v=v))

        def on_camera_dropdown(event=None):
            if event.IsDropDownClicked():
                menu = wx.Menu()
                menu.Append(ID_CAMERA0, _("Camera %d") % 0)
                menu.Append(ID_CAMERA1, _("Camera %d") % 1)
                menu.Append(ID_CAMERA2, _("Camera %d") % 2)
                menu.Append(ID_CAMERA3, _("Camera %d") % 3)
                menu.Append(ID_CAMERA4, _("Camera %d") % 4)
                menu.Bind(wx.EVT_MENU, on_camera_click, id=ID_CAMERA0)
                menu.Bind(wx.EVT_MENU, on_camera_click, id=ID_CAMERA1)
                menu.Bind(wx.EVT_MENU, on_camera_click, id=ID_CAMERA2)
                menu.Bind(wx.EVT_MENU, on_camera_click, id=ID_CAMERA3)
                menu.Bind(wx.EVT_MENU, on_camera_click, id=ID_CAMERA4)
                gui.PopupMenu(menu)
            else:
                on_camera_click(event)
            toolbar.SetToolSticky(event.GetId(), False)

        toolbar.SetToolDropDown(ID_CAMERA, True)
        toolbar.Bind(
            EVT_AUITOOLBAR_TOOL_DROPDOWN,
            on_camera_dropdown,
            id=ID_CAMERA,
        )

    toolbar.AddTool(
        ID_SPOOLER,
        _("Spooler"),
        icons8_route_50.GetBitmap(),
        kind=wx.ITEM_NORMAL,
        short_help_string=_("Opens Spooler Window"),
    )
    toolbar.Bind(
        wx.EVT_TOOL,
        lambda v: context("window toggle JobSpooler\n"),
        id=ID_SPOOLER,
    )
    toolbar.AddTool(
        ID_CONTROLLER,
        _("Controller"),
        icons8_connected_50.GetBitmap(),
        kind=wx.ITEM_NORMAL,
        short_help_string=_("Opens Controller Window"),
    )
    toolbar.Bind(
        wx.EVT_TOOL,
        lambda v: context("window toggle -o Controller\n"),
        id=ID_CONTROLLER,
    )
    toolbar.Create(gui)

    pane = (
        aui.AuiPaneInfo()
        .Name("control_toolbar")
        .Top()
        .ToolbarPane()
        .FloatingSize(230, 58)
        .Layer(1)
        .Caption(_("Control"))
        .CaptionVisible(not context.pane_lock)
        .Hide()
    )
    pane.dock_proportion = 230
    pane.control = toolbar
    pane.submenu = _("Toolbars")
    gui.on_pane_add(pane)
    context.register("pane/control_toolbar", pane)

    return toolbar
