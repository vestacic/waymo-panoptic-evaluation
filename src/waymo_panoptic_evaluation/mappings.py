ADE20K_TO_WAYMO = {
    0: 0,  # wall
    1: 19,  # building
    2: 25,  # sky
    3: 26,  # floor → ground
    4: 24,  # tree → vegetation
    5: 0,  # ceiling
    6: 20,  # road
    7: 0,  # bed
    8: 0,  # windowpane
    9: 24,  # grass → vegetation
    10: 0,  # cabinet
    11: 23,  # sidewalk
    12: 9,  # person → pedestrian
    13: 26,  # earth → ground
    14: 0,  # door
    15: 0,  # table
    16: 24,  # mountain → vegetation
    17: 24,  # plant → vegetation
    18: 0,  # curtain
    19: 0,  # chair
    20: 2,  # car
    21: 0,  # water
    22: 0,  # painting
    23: 0,  # sofa
    24: 0,  # shelf
    25: 19,  # house → building
    26: 0,  # sea
    27: 0,  # mirror
    28: 0,  # rug
    29: 26,  # field → ground
    30: 0,  # armchair
    31: 0,  # seat
    32: 0,  # fence
    33: 0,  # desk
    34: 26,  # rock → ground
    35: 0,  # wardrobe
    36: 0,  # lamp
    37: 0,  # bathtub
    38: 0,  # railing
    39: 0,  # cushion
    40: 0,  # base
    41: 0,  # box
    42: 15,  # column → pole
    43: 17,  # signboard → sign
    44: 0,  # chest of drawers
    45: 0,  # counter
    46: 26,  # sand → ground
    47: 0,  # sink
    48: 19,  # skyscraper → building
    49: 0,  # fireplace
    50: 0,  # refrigerator
    51: 0,  # grandstand
    52: 20,  # path → road
    53: 0,  # stairs
    54: 20,  # runway → road
    55: 0,  # case
    56: 0,  # pool table
    57: 0,  # pillow
    58: 0,  # screen door
    59: 0,  # stairway
    60: 0,  # river
    61: 0,  # bridge
    62: 0,  # bookcase
    63: 0,  # blind
    64: 0,  # coffee table
    65: 0,  # toilet
    66: 24,  # flower → vegetation
    67: 0,  # book
    68: 24,  # hill → vegetation
    69: 0,  # bench
    70: 0,  # countertop
    71: 0,  # stove
    72: 24,  # palm → vegetation
    73: 0,  # kitchen island
    74: 0,  # computer
    75: 0,  # swivel chair
    76: 3,  # boat → truck (best effort, maybe other large vehicle)
    77: 0,  # bar
    78: 0,  # arcade machine
    79: 19,  # hovel → building
    80: 4,  # bus
    81: 0,  # towel
    82: 0,  # light
    83: 3,  # truck
    84: 19,  # tower → building
    85: 0,  # chandelier
    86: 0,  # awning
    87: 18,  # streetlight → traffic light
    88: 0,  # booth
    89: 0,  # television
    90: 90,  # airplane (Waymo doesn't include 90; consider ignore or TYPE_OTHER_LARGE_VEHICLE)
    91: 26,  # dirt track → ground
    92: 0,  # apparel
    93: 15,  # pole
    94: 26,  # land → ground
    95: 0,  # bannister
    96: 0,  # escalator
    97: 0,  # ottoman
    98: 0,  # bottle
    99: 0,  # buffet
    100: 0,  # poster
    101: 0,  # stage
    102: 3,  # van → truck
    103: 0,  # ship
    104: 0,  # fountain
    105: 0,  # conveyer belt
    106: 0,  # canopy
    107: 0,  # washer
    108: 0,  # plaything
    109: 0,  # swimming pool
    110: 0,  # stool
    111: 0,  # barrel
    112: 0,  # basket
    113: 0,  # waterfall
    114: 0,  # tent
    115: 0,  # bag
    116: 7,  # minibike → motorcycle
    117: 0,  # cradle
    118: 0,  # oven
    119: 0,  # ball
    120: 0,  # food
    121: 0,  # step
    122: 3,  # tank → truck
    123: 0,  # trade name
    124: 0,  # microwave
    125: 0,  # pot
    126: 13,  # animal → ground animal
    127: 6,  # bicycle
    128: 0,  # lake
    129: 0,  # dishwasher
    130: 0,  # screen
    131: 0,  # blanket
    132: 0,  # sculpture
    133: 0,  # hood
    134: 0,  # sconce
    135: 0,  # vase
    136: 18,  # traffic light
    137: 0,  # tray
    138: 0,  # ashcan
    139: 0,  # fan
    140: 0,  # pier
    141: 0,  # crt screen
    142: 0,  # plate
    143: 0,  # monitor
    144: 17,  # bulletin board → sign
    145: 0,  # shower
    146: 0,  # radiator
    147: 0,  # glass
    148: 0,  # clock
    149: 0,  # flag
}

