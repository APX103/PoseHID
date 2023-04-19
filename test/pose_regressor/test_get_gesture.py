import cv2
import json
from pose_hid.pose_regressor.get_gesture import FrameHandler


def test_get_gesture():
    fh = FrameHandler(task_path="./pose_hid/pose_regressor/gesture_recognizer.task")
    img = cv2.imread("./test/pose_regressor/test_double_hands.jpg")
    print(json.dumps(fh.get_gesture(img)))
