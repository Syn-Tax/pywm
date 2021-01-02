import window
import multiprocessing
import time
import win32gui


def _window_open_close(callback, window_delay, workspaces, window_ignore):
    prev_windows = window.get_windows(window_ignore)
    time.sleep(window_delay)

    while True:
        current_windows = window.get_windows(window_ignore)

        # check for opened windows
        for w in current_windows:
            if not w in prev_windows:
                print(f"window open detected, {win32gui.GetWindowText(w)}")
                callback(w, workspaces, True)
                prev_windows = current_windows

        # check for closed windows
        for w in prev_windows:
            if not w in current_windows:
                print("window close detected")
                callback(w, workspaces, False)
                prev_windows = current_windows
        time.sleep(window_delay)


def window_open_close(callback, window_delay, workspaces, window_ignore):
    thread = multiprocessing.Process(target=_window_open_close, args=(
        callback, window_delay, workspaces, window_ignore))
    thread.start()
    # print("window_open_close thread started")
    return thread


def wait():
    while True:
        time.sleep(0.1)
