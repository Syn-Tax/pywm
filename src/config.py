import screen
import workspace
import desktop
import layouts
import window
import bar
from key import Key, win, shift
import subprocess
import win32gui

mod = win

screens = [screen.Screen(
    screen.resolution(), screen.border(), bar.Bar([], 30))]

window_ignore = [
    "Wox",
    "DesktopWindowXamlSource",  # some secondary window for wt that is always transparent
    "Bar"
]

border_window_classes = [
    "Chrome_WidgetWin_[0-9]",
]

border_window_ignore = [
    "Brave",
    "Chrome",
    "Atom"
]

wrap = True

workspaces = [workspace.Workspace(f"Desktop {i}", screens[0], layouts=[layouts.MonadTall(
    border_window_classes, border_window_ignore, margin=5), layouts.Monacle()]) for i in range(desktop.count())]
resize_step = 20

keys = [
    # move windows in stack
    Key([mod, shift], "t", window.move_up_active,
        args=[workspaces, window_ignore]),
    Key([mod, shift], "h", window.move_down_active,
        args=[workspaces, window_ignore]),

    # change window focus
    Key([mod], "t", window.activate_up, args=[workspaces, window_ignore]),
    Key([mod], "h", window.activate_down, args=[workspaces, window_ignore]),
    Key([mod, shift], "a", window.close_active, args=[workspaces, window_ignore]),

    # layout properties
    Key([mod], "space", workspace.switch_current, args=[workspaces]),
    Key([mod, shift], "space",
        workspace.cycle_current_layout, args=[workspaces]),

    # resize master & stack panes & margin
    Key([mod, shift], "left", workspace.resize_current,
        args=[workspaces, -resize_step]),
    Key([mod, shift], "right", workspace.resize_current,
        args=[workspaces, resize_step]),
    Key([mod, shift], "down", workspace.reset_scale, args=[workspaces]),

    # run programs
    Key([mod], "enter", subprocess.call, args=["wt"]),

    # layout current workspace
    Key([mod, shift], "l", workspace.layout_current, args=[workspaces])
]

window_delay = 0.05

for s in screens:
    s.bar.set_workspaces(workspaces)

for i, workspace in enumerate(workspaces):
    workspace.stack = desktop.get_windows(workspaces, i)
