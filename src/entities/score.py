import pygame
import time
from pathlib import Path

from ..utils import get_image, get_font, get_record


START_SCORE = 1000
COEF_SCORE_LIFE = 100
MAX_LIFES = 3
 
class Score: 
    def __init__(self, config): 
        self.game_config = config 
 
        self.time_from_start = 0 
        # print(self.game_config.platform_module_size) 
        self.vw = self.game_config.score_module_size[0] / 100 
        self.vh = self.game_config.score_module_size[1] / 100 
        self.vc = (self.vh + self.vw) / 2
        # self.font = get_fonts("firasans.ttf", int(6 * self.vc))
        self.score = 0
 
 
    def update_time(self): 
        time_now = time.time() 
        real_time_from_start = time_now - self.game_config.start_time 
        self.time_from_start = int(real_time_from_start)

    def update_score(self):
        lost_lifes = MAX_LIFES - self.game_config.lifes
        self.score = START_SCORE - self.time_from_start  - COEF_SCORE_LIFE * lost_lifes
 
    def draw(self) -> None: 
        self.update_time()
        self.update_score()

        maket = get_image("scoreboard_maket.png")

        main_surf = pygame.Surface(self.game_config.score_module_size) 
        main_surf.blit(maket, (0, 0))
        # main_surf.fill((40, 70, 255)) 
 
        # self.score = max(0, self.start_score - self.time_from_start) 
        # self.draw_score(main_surf) 
 
        self.game_config.screen.blit(main_surf, self.game_config.score_module_location) 






    
 