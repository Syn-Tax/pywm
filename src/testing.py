import win32gui
import pyvda
import window

w = window.Window(win32gui.GetWindowText(win32gui.GetForegroundWindow()))

pyvda.GoToDesktopNumber(5)

print(w.get_desktop())
w.move_to_desktop(5, True)
print(w.get_desktop())