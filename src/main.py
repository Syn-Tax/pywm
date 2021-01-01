import win32gui, pyvda, keyboard, win32com
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

def start_bars():
    for s in config.screens:
        s.bar.start_process()

def main():
    # Check for newly opened and closed windows and re-establing layouts in those cases
    window_thread = callbacks.window_open_close(window_open_close_callback, config.window_delay, config.workspaces, config.window_ignore)

    # start bars on all screens
    hwnd = win32gui.GetForegroundWindow()
    start_bars()

    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('%')

    win32gui.SetForegroundWindow(hwnd)
    # block the current thread so the program doesn't exit and other threads/processes can continue
    keyboard.wait()
    

if __name__ == "__main__":
    main()