import win32gui
import pyvda
import re


def get_current(workspaces):
    return workspaces[pyvda.GetCurrentDesktopNumber()-1]


def switch_current(workspaces):
    w = get_current(workspaces)
    w.switch_stack()


def resize_current(step, workspaces):
    step = int(step)
    w = get_current(workspaces)
    w.layout.scale += step
    w.layout_windows()


def reset_scale(workspaces):
    w = get_current(workspaces)
    w.layout.scale = 0
    w.layout_windows()


def resize_current_margins(step, workspaces):
    step = int(step)
    w = get_current(workspaces)
    w.layout.margin += step
    w.layout_windows()


def layout_current(workspaces):
    w = get_current(workspaces)
    w.layout_windows()


def cycle_current_layout(workspaces):
    w = get_current(workspaces)
    w.cycle_layout()


class Workspace:
    def __init__(self, name, screen, layouts: list, current_windows: list = []):
        self.stack = current_windows
        self.layouts = layouts
        self.layout = layouts[0]
        self.name = name
        self.screen = screen
        self.workspaces = None

    def add_window(self, window):
        self.stack.append(window)

    def remove_window(self, window):
        self.stack.remove(window)

    def set_workspaces(self, workspaces):
        self.workspaces = workspaces

    def layout_windows(self, window_ignore=[]):
        print([f"{w.hwnd}, {win32gui.GetWindowText(w.hwnd)}" for w in self.stack])

        # titles = [w.title for w in self.stack]
        #
        # if any([re.findall("|".join(window_ignore), title) for title in titles]):
        #     self.clean_stack(window_ignore)

        self.layout.arrange(self.stack, self.screen, self.workspaces,
                            window_ignore=window_ignore)

    def cycle_layout(self):
        ind = self.layouts.index(self.layout)
        self.layout = self.layouts[(ind+1) % len(self.layouts)]
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

    def clean_stack(self, window_ignore):
        new_stack = []

        for w in self.stack:
            if not re.findall("|".join(window_ignore), w.title):
                new_stack.append(w)

        self.stack = new_stack


if __name__ == '__main__':
    globals()[sys.argv[1]](*sys.argv[2::])
