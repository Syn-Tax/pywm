import win32gui, pyvda, keyboard
import desktop, workspace, window, screen, layouts, callbacks, key, config
import sys
import time

def window_open_close_callback(hwnd, workspaces, open):
    if open:
        try:
            w = workspaces[pyvda.GetWindowDesktopNumber(hwnd)-1]
        except:
            w = workspace.get_current(workspaces)
        w.add_window(window.Window(None, hwnd, w))
        w.layout_windows()
    else:
        curr_workspace = None
        win = None
        for work in workspaces:
            for curr_win in work.stack:
                if curr_win.hwnd == hwnd:
                    curr_workspace = work
                    win = curr_win
        if not curr_workspace or not win:
            raise Warning("Workspace/window shouldn't equal None")
        curr_workspace.remove_window(win)
        curr_workspace.layout_windows()

def main():
    # Check for newly opened and closed windows and re-establing layouts in those cases
    window_thread = callbacks.window_open_close(window_open_close_callback, config.window_delay, config.workspaces, config.window_ignore)

    # block the current thread so the program doesn't exit
    keyboard.wait()
    

if __name__ == "__main__":
    main()