import ctypes

def resolution():
    return (ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1))

def border():
    res = resolution()
    return (int((ctypes.windll.user32.GetSystemMetrics(61)-res[0])/2), int((ctypes.windll.user32.GetSystemMetrics(62)-res[1])/2))

def taskber():
    pas

class Screen:
    def __init__(self, resolution, border, bar):
        self.border = border
        self.bar = bar
        self.bar.set_screen(self)
        self.resolution = (resolution[0], resolution[1]-bar.height)
