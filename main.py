from typing import Tuple
import argparse

import cv2
from collections import Counter

from pose_hid.HID_link.gesture_map import parse_config, map_pose_method
from pose_hid.pose_regressor.get_gesture import FrameHandler
from pose_hid.HID_link.hid_link import HIDLink


def parse_arg():
    parser = argparse.ArgumentParser("PoseHID Program. Control mouse with camera!!!")
    parser.add_argument("--show_window", action=argparse.BooleanOptionalAction, 
                        help="Set to False if there is no need to show camera output.")
    return parser.parse_args()


class PoseWindow:
    def __init__(self, window_size: int = 5):
        self.left_window = [None for i in range(0, window_size)]

    def rolling(self, pose_info: dict) -> str:
        self.left_window.pop(0)
        self.left_window.append(pose_info["Handedness"]["Left"]["gesture"])

        most_left = Counter(self.left_window).most_common(1)[0]
        most_left_pose = most_left[0] if most_left[1] >= (len(self.left_window) / 2 + 1) else None
        return most_left_pose


def exec_method(method_map: dict, pose_info: dict, method_name: str, params: list):
    method_map[method_name](pose_info, *params)


def main(if_show_video: bool = False) -> None:
    pose_window = PoseWindow()
    gesture_map = map_pose_method(parse_config())
    hid_link = HIDLink()
    method_map = hid_link.str2method()
    frame_handler = FrameHandler('pose_hid/pose_regressor/gesture_recognizer.task')
    cap = cv2.VideoCapture(0)
    cap.open(0)
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            print('Capture image failed, Exit.\n')
            break
        if if_show_video:
            print("show windows")
            frame, pose_info = frame_handler.get_gesture_and_frame(frame)
            cv2.imshow('Pose_HID', frame)
            pass
        else:
            pose_info = frame_handler.get_gesture(frame)
        l_pose = pose_window.rolling(pose_info)
        # TODO add slide for right hands func(like mouse movement)
        if l_pose != "None" and l_pose and pose_info["Handedness"]["Left"]["gesture"] != "None":
            for k, v in gesture_map["Left/" + l_pose].items():
                exec_method(method_map, pose_info, k, v)
        key_pressed = cv2.waitKey(60)
        if key_pressed in [ord('q'), 27]:
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    args = parse_arg()
    main(args.show_window)
