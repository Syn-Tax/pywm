import win32gui, pyvda, pygetwindow
import desktop, workspace, window, screen, layouts
import sys
import time

window_delay = 0.001

screens = [screen.Screen(1920, 1080)]

workspaces = [workspace.Workspace(f"Desktop {i}", screens[0], layouts.MonadTall(), desktop.get_windows(i)) for i in range(desktop.count())]

#workspaces[2].layout_windows()

# Check for newly opened and closed windows and re-establing layouts in those cases

prev_windows = window.get_windows()
time.sleep(window_delay)

while True:
    current_windows = window.get_windows()

    # check for opened windows
    for w in current_windows:
        if not w in prev_windows:
            print("new window detected")
            workspace = workspaces[pyvda.GetWindowDesktopNumber(w)-1]

            workspace.add_window(window.Window(None, w, workspace))

            workspace.layout_windows()
            print(f"layed out workspace {pyvda.GetWindowDesktopNumber(w)-1}")
            prev_windows = current_windows

    # check for closed windows
    for w in prev_windows:
        if not w in current_windows:
            print("window close detected")
            curr_workspace = None
            win = None
            for work in workspaces:
                for curr_win in work.stack:
                    if curr_win.win32 == w:
                        curr_workspace = work
                        win = curr_win
            
            if not curr_workspace or not win:
                raise Warning("Workspace/window shouldn't equal None")

            curr_workspace.remove_window(win)

            curr_workspace.layout_windows()
            prev_windows = current_windows
    time.sleep(window_delay)