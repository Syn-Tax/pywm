import win32gui
import pyvda
import window

class Workspace:
    def __init__(self, name, screen, layout, current_windows:list=[]):
        self.stack = current_windows
        self.layout = layout
        self.name = name
        self.screen = screen
    
    def add_window(self, window):
       self.stack.append(window)

    def layout_windows(self):
        self.layout.arrange(self.stack, self.screen)
