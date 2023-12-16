import pygame
import json
from pathlib import Path


def get_fonts(name: str, size: int = 24) -> pygame.font.Font:
    path_to_font = Path(Path.cwd() / "assets" / "fonts"/ name) 
    font = pygame.font.Font(path_to_font, size) 
    return font

def get_image(name: str, transparency: bool = False) -> pygame.image:
    path_to_image = Path(Path.cwd() / "assets" / "sprites"/ name) 
    image = pygame.image.load(path_to_image)
    if transparency:
        image = image.convert_alpha()
    return image

def get_gif(name: str) -> pygame.image:
    path_to_gif = Path(Path.cwd() / "assets" / "sprites"/ name) 
    gif_frames = [pygame.image.load(path_to_gif)]
    return gif_frames

def get_audio(name: str) -> pygame.mixer.Sound:
    path_to_sound = Path(Path.cwd() / "assets" / "audio"/ name) 
    sound = pygame.mixer.Sound(path_to_sound)
    return sound

def get_int(st):
    st = str(st).split("level")[-1]
    return int(st.replace(".json", ""))

def get_level_config(level_id: int) -> dict:
    assets = Path(Path.cwd() / "assets" / "levels")
    levels = sorted(assets.iterdir(), key=get_int)
    if level_id < len(levels):
        level_filename = levels[level_id]
        with level_filename.open() as F:
            level_config = json.load(F)
            return level_config
        

