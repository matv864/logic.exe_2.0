import pygame
import time

from .working_with_assets import get_level_config
from .working_with_result import save_result, set_saving_result


START_SCORE = 1000
COEF_SCORE_LIFE = 200
MAX_LIFES = 3


class GameConfig:
    def __init__(self, screen: pygame.Surface, size_of_screen: int) -> None:
        self.screen = screen
        self.fps = 30

        self.level: int
        self.lifes: int
        self.start_time: float
        self.score: int

        self.size_logic_x: int
        self.size_logic_y: int

        self.buttons = dict()

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
        time_now = time.time()
        real_time_from_start = time_now - self.start_time
        self.time_from_start = int(real_time_from_start)

    def update_score(self):
        self.update_time()
        lost_lifes = MAX_LIFES - self.lifes
        self.score = START_SCORE - \
            self.time_from_start - \
            COEF_SCORE_LIFE * lost_lifes
        if self.score <= 1:
            # self.game_config.state = "losing"
            self.lifes = 0

    def set_state(self, state):
        self.state = state

    # counting values for modules with vw, vh
    # this idea is gone from css
    def calculate_new_values(self):
        vw = self.size_of_screen[0] / 100
        vh = self.size_of_screen[1] / 100

        self.player_module_size = (100 * vw, 30 * vh)
        self.player_module_location = (0 * vw, 0 * vh)

        self.schema_module_size = (70 * vw, 70 * vh)
        self.schema_module_location = (0 * vw, 30 * vh)

        self.platform_module_size = (30 * vw, 70 * vh)
        self.platform_module_location = (70 * vw, 30 * vh)

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

    def handle_click(self, click_coords):
        click_x, click_y = click_coords
        for key_coords, func in self.buttons.items():
            x1, y1, x2, y2 = key_coords
            if (x1 <= click_x <= x2 and y1 <= click_y <= y2):
                func(self)


# it's main config of game, where I keeping info about game
# and some method to work with this info
