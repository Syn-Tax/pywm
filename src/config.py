import screen, workspace, desktop, layouts
from keys import *

keys = [
    Key(["win", "shift"], "t", window.move_up_active())
]

window_delay = 0.001

screens = [screen.Screen(screen.resolution())]

window_ignore = ["Wox"]

workspaces = [workspace.Workspace(f"Desktop {i}", screens[0], layouts.MonadTall()) for i in range(desktop.count())]

def init():
    print("running init")
    for i, workspace in enumerate(workspaces):
        print("in loop")
        workspace.stack = desktop.get_windows(workspaces, i)