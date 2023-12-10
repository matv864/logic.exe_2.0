import pygame
import time

from .working_with_assets import get_level_config


class GameConfig:
    def __init__(self, screen: pygame.Surface, size_of_screen: int) -> None:
        self.screen = screen
        self.fps = 30

        # for score board
        self.start_time = time.time()
        self.score_now = 0
        self.lifes = 3
        self.level = 1

        self.state = "greeting"
        
        self.update_level_config()
        

        # calculate sizes of screen modules
        self.size_of_screen = size_of_screen
        self.calculate_new_values()


    def update_level_config(self):
        self.level_config = get_level_config(self.level - 1)


    def calculate_new_values(self):
        vw = self.size_of_screen[0] / 100
        vh = self.size_of_screen[1] / 100
        

        self.player_module_size = (20 * vw, 90 * vh)
        self.player_module_location = (0 * vw, 10 * vh)
        
        self.schema_module_size = (80 * vw, 90 * vh)
        self.schema_module_location = (0 * vw, 10 * vh)

        self.platform_module_size = (20 * vw, 90 * vh)
        self.platform_module_location = (80 * vw, 10 * vh)

        self.score_module_size = (60 * vw, 10 * vh)
        self.score_module_location = (20 * vw, 0 * vh)

        


