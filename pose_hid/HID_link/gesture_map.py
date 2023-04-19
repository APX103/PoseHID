# gesture define and map
# parse gesture from left hand to right hand
# left hand and right hand detect independently

# operation map
# TODO 写完这个文件，主要从config读取

import sys
import json

sys.path.append("./")

with open('../../config/config.json', 'r') as f:
    config = json.loads(f.read())

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

lg = ["Left_" + i for i in g if i != "None"]
rg = ["Right_" + i for i in g if i != "None"]

gesture_map = {
    
}

