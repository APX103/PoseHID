from typing import Tuple

import cv2
import time
import numpy as np
from collections import Counter

from pose_hid.pose_regressor.get_gesture import FrameHandler
# from pose_hid.HID_link.gesture_map import


class PoseWindow:
    def __init__(self, window_size: int = 5):
        self.left_window = [None for i in range(0, window_size)]
        self.right_window = [None for i in range(0, window_size)]
        self.left_method = None
        self.right_method = []

    # TODO 修改方案，不再推手势，推方法
    def rolling(self, pose_info: dict) -> tuple[None, None]:
        self.left_window.pop(0)
        self.right_window.pop(0)
        self.left_window.append(pose_info["Handedness"]["Left"]["gesture"])
        self.left_window.append(pose_info["Handedness"]["Left"]["gesture"])

        # Get
        most_left = Counter(self.left_window).most_common(1)[0]
        most_right = Counter(self.right_window).most_common(1)[0]
        most_left_pose = most_left[0] if most_left[1] >= (len(self.left_window) / 2 + 1) else None
        most_right_pose = most_right[0] if most_right[1] >= (len(self.left_window) / 2 + 1) else None
        return most_left_pose, most_right_pose


def main(if_show_video: bool = False):
    pose_window = PoseWindow()
    frame_handler = FrameHandler('pose_hid/pose_regressor/gesture_recognizer.task')
    cap = cv2.VideoCapture(0)

    cap.open(0)
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            print('Capture image failed, Exit.\n')
            break
        if if_show_video:
            frame, pose_info = frame_handler.get_gesture_and_frame(frame)
            cv2.imshow('Pose_HID', frame)
            pass
        else:
            pose_info = frame_handler.get_gesture(frame)
        l_pose, r_pose = pose_window.rolling(pose_info)
        # TODO add slide for right hands func(like mouse movement)
        if l_pose:
            # TODO 具体的操作逻辑
            pass
        key_pressed = cv2.waitKey(60)
        if key_pressed in [ord('q'), 27]:
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    pass
