import sys
import time
import ctypes
import ctypes.wintypes
import win32gui
import pyvda

EVENT_OBJECT_SHOW = 0x8005
WINEVENT_OUTOFCONTEXT = 0x0000

user32 = ctypes.windll.user32
ole32 = ctypes.windll.ole32

ole32.CoInitialize(0)

WinEventProcType = ctypes.WINFUNCTYPE(
    None, 
    ctypes.wintypes.HANDLE,
    ctypes.wintypes.DWORD,
    ctypes.wintypes.HWND,
    ctypes.wintypes.LONG,
    ctypes.wintypes.LONG,
    ctypes.wintypes.DWORD,
    ctypes.wintypes.DWORD
)

def callback(hWinEventHook, event, hwnd, idObject, idChild, dwEventThread, dwmsEventTime):
    open_windows = []
    def c(handle, _):
        try:
            if pyvda.GetWindowDesktopNumber(handle):
                open_windows.append(handle)
        except:
            pass

    win32gui.EnumWindows(c, None)

    #print(open_windows)

    if hwnd in open_windows:
        print(win32gui.GetWindowText(hwnd))

WinEventProc = WinEventProcType(callback)

user32.SetWinEventHook.restype = ctypes.wintypes.HANDLE
hook = user32.SetWinEventHook(
    EVENT_OBJECT_SHOW,
    EVENT_OBJECT_SHOW,
    0,
    WinEventProc,
    0,
    0,
    WINEVENT_OUTOFCONTEXT
)
if hook == 0:
    print("setwinhook event failed")
    sys.exit(1)

msg = ctypes.wintypes.MSG()
while user32.GetMessageW(ctypes.byref(msg), 0, 0, 0) != 0:
    user32.TranslateMessageW(msg)
    user32.DispatchMessageW(msg)

user32.UnhookWinEvent(hook)
ole32.CoUninitialize()