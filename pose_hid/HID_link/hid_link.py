import pyautogui


class HIDLinker:
    """
    combine config str to operations
    """
    def __init__(self) -> None:
        self.config = {}

    def parse_config(self) -> dict:
        pass

    def execute(self) -> None:
        pass

    def key_press(self) -> None:
        pass

    def key_combine(self) -> None:
        pass

    def mouse_move(self) -> None:
        pass

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
