import cv2
import os
from pose_hid.HID_link.hid_link import HIDLink
from pose_hid.pose_regressor.get_gesture import FrameHandler


def test_full_process():
    hid_link = HIDLink()
    ws = os.path.dirname(os.path.realpath(__file__)) + "/../.."
    fh = FrameHandler(task_path=ws + "/pose_hid/pose_regressor/gesture_recognizer.task")
    img = cv2.imread(ws + "/test/pose_regressor/test_double_hands.jpg")
    pose_info = fh.get_gesture(img)

    # hid_link.lock(pose_info)
    # hid_link.mouse_move(pose_info)
    # hid_link.unlock(pose_info)
    hid_link.mouse_move(pose_info)
    # hid_link.mouse_press_right(pose_info, "Right/Dis_Thumb_Middle_Tip")
    # hid_link.mouse_press_right(pose_info, "Right/Dis_Thumb_Middle_Tip", 100)
    # hid_link.mouse_press_right(pose_info, "Right/Dis_Thumb_Middle_Tip")


def test_method_map():
    hid_link = HIDLink()
    print(hid_link.str2method())
