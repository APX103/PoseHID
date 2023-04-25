# gesture define and map
# parse gesture from left hand to right hand
# left hand and right hand detect independently

# parse log
# map operation

import os
import yaml

ws = os.path.dirname(os.path.realpath(__file__)) + "/../.."


def parse_config(config_path: str = ws + '/config/config.yml') -> dict:
    with open(config_path, 'r') as f:
        config = yaml.load(f.read(), yaml.FullLoader)
    return config


# Update this if add new pose into model
g = [
    "None",
    "Closed_Fist",
    "Open_Palm",
    "Pointing_Up",
    "Thumb_Down",
    "Thumb_Up",
    "Victory",
    "ILoveYou",
]

lg = ["Left/" + i for i in g if i != "None"]
rg = ["Right/" + i for i in g if i != "None"]

gesture_map = {i: {} for i in lg}


def map_pose_method(config: dict) -> dict:
    for k, v in config.items():
        k = [k] if "+" not in k else k.split("+")
        v = [v] if "|" not in v else v.split("|")
        if len(k) == 1:
            gesture_map[k[0]][v[0]] = v[1:]
            continue
        gesture_map[k[0]][v[0]] = [k[1], *v[1:]]
    return gesture_map
