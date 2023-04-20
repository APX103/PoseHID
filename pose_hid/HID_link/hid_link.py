import pyautogui

key_list = ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2',
     '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c',
     'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
     '{', '|', '}', '~', 'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace', 'browserback',
     'browserfavorites', 'browserforward', 'browserhome', 'browserrefresh', 'browsersearch', 'browserstop', 'capslock',
     'clear', 'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete', 'divide', 'down', 'end', 'enter',
     'esc', 'escape', 'execute', 'f1', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2',
     'f20', 'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'final', 'fn', 'hanguel', 'hangul',
     'hanja', 'help', 'home', 'insert', 'junja', 'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
     'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack', 'nonconvert', 'num0', 'num1', 'num2', 'num3',
     'num4', 'num5', 'num6', 'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn', 'pgup',
     'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn', 'prtsc', 'prtscr', 'return', 'right', 'scrolllock',
     'select', 'separator', 'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab', 'up',
     'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen', 'command', 'option', 'optionleft',
     'optionright']


class HIDLinker:
    """
    Map config str to operations
    """

    def __init__(self, mouse_move_duration: float = 0.1, secs_between_keys: float = 0.1) -> None:
        self.duration = mouse_move_duration
        self.key_duration = secs_between_keys
        self.config = {}

    def parse_config(self) -> dict:
        pass

    def execute(self) -> None:
        pass

    def key_press(self) -> None:
        pass

    def key_combine(self) -> None:
        pass

    def mouse_move(self, x: int, y: int) -> None:
        pyautogui.moveTo(x, y, duration=self.duration)

    def mouse_click(self) -> None:
        pass

    def key_combine_and_mouse_move(self) -> None:
        pass


class HIDLinkerDirect(HIDLinker):
    def __init__(self):
        super().__init__()


class HIDLinkerBuffer(HIDLinker):
    def __init__(self):
        super().__init__()
