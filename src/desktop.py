import win32gui
import pyvda
import subprocess

def focus(desktop):
    if desktop > pyvda.GetDesktopCount():
        subprocess.call("VirtualDesktop /n")

    pyvda.GoToDesktopNumber(desktop)