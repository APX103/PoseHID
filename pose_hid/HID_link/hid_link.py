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
        if not self.lock_st:
            return
        w, h = pose_info["Landmark"]["Right"][12][0], pose_info["Landmark"]["Right"][12][1]
        operator.mouse_move(w, h)

    def mouse_press_left(self, pose_info: dict, thresh_hold: int = 30):
        if not self.lock_st:
            return
        dis_t_i = pose_info["Distance"]["Right/Dis_Thumb_Index_Tip"]
        if dis_t_i < thresh_hold and "left" not in operator.pressed_mouse_button:
            operator.mouse_press()
        elif dis_t_i > thresh_hold and "right" in operator.pressed_mouse_button:
            operator.mouse_release()

    def mouse_press_right(self, pose_info: dict, thresh_hold: int = 30):
        if not self.lock_st:
            return
        dis_t_m = pose_info["Distance"]["Right/Dis_Thumb_Middle_Tip"]
        if dis_t_m < thresh_hold and "right" not in operator.pressed_mouse_button:
            operator.mouse_press("right")
        elif dis_t_m > thresh_hold and "right" in operator.pressed_mouse_button:
            operator.mouse_release("right")

    def mouse_click_left(self, pose_info: dict, thresh_hold: int = 30):
        if not self.lock_st:
            return
        dis_t_i = pose_info["Distance"]["Right/Dis_Thumb_Index_Tip"]
        if dis_t_i < thresh_hold:
            w, h = pose_info["Landmark"]["Right"][12][0], pose_info["Landmark"]["Right"][12][1]
            operator.mouse_click(w, h)

    def mouse_click_right(self, pose_info: dict, thresh_hold: int = 30):
        if not self.lock_st:
            return
        dis_t_m = pose_info["Distance"]["Right/Dis_Thumb_Middle_Tip"]
        if dis_t_m < thresh_hold:
            w, h = pose_info["Landmark"]["Right"][12][0], pose_info["Landmark"]["Right"][12][1]
            operator.mouse_click(w, h, button="right")

    def lock(self):
        self.lock_st = False

    def unlock(self):
        self.lock_st = True

    def check_lock(self):
        return self.lock_st
