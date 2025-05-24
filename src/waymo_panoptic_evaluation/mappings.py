WAYMO_THING_CLASSES_IDS = [2, 3, 4, 5, 8, 9, 10, 11]
WAYMO_STUFF_CLASSES_IDS = [
    0,
    1,
    6,
    7,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
]
WAYMO_CONTINUOUS_IDS = WAYMO_THING_CLASSES_IDS + WAYMO_STUFF_CLASSES_IDS
WAYMO_CLASS_ID_BY_LABEL = {
    "undefined": 0,
    "ego vehicle": 1,
    "car": 2,
    "truck": 3,
    "bus": 4,
    "other large vehicle": 5,
    "bicycle": 6,
    "motorcycle": 7,
    "trailer": 8,
    "pedestrian": 9,
    "cyclist": 10,
    "motorcyclist": 11,
    "bird": 12,
    "ground animal": 13,
    "construnction cone": 14,
    "pole": 15,
    "pedestrian object": 16,
    "sign": 17,
    "traffic light": 18,
    "building": 19,
    "road": 20,
    "lane marker": 21,
    "road marker": 22,
    "sidewalk": 23,
    "vegetation": 24,
    "sky": 25,
    "ground": 26,
    "dynamic": 27,
    "static": 28,
}
WAYMO_CLASS_LABELS = list(WAYMO_CLASS_ID_BY_LABEL.keys())

COCO_LABEL_TO_WAYMO_LABEL = {
    "person": "pedestrian",
    "bicycle": "bicycle",
    "car": "car",
    "motorcycle": "motorcycle",
    "airplane": "other large vehicle",
    "bus": "bus",
    "train": "other large vehicle",
    "truck": "truck",
    "boat": "other large vehicle",
    "traffic light": "traffic light",
    "fire hydrant": "static",
    "stop sign": "sign",
    "parking meter": "static",
    "bench": "static",
    "bird": "bird",
    "cat": "ground animal",
    "dog": "ground animal",
    "horse": "ground animal",
    "sheep": "ground animal",
    "cow": "ground animal",
    "elephant": "ground animal",
    "bear": "ground animal",
    "zebra": "ground animal",
    "giraffe": "ground animal",
    "backpack": "pedestrian object",
    "umbrella": "pedestrian object",
    "handbag": "pedestrian object",
    "tie": "pedestrian object",
    "suitcase": "pedestrian object",
    "frisbee": "pedestrian object",
    "skis": "pedestrian object",
    "snowboard": "pedestrian object",
    "sports ball": "pedestrian object",
    "kite": "pedestrian object",
    "baseball bat": "pedestrian object",
    "baseball glove": "pedestrian object",
    "skateboard": "pedestrian object",
    "surfboard": "pedestrian object",
    "tennis racket": "pedestrian object",
    "bottle": "pedestrian object",
    "wine glass": "pedestrian object",
    "cup": "pedestrian object",
    "fork": "pedestrian object",
    "knife": "pedestrian object",
    "spoon": "pedestrian object",
    "bowl": "pedestrian object",
    "banana": "static",
    "apple": "static",
    "sandwich": "static",
    "orange": "static",
    "broccoli": "static",
    "carrot": "static",
    "hot dog": "static",
    "pizza": "static",
    "donut": "static",
    "cake": "static",
    "chair": "static",
    "couch": "static",
    "potted plant": "vegetation",
    "bed": "static",
    "dining table": "static",
    "toilet": "static",
    "tv": "static",
    "laptop": "static",
    "mouse": "static",
    "remote": "static",
    "keyboard": "static",
    "cell phone": "static",
    "microwave": "static",
    "oven": "static",
    "toaster": "static",
    "sink": "static",
    "refrigerator": "static",
    "book": "static",
    "clock": "static",
    "vase": "static",
    "scissors": "static",
    "teddy bear": "static",
    "hair drier": "static",
    "toothbrush": "static",
    "things": "static",
    "banner": "static",
    "blanket": "static",
    "bridge": "static",
    "cardboard": "static",
    "counter": "static",
    "curtain": "static",
    "door-stuff": "static",
    "floor-wood": "static",
    "flower": "vegetation",
    "fruit": "static",
    "gravel": "road",
    "house": "building",
    "light": "static",
    "mirror-stuff": "static",
    "net": "static",
    "pillow": "static",
    "platform": "static",
    "playingfield": "static",
    "railroad": "ground",
    "river": "static",
    "road": "road",
    "roof": "building",
    "sand": "ground",
    "sea": "static",
    "shelf": "static",
    "snow": "ground",
    "stairs": "static",
    "tent": "static",
    "towel": "static",
    "wall-brick": "building",
    "wall-stone": "building",
    "wall-tile": "building",
    "wall-wood": "building",
    "water": "static",
    "window-blind": "building",
    "window": "building",
    "tree": "vegetation",
    "fence": "static",
    "ceiling": "static",
    "sky": "sky",
    "cabinet": "static",
    "table": "static",
    "floor": "ground",
    "pavement": "sidewalk",
    "mountain": "vegetation",
    "grass": "vegetation",
    "dirt": "ground",
    "paper": "static",
    "food": "static",
    "building": "building",
    "rock": "vegetation",
    "wall": "building",
    "rug": "static",
}

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

