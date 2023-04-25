from pose_hid.HID_link.operations import Operations
from pose_hid.HID_link.gesture_map import parse_config, map_pose_method

operator = Operations()


class HIDLink:
    """
    PS: If a method activated(left hand), it will process in every frame(every frame out from slid window)
    """

    def __init__(self):
        self.lock_st = False
        self.mouse_activate = False
        self.mouse_press = False
        self.gesture_map = map_pose_method(parse_config())

    def mouse_move(self, pose_info: dict, thresh_hold: float = 1.2):
        if self.lock_st:
            return
        w, h = pose_info["Landmark"]["Right"][12][0], pose_info["Landmark"]["Right"][12][1]
        operator.mouse_move(w * thresh_hold, h * thresh_hold)

    def mouse_press_left(self, pose_info: dict, func: str, thresh_hold: int = 30):
        if self.lock_st:
            return
        dis_t_i = pose_info["Distance"][func]
        if dis_t_i < thresh_hold and "left" not in operator.pressed_mouse_button:
            operator.mouse_press()
        elif dis_t_i > thresh_hold and "right" in operator.pressed_mouse_button:
            operator.mouse_release()

    def mouse_press_right(self, pose_info: dict, func: str, thresh_hold: int = 30):
        if self.lock_st:
            return
        dis_t_m = pose_info["Distance"][func]
        if dis_t_m < thresh_hold and "right" not in operator.pressed_mouse_button:
            operator.mouse_press("right")
        elif dis_t_m > thresh_hold and "right" in operator.pressed_mouse_button:
            operator.mouse_release("right")

    def mouse_click_left(self, pose_info: dict, func: str, thresh_hold: int = 30):
        if self.lock_st:
            return
        dis_t_i = pose_info["Distance"][func]
        if dis_t_i < thresh_hold:
            w, h = pose_info["Landmark"]["Right"][12][0], pose_info["Landmark"]["Right"][12][1]
            operator.mouse_click(w, h)

    def mouse_click_right(self, pose_info: dict, func: str, thresh_hold: int = 30):
        if self.lock_st:
            return
        dis_t_m = pose_info["Distance"][func]
        if dis_t_m < thresh_hold:
            w, h = pose_info["Landmark"]["Right"][12][0], pose_info["Landmark"]["Right"][12][1]
            operator.mouse_click(w, h, button="right")

    def lock(self, pose_info: dict):
        if "lock" in self.gesture_map[pose_info["Handedness"]["Left"]["gesture"]] and \
                pose_info["Handedness"]["Right"]["gesture"] == self.gesture_map['lock'][0]:
            self.lock_st = True

    def unlock(self, pose_info: dict):
        if "unlock" in self.gesture_map[pose_info["Handedness"]["Left"]["gesture"]] and \
                pose_info["Handedness"]["Right"]["gesture"] == self.gesture_map['unlock'][0]:
            self.lock_st = False

    def check_lock(self):
        return self.lock_st

    def str2method(self):
        maps = {}
        for i in self.gesture_map:
            for j in self.gesture_map[i].keys():
                maps[j] = eval(f"self.{j}")
        return maps


