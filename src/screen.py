import ctypes

def resolution():
    return (ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1))


class Screen:
    def __init__(self, resolution):
        self.resolution = resolution

    def test(self):
        pass