COCO_ID_TO_WAYMO_ID = {
    1: 9,    # person → pedestrian
    2: 6,    # bicycle
    3: 2,    # car
    4: 7,    # motorcycle
    5: 5,    # airplane → other large vehicle
    6: 4,    # bus
    7: 5,    # train → other large vehicle
    8: 3,    # truck
    9: 5,    # boat → other large vehicle
    10: 18,  # traffic light
    11: 28,  # fire hydrant → static
    13: 17,  # stop sign → sign
    14: 28,  # parking meter → static
    15: 28,  # bench → static
    16: 12,  # bird
    17: 13,  # cat → ground animal
    18: 13,  # dog → ground animal
    19: 13,  # horse → ground animal
    20: 13,  # sheep → ground animal
    21: 13,  # cow → ground animal
    22: 13,  # elephant → ground animal
    23: 13,  # bear → ground animal
    24: 13,  # zebra → ground animal
    25: 13,  # giraffe → ground animal
    27: 16,  # backpack → pedestrian object
    28: 16,  # umbrella → pedestrian object
    31: 16,  # handbag → pedestrian object
    32: 16,  # tie → pedestrian object
    33: 16,  # suitcase → pedestrian object
    34: 16,  # frisbee → pedestrian object
    35: 16,  # skis → pedestrian object
    36: 16,  # snowboard → pedestrian object
    37: 16,  # sports ball → pedestrian object
    38: 16,  # kite → pedestrian object
    39: 16,  # baseball bat → pedestrian object
    40: 16,  # baseball glove → pedestrian object
    41: 16,  # skateboard → pedestrian object
    42: 16,  # surfboard → pedestrian object
    43: 16,  # tennis racket → pedestrian object
    44: 16,  # bottle → pedestrian object
    46: 16,  # wine glass → pedestrian object
    47: 16,  # cup → pedestrian object
    48: 16,  # fork → pedestrian object
    49: 16,  # knife → pedestrian object
    50: 16,  # spoon → pedestrian object
    51: 16,  # bowl → pedestrian object
    52: 16,  # banana → pedestrian object
    53: 16,  # apple → pedestrian object
    54: 16,  # sandwich → pedestrian object
    55: 16,  # orange → pedestrian object
    56: 16,  # broccoli → pedestrian object
    57: 16,  # carrot → pedestrian object
    58: 16,  # hot dog → pedestrian object
    59: 16,  # pizza → pedestrian object
    60: 16,  # donut → pedestrian object
    61: 16,  # cake → pedestrian object
    62: 28,  # chair → static
    63: 28,  # couch → static
    64: 24,  # potted plant → vegetation
    65: 28,  # bed → static
    67: 28,  # dining table → static
    70: 28,  # toilet → static
    72: 28,  # tv → static
    73: 28,  # laptop → static
    74: 28,  # mouse → static
    75: 28,  # remote → static
    76: 28,  # keyboard → static
    77: 16,  # cell phone → pedestrian object
    78: 28,  # microwave → static
    79: 28,  # oven → static
    80: 28,  # toaster → static
    81: 28,  # sink → static
    82: 28,  # refrigerator → static
    84: 16,  # book → pedestrian object
    85: 16,  # clock → pedestrian object
    86: 28,  # vase → static
    87: 16,  # scissors → pedestrian object
    88: 16,  # teddy bear → pedestrian object
    89: 16,  # hair drier → pedestrian object
    90: 16,  # toothbrush → pedestrian object
    92: 17,  # banner → sign
    93: 28,  # blanket → static
    95: 19,  # bridge → building
    100: 28, # cardboard → static
    107: 28, # counter → static
    109: 28, # curtain → static
    112: 19, # door-stuff → building
    118: 26, # floor-wood → ground
    119: 24, # flower → vegetation
    122: 28, # fruit → static
    125: 26, # gravel → ground
    128: 19, # house → building
    130: 28, # light → static
    133: 19, # mirror-stuff → building
    138: 28, # net → static
    141: 28, # pillow → static
    144: 19, # platform → building
    145: 20, # playingfield → road
    147: 20, # railroad → road
    148: 26, # river → ground
    149: 20, # road
    151: 19, # roof → building
    154: 26, # sand → ground
    155: 26, # sea → ground
    156: 28, # shelf → static
    159: 26, # snow → ground
    161: 19, # stairs → building
    166: 19, # tent → building
    168: 28, # towel → static
    171: 19, # wall-brick → building
    175: 19, # wall-stone → building
    176: 19, # wall-tile → building
    177: 19, # wall-wood → building
    178: 26, # water-other → ground
    180: 19, # window-blind → building
    181: 19, # window-other → building
    184: 24, # tree-merged → vegetation
    185: 19, # fence-merged → building
    186: 19, # ceiling-merged → building
    187: 25, # sky-other-merged → sky
    188: 19, # cabinet-merged → building
    189: 19, # table-merged → building
    190: 26, # floor-other-merged → ground
    191: 23, # pavement-merged → sidewalk
    192: 26, # mountain-merged → ground
    193: 24, # grass-merged → vegetation
    194: 26, # dirt-merged → ground
    195: 28, # paper-merged → static
    196: 28, # food-other-merged → static
    197: 19, # building-other-merged → building
    198: 26, # rock-merged → ground
    199: 19, # wall-other-merged → building
    200: 26  # rug-merged → ground
}

def get_waymo_class_id_from_coco_label(coco_label: str) -> int:
    waymo_label = COCO_LABEL_TO_WAYMO_LABEL.get(coco_label, "undefined")
    waymo_class_id = WAYMO_CLASS_ID_BY_LABEL.get(waymo_label, 0)
    return waymo_class_id

def is_waymo_thing(waymo_class_id: int) -> bool:
    return waymo_class_id in WAYMO_THING_CLASSES_IDS