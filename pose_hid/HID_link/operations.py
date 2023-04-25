import pyautogui

key_list = ["\t", "\n", "\r", " ", "!", """, "#", "$", "%", "&", """, "(", ")", "*", "+", ",", "-", ".", "/", "0", "1",
            "2", "3", "4", "5", "6", "7", "8", "9", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`",
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z", "{", "|", "}", "~", "accept", "add", "alt", "altleft", "altright", "apps",
            "backspace", "browserback", "browserfavorites", "browserforward", "browserhome", "browserrefresh",
            "browsersearch", "browserstop", "capslock", "clear", "convert", "ctrl", "ctrlleft", "ctrlright", "decimal",
            "del", "delete", "divide", "down", "end", "enter", "esc", "escape", "execute", "f1", "f10", "f11", "f12",
            "f13", "f14", "f15", "f16", "f17", "f18", "f19", "f2", "f20", "f21", "f22", "f23", "f24", "f3", "f4", "f5",
            "f6", "f7", "f8", "f9", "final", "fn", "hanguel", "hangul", "hanja", "help", "home", "insert", "junja",
            "kana", "kanji", "launchapp1", "launchapp2", "launchmail", "launchmediaselect", "left", "modechange",
            "multiply", "nexttrack", "nonconvert", "num0", "num1", "num2", "num3", "num4", "num5", "num6", "num7",
            "num8", "num9", "numlock", "pagedown", "pageup", "pause", "pgdn", "pgup", "playpause", "prevtrack", "print",
            "printscreen", "prntscrn", "prtsc", "prtscr", "return", "right", "scrolllock", "select", "separator",
            "shift", "shiftleft", "shiftright", "sleep", "space", "stop", "subtract", "tab", "up", "volumedown",
            "volumemute", "volumeup", "win", "winleft", "winright", "yen", "command", "option", "optionleft",
            "optionright"]


def reset_screen_location(x, y):
    if x < 0:
        x = 0
    if y < 0:
        y = 0
    if x > 1:
        x = 1
    if y > 1:
        y = 1
    return x, y


class Operations:
    """
    Encapsulates some pyautogui operations
    """

    def __init__(self, mouse_move_duration: float = 0.1,
                 secs_between_keys: float = 0.1,
                 default_interval: float = 0) -> None:
        self.screen_size = pyautogui.size()
        self.duration = mouse_move_duration
        self.key_duration = secs_between_keys
        self.interval = default_interval
        self.pressed_key = []
        self.pressed_mouse_button = []

    def one_key_press(self, key_name) -> None:
        if key_name not in key_list:
            raise KeyError("key_name not in key_list, config err")

        if key_name in self.pressed_key:
            pyautogui.keyUp(key_name)
            self.pressed_key.remove(key_name)

    def one_key_release(self, key_name) -> None:
        if key_name not in key_list:
            raise KeyError("key_name not in key_list, config err")

        if key_name not in self.pressed_key:
            pyautogui.keyDown(key_name)
            self.pressed_key.append(key_name)

    def keyboard_input(self, key_name_list: list) -> None:
        pyautogui.typewrite(key_name_list, interval=self.key_duration)

    @staticmethod
    def hotkey(hotkeys: tuple = ("ctrl", "c")) -> None:
        pyautogui.hotkey(*hotkeys)

    def mouse_move(self, x: float, y: float) -> None:
        x, y = reset_screen_location(x, y)
        w, h = self.screen_size
        x = int((w - 1) * x)
        y = int((h - 1) * y)
        pyautogui.moveTo(x, y, duration=self.duration)

    def mouse_click(self, x: float, y: float, click_time: int = 1, button: str = "left") -> None:
        x, y = reset_screen_location(x, y)
        w, h = self.screen_size
        x = int((w - 1) * x)
        y = int((h - 1) * y)
        pyautogui.click(x, y, click_time, interval=self.interval, duration=self.duration, button=button)

    def mouse_press(self, button: str = "left"):
        if button not in self.pressed_mouse_button:
            pyautogui.mouseDown(button=button)
            self.pressed_mouse_button.append(button)

    def mouse_release(self, button: str = "left"):
        if button in self.pressed_mouse_button:
            pyautogui.mouseUp(button=button)
            self.pressed_mouse_button.remove(button)
