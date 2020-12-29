import keyboard

class Key:
    def __init__(self, mods, key, function, args=[], suppress=False):
        self.mods = mods
        self.key = key
        self.function = function
        self.args = args
        self.hotkey = "+".join(mods) + f"+{key}"
        keyboard.add_hotkey(self.hotkey, function, args, suppress=suppress)
    