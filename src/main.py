import win32gui, pyvda, pygetwindow
import desktop, workspace, window, screen, layouts
import sys
import time

screens = [screen.Screen(1920, 1080)]

workspaces = [workspace.Workspace(f"Desktop {i}", screens[0], layouts.MonadTall(), desktop.get_windows(i)) for i in range(desktop.count())]

#workspaces[2].layout_windows()

prev_windows = window.get_windows()
time.sleep(0.1)

while True:
    current_windows = window.get_windows()

    print(current_windows)

    for w in current_windows:
        if not w in prev_windows:
            print("new window detected")
            workspaces[pyvda.GetWindowDesktopNumber(w)-1].layout_windows()
            prev_windows = current_windows
    time.sleep(0.1)
