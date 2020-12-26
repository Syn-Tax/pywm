import win32gui
import window
import sys

w = window.Window(win32gui.GetWindowText(win32gui.GetForegroundWindow()))

w.move(150, 150, -300, -300)