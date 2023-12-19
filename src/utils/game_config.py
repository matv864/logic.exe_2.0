import pygame
import time

from .working_with_assets import get_level_config
from .working_with_result import save_result, set_saving_result


class GameConfig:
    def __init__(self, screen: pygame.Surface, size_of_screen: int) -> None:
        self.screen = screen
        self.fps = 30
        self.level: int
        self.lifes: int
        self.start_time: float

        self.size_logic_x: int
        self.size_logic_y: int

        # for score board
        self.set_info_from_saving()
        self.state = "greeting"

        self.update_level_config()

        # calculate sizes of screen modules
        self.size_of_screen = size_of_screen
        self.calculate_new_values()
        self.set_sizes_logic_objects()

    def update_level_config(self):
        self.level_config = get_level_config(self.level - 1)

    def update_time(self):
        self.start_time = time.time()

    # counting values for modules with vw, vh
    # this idea is gone from css
    def calculate_new_values(self):
        vw = self.size_of_screen[0] / 100
        vh = self.size_of_screen[1] / 100

        self.player_module_size = (100 * vw, 30 * vh)
        self.player_module_location = (0 * vw, 0 * vh)

        self.schema_module_size = (80 * vw, 70 * vh)
        self.schema_module_location = (0 * vw, 30 * vh)

        self.platform_module_size = (20 * vw, 70 * vh)
        self.platform_module_location = (80 * vw, 30 * vh)

        self.score_module_size = (60 * vw, 10 * vh)
        self.score_module_location = (20 * vw, 0 * vh)

    def set_sizes_logic_objects(self):
        self.size_logic_x = 13 * 6
        self.size_logic_y = 11 * 6

    def full_losing(self):
        self.level = 1
        self.lifes = 3
        self.start_time = time.time()
        self.update_level_config()

        self.saving_info()

    def saving_info(self):
        save_result(self)

    def set_info_from_saving(self):
        set_saving_result(self)

# it's main config of game, where I keeping info about game
# and some method to work with this info
