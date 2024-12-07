import sys
import os

def get_resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):  # 当应用打包成exe时，使用 _MEIPASS 路径
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# list of all possible players (tuple of 3 positions of flap)
PLAYERS = (
    # red bird
    (
        get_resource_path("assets/sprites/redbird-upflap.png"),
        get_resource_path("assets/sprites/redbird-midflap.png"),
        get_resource_path("assets/sprites/redbird-downflap.png"),
    ),
    # blue bird
    (
        get_resource_path("assets/sprites/bluebird-upflap.png"),
        get_resource_path("assets/sprites/bluebird-midflap.png"),
        get_resource_path("assets/sprites/bluebird-downflap.png"),
    ),
    # yellow bird
    (
        get_resource_path("assets/sprites/yellowbird-upflap.png"),
        get_resource_path("assets/sprites/yellowbird-midflap.png"),
        get_resource_path("assets/sprites/yellowbird-downflap.png"),
    ),
)

# list of backgrounds
BACKGROUNDS = (
    get_resource_path("assets/sprites/background-day.png"),
    get_resource_path("assets/sprites/background-night.png"),
)

# list of pipes
PIPES = (
    get_resource_path("assets/sprites/pipe-green.png"),
    get_resource_path("assets/sprites/pipe-red.png"),
)
