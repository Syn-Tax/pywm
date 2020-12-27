import win32gui, pyvda, pygetwindow
import desktop, workspace, window

workspaces = [workspace.Workspace(desktop.get_windows(i), None) for i in range(desktop.count())]

for w in workspaces:
    print([win32gui.GetWindowText(s) for s in w.stack])
#print([win32gui.GetWindowText(hwnd) for hwnd in desktop.get_windows(3)])