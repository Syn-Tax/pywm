import ctypes

def resolution():
    return (ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1))

def border():
    res = resolution()
    return (int((ctypes.windll.user32.GetSystemMetrics(61)-res[0])/2), int((ctypes.windll.user32.GetSystemMetrics(62)-res[1])/2))

class Screen:
    def __init__(self, resolution, border):
        self.resolution = resolution
        self.border = border
