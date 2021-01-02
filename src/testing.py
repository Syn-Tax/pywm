import win32gui, win32ui, win32api, win32con
from win32api import GetSystemMetrics

dc = win32gui.GetDC(0)
dcObj = win32ui.CreateDCFromHandle(dc)
hwnd = win32gui.WindowFromPoint((0,0))
monitor = (0, 0, GetSystemMetrics(0), GetSystemMetrics(1))

red = win32api.RGB(255, 0, 0) # Red

past_coordinates = monitor
while True:
    m = win32gui.GetCursorPos()

    rect = win32gui.CreateRoundRectRgn(*past_coordinates, 2 , 2)
    win32gui.RedrawWindow(hwnd, past_coordinates, rect, win32con.RDW_INVALIDATE)

    for x in range(100):
        win32gui.SetPixel(dc, 100+x, 100, red)
        win32gui.SetPixel(dc, 100+x, 100+100, red)
        for y in range(100):
            win32gui.SetPixel(dc, 100, 100+y, red)
            win32gui.SetPixel(dc, 100+100, 100+y, red)

    past_coordinates = (m[0]-20, m[1]-20, m[0]+20, m[1]+20)
