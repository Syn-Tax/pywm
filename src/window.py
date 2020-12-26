import win32gui, win32con
import pyvda
import time

class Window:
    def __init__(self, title):
        self.title = title
        self.win32 = win32gui.FindWindow(None, title)

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

        win32gui.ShowWindow(self.win32, win32con.SW_NORMAL)
        win32gui.MoveWindow(self.win32, new_x, new_y, new_width, new_height, 1)
    
    def get_desktop(self):
        return pyvda.GetWindowDesktopNumber(self.win32)
    
    def move_to_desktop(self, desktop, follow=False):
        # if desktop > pyvda.GetDesktopCount():
        #     raise ValueError(f"{desktop} is not a valid desktop number (there are {pyvda.GetDesktopCount()} desktops)")

        pyvda.MoveWindowToDesktopNumber(self.win32, desktop)

        if follow:
            pyvda.GoToDesktopNumber(desktop)
