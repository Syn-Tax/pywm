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
    
    def remove_window(self, window):
        self.stack.remove(window)

    def layout_windows(self):
        print([f"{w.win32}, {win32gui.GetWindowText(w.win32)}" for w in self.stack])
        self.layout.arrange(self.stack, self.screen)

    def change_layout(self, layout):
        self.layout = layout
        self.layout_windows()
