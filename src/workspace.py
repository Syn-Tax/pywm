import win32gui
import pyvda
import window

class Workspace:
    def __init__(self, current_windows:list, layout):
        self.stack = current_windows
        self.layout = layout
    
    def add_window(self, window):
       self.stack.append(window)