COCO_TO_WAYMO_THING = {
    0: 9, # person -> pedestriant
    1: 6, # bicycle
    2: 2, # car
    3: 7, # motorcycle
    4: 5, # airplane -> other large vehicle
    5: 4, # bus
    6: 5, # train -> other large vehicle
    7: 3, # truck
    6: 3, # boat -> truck
    9: 18, # traffic light
    10: 28, # fire hydrant -> static
    11: 17, # stop sign -> sign
    12: 15, # parking meter -> pole
    "bench": 13,
    "bird": 14,
    "cat": 15,
    "dog": 16,
    "horse": 17,
    "sheep": 18,
    "cow": 19,
    "elephant": 20,
    "bear": 21,
    "zebra": 22,
    "giraffe": 23,
    "backpack": 24,
    "umbrella": 25,
    "handbag": 26,
    "tie": 27,
    "suitcase": 28,
    "frisbee": 29,
    "skis": 30,
    "snowboard": 31,
    "sports ball": 32,
    "kite": 33,
    "baseball bat": 34,
    "baseball glove": 35,
    "skateboard": 36,
    "surfboard": 37,
    "tennis racket": 38,
    "bottle": 39,
    "wine glass": 40,
    "cup": 41,
    "fork": 42,
    "knife": 43,
    "spoon": 44,
    "bowl": 45,
    "banana": 46,
    "apple": 47,
    "sandwich": 48,
    "orange": 49,
    "broccoli": 50,
    "carrot": 51,
    "hot dog": 52,
    "pizza": 53,
    "donut": 54,
    "cake": 55,
    "chair": 56,
    "couch": 57,
    "potted plant": 58,
    "bed": 59,
    "dining table": 60,
    "toilet": 61,
    "tv": 62,
    "laptop": 63,
    "mouse": 64,
    "remote": 65,
    "keyboard": 66,
    "cell phone": 67,
    "microwave": 68,
    "oven": 69,
    "toaster": 70,
    "sink": 71,
    "refrigerator": 72,
    "book": 73,
    "clock": 74,
    "vase": 75,
    "scissors": 76,
    "teddy bear": 77,
    "hair drier": 78,
    "toothbrush": 79,
}

