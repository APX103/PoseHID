import cv2
import time
import math
import numpy as np
from enum import Enum

import mediapipe as mp
from mediapipe.framework.formats import landmark_pb2
from mediapipe.tasks import python
from mediapipe.tasks.python import vision


class NormalizedLandmark(Enum):
    x = 1
    y = 2
    z = 3
    visibility = 4
    presence = 5


def gesture_templet() -> dict:
    return {
        "Imagesize": {
            "Height": None,
            "Width": None
        },
        "Handedness": {
            "Left": {
                "exist": False,
                "gesture": None,
                "confidence": None
            },
            "Right": {
                "exist": False,
                "gesture": None,
                "confidence": None
            },
        },
        "Landmark": {
            "Left": [],
            "Right": []
        },
        "Distance": {
            "Left/Dis_Thumb_Index_Tip": None,
            "Left/Dis_Thumb_Middle_Tip": None,
            "Right/Dis_Thumb_Index_Tip": None,
            "Right/Dis_Thumb_Middle_Tip": None,
            "Dis_Index_Index_Tip": None
        },
        "Angle": {
            "Left/Angle_Thumb_Index_Tip": None,
            "Right/Angle_Thumb_Index_Tip": None
        },
        "Process_time": 0.0
    }


class FrameHandler:
    def __init__(self, task_path: str = "gesture_recognizer.task") -> None:
        # gesture
        with open(task_path, "rb") as f:
            bf = f.read()
        base_options = python.BaseOptions(model_asset_buffer=bf)
        options = vision.GestureRecognizerOptions(base_options=base_options, num_hands=2)
        self.recognizer = vision.GestureRecognizer.create_from_options(options)

        # hands" landmark
        mp_hands = mp.solutions.hands
        self.hands = mp_hands.Hands(static_image_mode=True,
                                    max_num_hands=2,
                                    min_detection_confidence=0.4,
                                    min_tracking_confidence=0.5)

    def get_gesture(self, image: np.array) -> dict:
        """get gesture info from per frame

        Returns:
            dict: dict of hand landmark and etc. info
        """
        templet = gesture_templet()

        h, w = image.shape[0], image.shape[1]
        templet["Imagesize"]["Height"], templet["Imagesize"]["Width"] = h, w

        start_time = time.time()

        # flip
        img = cv2.flip(image, 1)

        # BGR 2 RGB
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        image = mp.Image(image_format=mp.ImageFormat.SRGB, data=img_rgb)

        recognition_result = self.recognizer.recognize(image)
        # we can use `recognizer.recognize_async(image, timestamp_ms=100)`to run a stream data

        # gestures" class and confidence
        top_gesture = recognition_result.gestures
        # handedness
        handedness = recognition_result.handedness
        # hand landmarks
        hand_landmarks = recognition_result.hand_landmarks

        # for each hand
        for i, hand_landmarkz in enumerate(hand_landmarks):
            handedness_str = handedness[i][0].category_name

            templet["Handedness"][handedness_str]["exist"] = True
            templet["Handedness"][handedness_str]["gesture"] = top_gesture[i][0].category_name
            templet["Handedness"][handedness_str]["confidence"] = top_gesture[i][0].score
            # templet["Landmark"][handedness_str] = hand_landmarkz
            templet["Landmark"][handedness_str] = [[i.x, i.y, i.z, i.visibility, i.presence] for i in hand_landmarkz]

            thumb_tip_x = int(hand_landmarkz[4].x * w)
            thumb_tip_y = int(hand_landmarkz[4].y * h)
            index_tip_x = int(hand_landmarkz[8].x * w)
            index_tip_y = int(hand_landmarkz[8].y * h)
            middle_tip_x = int(hand_landmarkz[12].x * w)
            middle_tip_y = int(hand_landmarkz[12].y * h)

            templet["Distance"][handedness_str + "/Dis_Thumb_Index_Tip"] = np.linalg.norm(
                [index_tip_x - thumb_tip_x, index_tip_y - thumb_tip_y])
            templet["Distance"][handedness_str + "/Dis_Thumb_Middle_Tip"] = np.linalg.norm(
                [middle_tip_x - thumb_tip_x, middle_tip_y - thumb_tip_y])
            templet["Angle"][handedness_str + "/Angle_Thumb_Index_Tip"] = math.atan2(index_tip_y - thumb_tip_y,
                                                                                   index_tip_x - thumb_tip_x)

            # TODO calculate angle

        # calculate distance between 2 index finger tip
        if templet["Handedness"]["Left"]["exist"] and templet["Handedness"]["Right"]["exist"]:
            templet["Distance"]["Dis_Index_Index_Tip"] = np.linalg.norm(
                [int((hand_landmarks[0][8].x - hand_landmarks[1][8].x) * w),
                 int((hand_landmarks[0][8].y - hand_landmarks[1][8].y) * h)])

        end_time = time.time()
        # count process time
        templet["Process_time"] = end_time - start_time

        return templet
