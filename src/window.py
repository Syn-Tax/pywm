import win32gui, win32con, win32com.client
import pyvda
import subprocess
import desktop
import workspace

def get_windows(window_ignore=[]):
    windows = []
    def callback(hwnd, _):
        if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) != "":
            try:
                if pyvda.GetWindowDesktopNumber(hwnd) and not win32gui.GetWindowText(hwnd) in window_ignore:
                    windows.append(hwnd)
            except:
                pass
    
    win32gui.EnumWindows(callback, None)

    return windows

def get_window_objects(workspaces, window_ignore=[]):
    windows = []
    for work in workspaces:
        for curr_win in work.stack:
            if not win32gui.GetWindowText(curr_win.hwnd) in window_ignore:
                windows.append(curr_win)
    
    return windows

def get_active_window(workspaces, window_ignore=[]):
    hwnd = win32gui.GetForegroundWindow()
    win = None
    for w in get_window_objects(workspaces, window_ignore=window_ignore):
        if w.hwnd == hwnd:
            win = w
    return win

def move_up_active(workspaces, window_ignore=[], wrap=True):
    w = get_active_window(workspaces, window_ignore=window_ignore)
    w.move_up(wrap=wrap)

def move_down_active(workspaces, window_ignore=[], wrap=True):
    w = get_active_window(workspaces, window_ignore=window_ignore)
    w.move_down(wrap=True)

def activate_up(workspaces, window_ignore=[], wrap=True):
    w = workspace.get_current(workspaces)
    active_window = get_active_window(workspaces, window_ignore=window_ignore)
    ind = w.stack.index(active_window)
    if wrap:
        w.stack[(ind-1) % len(w.stack)].focus()
    else:
        w.stack[ind-1].focus()

def activate_down(workspaces, window_ignore=[], wrap=True):
    w = workspace.get_current(workspaces)
    active_window = get_active_window(workspaces, window_ignore=window_ignore)
    ind = w.stack.index(active_window)
    if wrap:
        w.stack[(ind+1) % len(w.stack)].focus()
    else:
        w.stack[ind+1].focus()

class Window:
    def __init__(self, title, hwnd, work:workspace.Workspace):
        if title == None and hwnd == None:
            raise Warning("Cannot find window")
        elif hwnd == None:
            self.title = title
            self.hwnd = win32gui.FindWindow(None, title)
        elif title == None:
            self.title = win32gui.GetWindowText(hwnd)
            self.hwnd = hwnd

        self.work = work

    def maximize(self):
        win32gui.ShowWindow(self.hwnd, win32con.SW_MAXIMIZE)

    def minimize(self):
        win32gui.ShowWindow(self.hwnd, win32con.SW_MINIMIZE)

    def restore(self):
        win32gui.ShowWindow(self.hwnd, win32con.SW_NORMAL)
    
    def move(self, dx, dy, dw, dh):
        # (left, top, right, bottom)
        window_rect = win32gui.GetWindowRect(self.hwnd)

        width = window_rect[2] - window_rect[0]
        height = window_rect[3] - window_rect[1]

        new_x = window_rect[0]+dx
        new_y = window_rect[1]+dy
        new_width = width+dw
        new_height = height+dh

        self.restore()
        win32gui.MoveWindow(self.hwnd, new_x, new_y, new_width, new_height, 1)

    def place(self, x, y, w, h):
        self.restore()

        win32gui.MoveWindow(int(self.hwnd), int(x), int(y), int(w), int(h), 1)
    
    def get_desktop(self):
        return pyvda.GetWindowDesktopNumber(self.hwnd)-1
    
    def move_to_desktop(self, d, follow=False):
        if d > pyvda.GetDesktopCount():
            raise ValueError("That is not a valid desktop number")
        if d >= pyvda.GetDesktopCount():
            subprocess.call(f"VirtualDesktop /n:{d}")

        desktop.move_window(self.hwnd, d)

        if follow:
            desktop.focus(desktop)
    
    def focus(self):
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys('%')

        win32gui.SetForegroundWindow(self.hwnd)

    def move_up(self, wrap=True):
        ind = self.work.stack.index(self)
        if wrap:
            self.work.stack[(ind+1) % len(self.work.stack)], self.work.stack[ind] = self.work.stack[ind], self.work.stack[(ind+1) % len(self.work.stack)]

        else:
            self.work.stack[ind+1], self.work.stack[ind] = self.work.stack[ind], self.work.stack[ind+1]

        self.work.layout_windows()

    def move_down(self, wrap=True):
        ind = self.work.stack.index(self)
        if wrap:
            self.work.stack[(ind-1) % len(self.work.stack)], self.work.stack[ind] = self.work.stack[ind], self.work.stack[(ind-1) % len(self.work.stack)]
        else:
            self.work.stack[ind-1], self.work.stack[ind] = self.work.stack[ind], self.work.stack[ind-1]

        self.work.layout_windows()