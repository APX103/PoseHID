# gesture define and map
# parse gesture from left hand to right hand
# left hand and right hand detect independently

# operation map
# TODO 写完这个文件，主要从config读取

import os
import json

ws = os.path.dirname(os.path.realpath(__file__)) + "/../.."


def parse_config(config_path: str = ws + '/config/config.json'):
    with open(config_path, 'r') as f:
        config = json.loads(f.read())
    return config


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

gesture_map = {

}