COCO_TO_WAYMO_THING = {
    "person": "TYPE_PEDESTRIAN",
    "bicycle": "TYPE_BICYCLE",
    "car": "TYPE_CAR",
    "motorcycle": "TYPE_MOTORCYCLE",
    "airplane": "TYPE_STATIC",
    "bus": "TYPE_BUS",
    "train": "TYPE_OTHER_LARGE_VEHICLE",
    "truck": "TYPE_TRUCK",
    "boat": "TYPE_STATIC",
    "traffic light": "TYPE_TRAFFIC_LIGHT",
    "fire hydrant": "TYPE_STATIC",
    "stop sign": "TYPE_SIGN",
    "parking meter": "TYPE_STATIC",
    "bench": "TYPE_STATIC",
    "bird": "TYPE_BIRD",
    "cat": "TYPE_GROUND_ANIMAL",
    "dog": "TYPE_GROUND_ANIMAL",
    "horse": "TYPE_GROUND_ANIMAL",
    "sheep": "TYPE_GROUND_ANIMAL",
    "cow": "TYPE_GROUND_ANIMAL",
    "elephant": "TYPE_GROUND_ANIMAL",
    "bear": "TYPE_GROUND_ANIMAL",
    "zebra": "TYPE_GROUND_ANIMAL",
    "giraffe": "TYPE_GROUND_ANIMAL",
    "backpack": "TYPE_PEDESTRIAN_OBJECT",
    "umbrella": "TYPE_PEDESTRIAN_OBJECT",
    "handbag": "TYPE_PEDESTRIAN_OBJECT",
    "tie": "TYPE_PEDESTRIAN_OBJECT",
    "suitcase": "TYPE_PEDESTRIAN_OBJECT",
    "frisbee": "TYPE_PEDESTRIAN_OBJECT",
    "skis": "TYPE_PEDESTRIAN_OBJECT",
    "snowboard": "TYPE_PEDESTRIAN_OBJECT",
    "sports ball": "TYPE_PEDESTRIAN_OBJECT",
    "kite": "TYPE_PEDESTRIAN_OBJECT",
    "baseball bat": "TYPE_PEDESTRIAN_OBJECT",
    "baseball glove": "TYPE_PEDESTRIAN_OBJECT",
    "skateboard": "TYPE_PEDESTRIAN_OBJECT",
    "surfboard": "TYPE_PEDESTRIAN_OBJECT",
    "tennis racket": "TYPE_PEDESTRIAN_OBJECT",
    "bottle": "TYPE_STATIC",
    "wine glass": "TYPE_STATIC",
    "cup": "TYPE_STATIC",
    "fork": "TYPE_STATIC",
    "knife": "TYPE_STATIC",
    "spoon": "TYPE_STATIC",
    "bowl": "TYPE_STATIC",
    "banana": "TYPE_STATIC",
    "apple": "TYPE_STATIC",
    "sandwich": "TYPE_STATIC",
    "orange": "TYPE_STATIC",
    "broccoli": "TYPE_STATIC",
    "carrot": "TYPE_STATIC",
    "hot dog": "TYPE_STATIC",
    "pizza": "TYPE_STATIC",
    "donut": "TYPE_STATIC",
    "cake": "TYPE_STATIC",
    "chair": "TYPE_STATIC",
    "couch": "TYPE_STATIC",
    "potted plant": "TYPE_VEGETATION",
    "bed": "TYPE_STATIC",
    "dining table": "TYPE_STATIC",
    "toilet": "TYPE_STATIC",
    "tv": "TYPE_STATIC",
    "laptop": "TYPE_STATIC",
    "mouse": "TYPE_STATIC",
    "remote": "TYPE_STATIC",
    "keyboard": "TYPE_STATIC",
    "cell phone": "TYPE_STATIC",
    "microwave": "TYPE_STATIC",
    "oven": "TYPE_STATIC",
    "toaster": "TYPE_STATIC",
    "sink": "TYPE_STATIC",
    "refrigerator": "TYPE_STATIC",
    "book": "TYPE_STATIC",
    "clock": "TYPE_STATIC",
    "vase": "TYPE_STATIC",
    "scissors": "TYPE_STATIC",
    "teddy bear": "TYPE_STATIC",
    "hair drier": "TYPE_STATIC",
    "toothbrush": "TYPE_STATIC",
}

