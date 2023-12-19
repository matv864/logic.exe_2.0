import pygame
import json
from pathlib import Path
from PIL import Image, ImageSequence


def get_font(name: str, size: int = 24) -> pygame.font.Font:
    path_to_font = Path(Path.cwd() / "assets" / "fonts" / name)
    font = pygame.font.Font(path_to_font, size)
    return font


def get_image(name: str, transparency: bool = False) -> pygame.image:
    path_to_image = Path(Path.cwd() / "assets" / "sprites" / name)
    image = pygame.image.load(path_to_image)
    if transparency:
        image = image.convert_alpha()
    return image


def get_gif(name: str, count_frames: int | None = None) -> pygame.image:
    path_to_gif = Path(Path.cwd() / "assets" / "sprites" / name)
    gif = Image.open(path_to_gif)
    frames = [frame.copy() for frame in ImageSequence.Iterator(gif)]

    pygame_surface_list = []
    for frame in frames:
        pygame_surface = pygame.image.fromstring(
            frame.tobytes(),
            frame.size,
            frame.mode
        ).convert_alpha()
        pygame_surface_list.append(pygame_surface)
    pygame_surface_list.pop(0)

    return pygame_surface_list


def get_audio(name: str) -> pygame.mixer.Sound:
    path_to_sound = Path(Path.cwd() / "assets" / "audio" / name)
    sound = pygame.mixer.Sound(path_to_sound)
    return sound


def get_int_from_filename(st: Path) -> int:
    st = str(st).split("level")[-1]
    return int(st.replace(".json", ""))


def get_level_config(level_id: int) -> dict:
    assets = Path(Path.cwd() / "assets" / "levels")
    levels = sorted(assets.iterdir(), key=get_int_from_filename)
    if level_id < len(levels):
        level_filename = levels[level_id]
        with level_filename.open() as F:
            level_config = json.load(F)
            return level_config

# methods to work with any files in assets, where all path are wroten here
