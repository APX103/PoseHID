import cv2
import time
import numpy as np
from PIL import Image

import mediapipe as mp
from mediapipe.framework.formats import landmark_pb2
from mediapipe.tasks import python
from mediapipe.tasks.python import vision


class frame_handler:
    def __init__(self) -> None:
        # gesture
        base_options = python.BaseOptions(model_asset_path='gesture_recognizer.task')
        options = vision.GestureRecognizerOptions(base_options=base_options, num_hands=2)
        self.recognizer = vision.GestureRecognizer.create_from_options(options)
        
        
        # hands' landmark
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
        h, w = image.shape[0], image.shape[1]
        
        start_time = time.time()
        
        # flip
        img = cv2.flip(img, 1)
        
        # BGR 2 RGB
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        image = mp.Image(image_format=mp.ImageFormat.SRGB, data=img_rgb)
        
        recognition_result = self.recognizer.recognize(image)
        # we can use `recognizer.recognize_async(image, timestamp_ms=100)`to run a stream data
        
        # gestures' class and confidence
        top_gesture = recognition_result.gestures
        # handness
        handness = recognition_result.handness
        # hand landmarks
        hand_landmarks = recognition_result.hand_landmarks
        
        img = image.numpy_view()
        
        # for each hand
        for i in range(len(hand_landmarks)):
            id_str = str(i+1)
            handness_str = handness[i][0].category_name
            gesture_str = top_gesture[i][0].category_name
            confidence = '{:.2f}'.format(top_gesture[i][0].score)
        
            # TODO 改完
            for hand_landmarks in hand_landmarks:
                hand_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
                hand_landmarks_proto.landmark.extend([landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in hand_landmarks])
            
            # TODO fix this
            hand_idx = 0
            hand_21 = results.multi_hand_landmarks[hand_idx]

            index_tip_x = int(hand_21.landmark[4].x * w)
            index_tip_y = int(hand_21.landmark[4].y * h)

            thumb_tip_x = int(hand_21.landmark[8].x * w)
            thumb_tip_y = int(hand_21.landmark[8].y * h)

            distance = np.linalg.norm(
                [index_tip_x-thumb_tip_x, index_tip_y-thumb_tip_y])

        end_time = time.time()
        # count process time
        process_time = end_time - start_time
    
        img = img[:,:,::-1] # RGB 2 BGR

        return {}
