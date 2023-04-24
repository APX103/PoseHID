import numpy as np

from pose_hid.pose_regressor.get_gesture import FrameHandler


class PoseWindow:
    def __init__(self, window_size: int = 15):
        self.left_window = [None for i in range(0, window_size)]
        self.right_window = [None for i in range(0, window_size)]
        self.left_method = None
        self.right_method = []

    def rolling(self, pose_info: dict) -> (str, str):
        self.left_window.pop(0)
        self.right_window.pop(0)
        self.left_window.append(pose_info["Handedness"]["Left"]["gesture"])
        self.left_window.append(pose_info["Handedness"]["Left"]["gesture"])
        # TODO 需要完成返回当前命令的步骤，预计是滑窗中超过一半(8)的同样姿势就算这个姿势