COCO_TO_WAYMO_STUFF = {
    "things": "TYPE_UNDEFINED",
    "banner": "TYPE_STATIC",
    "blanket": "TYPE_STATIC",
    "bridge": "TYPE_BUILDING",
    "cardboard": "TYPE_STATIC",
    "counter": "TYPE_STATIC",
    "curtain": "TYPE_STATIC",
    "door-stuff": "TYPE_BUILDING",
    "floor-wood": "TYPE_GROUND",
    "flower": "TYPE_VEGETATION",
    "fruit": "TYPE_STATIC",
    "gravel": "TYPE_GROUND",
    "house": "TYPE_BUILDING",
    "light": "TYPE_STATIC",
    "mirror-stuff": "TYPE_STATIC",
    "net": "TYPE_STATIC",
    "pillow": "TYPE_STATIC",
    "platform": "TYPE_BUILDING",
    "playingfield": "TYPE_GROUND",
    "railroad": "TYPE_ROAD",
    "river": "TYPE_GROUND",
    "road": "TYPE_ROAD",
    "roof": "TYPE_BUILDING",
    "sand": "TYPE_GROUND",
    "sea": "TYPE_GROUND",
    "shelf": "TYPE_STATIC",
    "snow": "TYPE_GROUND",
    "stairs": "TYPE_BUILDING",
    "tent": "TYPE_BUILDING",
    "towel": "TYPE_STATIC",
    "wall-brick": "TYPE_BUILDING",
    "wall-stone": "TYPE_BUILDING",
    "wall-tile": "TYPE_BUILDING",
    "wall-wood": "TYPE_BUILDING",
    "water": "TYPE_GROUND",
    "window-blind": "TYPE_BUILDING",
    "window": "TYPE_BUILDING",
    "tree": "TYPE_VEGETATION",
    "fence": "TYPE_BUILDING",
    "ceiling": "TYPE_BUILDING",
    "sky": "TYPE_SKY",
    "cabinet": "TYPE_STATIC",
    "table": "TYPE_STATIC",
    "floor": "TYPE_GROUND",
    "pavement": "TYPE_SIDEWALK",
    "mountain": "TYPE_GROUND",
    "grass": "TYPE_VEGETATION",
    "dirt": "TYPE_GROUND",
    "paper": "TYPE_STATIC",
    "food": "TYPE_STATIC",
    "building": "TYPE_BUILDING",
    "rock": "TYPE_GROUND",
    "wall": "TYPE_BUILDING",
    "rug": "TYPE_GROUND",
}

WAYMO_CLASSES = [
    "TYPE_UNDEFINED",
    "TYPE_EGO_VEHICLE",
    "TYPE_CAR",
    "TYPE_TRUCK",
    "TYPE_BUS",
    "TYPE_OTHER_LARGE_VEHICLE",
    "TYPE_BICYCLE",
    "TYPE_MOTORCYCLE",
    "TYPE_TRAILER",
    "TYPE_PEDESTRIAN",
    "TYPE_CYCLIST",
    "TYPE_MOTORCYCLIST",
    "TYPE_BIRD",
    "TYPE_GROUND_ANIMAL",
    "TYPE_CONSTRUCTION_CONE_POLE",
    "TYPE_POLE",
    "TYPE_PEDESTRIAN_OBJECT",
    "TYPE_SIGN",
    "TYPE_TRAFFIC_LIGHT",
    "TYPE_BUILDING",
    "TYPE_ROAD",
    "TYPE_LANE_MARKER",
    "TYPE_ROAD_MARKER",
    "TYPE_SIDEWALK",
    "TYPE_VEGETATION",
    "TYPE_SKY",
    "TYPE_GROUND",
    "TYPE_DYNAMIC",
    "TYPE_STATIC",
]

waymo_thing_arr = list(COCO_TO_WAYMO_THING.values())
waymo_stuff_arr = list(COCO_TO_WAYMO_STUFF.values())

WAYMO_THING_CLASSES_IDS = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
]
WAYMO_STUFF_CLASSES_IDS = [20, 21, 22, 23, 24, 25, 26, 27, 28, 0]


def get_waymo_class_id_from_coco(class_id, is_thing):
    class_name = waymo_thing_arr[class_id] if is_thing else waymo_stuff_arr[class_id]
    return WAYMO_CLASSES.index(class_name)
