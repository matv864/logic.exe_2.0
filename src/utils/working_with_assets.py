import pygame

from pathlib import Path

def get_fonts(name):
    sans = Path(Path.cwd() / "assets" / "fonts"/ name) 
    font = pygame.font.Font(sans, 24) 
    return font