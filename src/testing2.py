import win32gui
import window

print([f"{win32gui.GetWindowText(w)}, {win32gui.GetClassName(w)}" for w in window.get_windows()])