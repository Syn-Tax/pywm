import win32gui
import pyvda

def get_current(workspaces):
    return workspaces[pyvda.GetCurrentDesktopNumber()-1]

def switch_current(workspaces):
    w = get_current(workspaces)
    w.switch_stack()

class Workspace:
    def __init__(self, name, screen, layout, current_windows:list=[]):
        self.stack = current_windows
        self.layout = layout
        self.name = name
        self.screen = screen
    
    def add_window(self, window):
        self.stack.append(window)
    
    def remove_window(self, window):
        self.stack.remove(window)

    def layout_windows(self):
        # print([f"{w.hwnd}, {win32gui.GetWindowText(w.hwnd)}" for w in self.stack])
        self.layout.arrange(self.stack, self.screen)

    def change_layout(self, layout):
        self.layout = layout
        self.layout_windows()

    def get_active_window(self, window_ignore=[]):
        hwnd = win32gui.GetForegroundWindow()
        win = None
        for w in self.stack:
            if w.hwnd == hwnd and win32gui.GetWindowText(hwnd) not in window_ignore:
                win = w
        
        if not win:
            raise TypeError("Workspace is not active")
        return win

    def switch_stack(self):
        self.layout.switch(self.stack, self.screen)
