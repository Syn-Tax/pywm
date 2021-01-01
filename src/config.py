import screen, workspace, desktop, layouts, window, bar
from key import *
import subprocess

screens = [screen.Screen(screen.resolution(), screen.border(), bar.Bar([], 20))]

window_ignore = [   
    "Wox",
    "DesktopWindowXamlSource", # some secondary window for wt that is always transparent
    "Bar"
]

border_window_classes = [
    "Chrome_WidgetWin_[0-9]",
]

border_window_ignore = [
    "Brave",
    "Chrome"
]

workspaces = [workspace.Workspace(f"Desktop {i}", screens[0], layouts=[layouts.MonadTall(border_window_classes, border_window_ignore), layouts.Monacle()]) for i in range(desktop.count())]
resize_step = 20

keys = [
    # move windows in stack
    Key(["win", "shift"], "t", window.move_up_active, args=[workspaces, window_ignore]),
    Key(["win", "shift"], "h", window.move_down_active, args=[workspaces, window_ignore]),

    # change window focus
    Key(["win"], "t", window.activate_up, args=[workspaces, window_ignore]),
    Key(["win"], "h", window.activate_down, args=[workspaces, window_ignore]),

    # layout properties
    Key(["win"], "space", workspace.switch_current, args=[workspaces]),
    Key(["win", "shift"], "space", workspace.cycle_current_layout, args=[workspaces]),

    # resize master & stack panes & margin
    Key(["win", "shift"], "left", workspace.resize_current, args=[workspaces, -resize_step]),
    Key(["win", "shift"], "right", workspace.resize_current, args=[workspaces, resize_step]),
    Key(["win", "shift"], "down", workspace.reset_scale, args=[workspaces]),

    # run programs
    Key(["win"], "enter", subprocess.call, args=["wt"]),

    # layout current workspace
    Key(["win", "shift"], "l", workspace.layout_current, args=[workspaces])
]

window_delay = 0.001

for s in screens:
    s.bar.set_workspaces(workspaces)

for i, workspace in enumerate(workspaces):
    workspace.stack = desktop.get_windows(workspaces, i)
