import keyboard

class Key:
    def __init__(self, mods, key, function, args=[]):
        self.mods = mods
        self.key = key
        self.function = function
        self.args = args
    
    def add_hotkeys(self):
        hotkey = "+".join(self.mods) + f"+{self.key}"
        keyboard.add_hotkey(hotkey, self.function, self.args)