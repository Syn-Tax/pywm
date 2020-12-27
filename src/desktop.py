import win32gui
import pyvda
import subprocess
import pygetwindow

def focus(desktop):
    if desktop >= pyvda.GetDesktopCount():
        subprocess.call("VirtualDesktop /n")

    pyvda.GoToDesktopNumber(desktop+1)

def create():
    subprocess.call("VirtualDesktop /n")

def remove(desktop):
    subprocess.call(f"VirtualDesktop /r:{desktop-1}")

def count():
    return pyvda.GetDesktopCount()

def move_window(hwnd, desktop):
    pyvda.MoveWindowToDesktopNumber(hwnd, desktop+1)

def get_windows(desktop):
    windows = []
    def callback(hwnd, _):
        if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) != "":
            try:
                if pyvda.GetWindowDesktopNumber(hwnd) == desktop+1:
                    windows.append(hwnd)
            except:
                pass
    
    win32gui.EnumWindows(callback, None)

    return windows