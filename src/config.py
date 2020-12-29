import screen, workspace, desktop, layouts, window
from key import *

screens = [screen.Screen(screen.resolution())]

window_ignore = ["Wox"]

workspaces = [workspace.Workspace(f"Desktop {i}", screens[0], layouts.MonadTall()) for i in range(desktop.count())]

keys = [
    # move windows in stack
    Key(["win", "shift"], "t", window.move_up_active, args=[workspaces, window_ignore]),
    Key(["win", "shift"], "h", window.move_down_active, args=[workspaces, window_ignore]),

    # change window focus
    Key(["win"], "t", window.activate_up, args=[workspaces, window_ignore]),
    Key(["win"], "h", window.activate_down, args=[workspaces, window_ignore]),

    # swap master & stack panes
    Key(["win"], "space", workspace.switch_current, args=[workspaces])
]

window_delay = 0.001

for i, workspace in enumerate(workspaces):
    workspace.stack = desktop.get_windows(workspaces, i)
