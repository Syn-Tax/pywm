import keyboard

win = "win"
ctrl = "ctrl"
shift = "shift"
alt = "alt"
# mods = ["up", "down", "left", "right", "enter"]

class Key:
    def __init__(self, mods, key, function, args=[], suppress=True):
        self.mods = mods
        self.key = key
        self.function = function
        self.args = args
        self.index = None
        self.hotkey = "+".join(self.mods)+f"+{self.key}"
        keyboard.add_hotkey(self.hotkey, self.function, args=self.args)

    def set_index(self, keys):
        self.index = keys.index(self)

    def define_hotkey(self):
        ahk = AHK()

        hk = "".join(self.mods)+self.key
        script = f"Run python hotkeys.py {self.index}, HIDE"
        hotkey = Hotkey(ahk, hk, script)
        hotkey.start()

