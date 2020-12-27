import win32gui, win32con
import pyvda
import subprocess
import desktop

def get_windows():
    windows = []
    def callback(hwnd, _):
        if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) != "":
            try:
                if pyvda.GetWindowDesktopNumber(hwnd):
                    windows.append(window.Window(None, hwnd, desktop))
            except:
                pass
    
    win32gui.EnumWindows(callback, None)

    return windows

class Window:
    def __init__(self, title, hwnd, workspace):
        if title == None and hwnd == None:
            raise Warning("Cannot find window")
        elif hwnd == None:
            self.title = title
            self.win32 = win32gui.FindWindow(None, title)
        elif title == None:
            self.title = win32gui.GetWindowText(hwnd)
            self.win32 = hwnd

        self.workspace = workspace

    def maximise(self):
        win32gui.ShowWindow(self.win32, win32con.SW_MAXIMIZE)

    def minimize(self):
        win32gui.ShowWindow(self.win32, win32con.SW_MINIMIZE)

    def restore(self):
        win32gui.ShowWindow(self.win32, win32con.SW_NORMAL)
    
    def move(self, dx, dy, dw, dh):
        # (left, top, right, bottom)
        window_rect = win32gui.GetWindowRect(self.win32)

        width = window_rect[2] - window_rect[0]
        height = window_rect[3] - window_rect[1]

        new_x = window_rect[0]+dx
        new_y = window_rect[1]+dy
        new_width = width+dw
        new_height = height+dh

        self.restore()
        win32gui.MoveWindow(self.win32, new_x, new_y, new_width, new_height, 1)

    def place(self, x, y, w, h):
        self.restore()

        win32gui.MoveWindow(int(self.win32), int(x), int(y), int(w), int(h), 1)
    
    def get_desktop(self):
        return pyvda.GetWindowDesktopNumber(self.win32)-1
    
    def move_to_desktop(self, d, follow=False):
        if d > pyvda.GetDesktopCount():
            raise ValueError("That is not a valid desktop number")
        if d >= pyvda.GetDesktopCount():
            subprocess.call(f"VirtualDesktop /n:{d}")

        desktop.move_window(self.win32, d)

        if follow:
            desktop.focus(desktop)
