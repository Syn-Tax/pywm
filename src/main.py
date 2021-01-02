import win32gui
import pyvda
import keyboard
import win32com
import workspace
import window
import callbacks
import config
import key
import time
from pynput import keyboard


def window_open_close_callback(hwnd, workspaces, open):
    if open:
        try:
            w = workspaces[pyvda.GetWindowDesktopNumber(hwnd)-1]
        except:
            w = workspace.get_current(workspaces)
        print(win32gui.GetWindowText(hwnd))
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


def prep_keys():
    for k in config.keys:
        k.set_index(config.keys)
        k.define_hotkey()


def set_keys():
    hks = {}
    for hotkey in config.keys:
        hk = ""
        for mod in hotkey.mods:
            hk += "<"+mod+">" + "+"
        if hotkey.key in key.mods:
            hk += "<"+hotkey.key+">"
        else:
            hk += hotkey.key
        hks |= {hk: lambda: hotkey.function(*hotkey.args)}
    print(hks)
    return keyboard.GlobalHotKeys(hks)

def main():
    # Check for newly opened and closed windows and re-establing layouts in those cases
    window_thread = callbacks.window_open_close(
        window_open_close_callback, config.window_delay, config.workspaces, config.window_ignore)

    # key_thread = set_keys()
    # key_thread.start()

    # # block the current thread so the program doesn't exit and other threads/processes can continue
    # key_thread.join()
    # prep_keys()
    for w in config.workspaces:
        w.set_workspaces(config.workspaces)

    while True:
        time.sleep(10)

if __name__ == "__main__":
    main()
