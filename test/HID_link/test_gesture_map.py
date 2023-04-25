import json

from pose_hid.HID_link.gesture_map import *


def test_gesture_map():
    config = parse_config()
    g_map = map_pose_method(config)
    print(json.dumps(g_map, sort_keys=True, indent=4))
