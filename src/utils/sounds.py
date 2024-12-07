import sys
import os
import pygame

def get_resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):    # 当应用打包成exe时，使用 _MEIPASS 路径
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class Sounds:
    die: pygame.mixer.Sound
    hit: pygame.mixer.Sound
    point: pygame.mixer.Sound
    swoosh: pygame.mixer.Sound
    wing: pygame.mixer.Sound

    def __init__(self) -> None:
        if "win" in sys.platform:
            ext = "wav"
        else:
            ext = "ogg"

        self.die = pygame.mixer.Sound(get_resource_path(f"assets/audio/die.{ext}"))
        self.hit = pygame.mixer.Sound(get_resource_path(f"assets/audio/hit.{ext}"))
        self.point = pygame.mixer.Sound(get_resource_path(f"assets/audio/point.{ext}"))
        self.swoosh = pygame.mixer.Sound(get_resource_path(f"assets/audio/swoosh.{ext}"))
        self.wing = pygame.mixer.Sound(get_resource_path(f"assets/audio/wing.{ext}"))
