import win32gui, pyvda, keyboard
import desktop, workspace, window, screen, layouts, callbacks, key, config
import sys
import time

def window_open_close_callback(w, workspaces, open):
    if open:
        workspace = workspaces[pyvda.GetWindowDesktopNumber(w)-1]

        workspace.add_window(window.Window(None, w, workspace))

        workspace.layout_windows()
        print(f"layed out workspace {pyvda.GetWindowDesktopNumber(w)-1}")
    else:
        curr_workspace = None
        win = None
        for work in workspaces:
            for curr_win in work.stack:
                if curr_win.win32 == w:
                    curr_workspace = work
                    win = curr_win
        
        if not curr_workspace or not win:
            raise Warning("Workspace/window shouldn't equal None")

        print(win.title)

        curr_workspace.remove_window(win)

        curr_workspace.layout_windows()
        print(f"layed out workspace {workspaces.index(curr_workspace)}")

def test(**kwargs):
    pass

def main():
    config.init()
    # Check for newly opened and closed windows and re-establing layouts in those cases
    # window_thread = callbacks.window_open_close(window_open_close_callback, config.window_delay, config.workspaces, config.window_ignore)

    k = key.Key(["ctrl", "shift"], "a", test)
    k.add_hotkeys()
    
    # keyboard.wait()

if __name__ == "__main__":
    main()