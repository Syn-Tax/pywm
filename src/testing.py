import win32gui
import pyvda
import window, stack

w = window.Window(win32gui.GetWindowText(win32gui.GetForegroundWindow()))

s = stack.Stack([w])

print(s.windows)