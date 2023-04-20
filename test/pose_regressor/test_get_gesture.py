import os
import cv2
import json
from pose_hid.pose_regressor.get_gesture import FrameHandler


def test_get_gesture():
    ws = os.path.dirname(os.path.realpath(__file__)) + "/../.."
    fh = FrameHandler(task_path=ws + "/pose_hid/pose_regressor/gesture_recognizer.task")
    img = cv2.imread(ws + "/test/pose_regressor/test_double_hands.jpg")
    print(json.dumps(fh.get_gesture(img)))
