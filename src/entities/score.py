import pygame
import time
from pathlib import Path

from ..utils import get_fonts
 
 
class Score: 
    def __init__(self, config): 
        self.game_config = config 
 
        self.time_from_start = 0 
        # print(self.game_config.platform_module_size) 
        self.vw = self.game_config.score_module_size[0] / 100 
        self.vh = self.game_config.score_module_size[1] / 100 
 
        self.score = 0 
        self.start_score = 1000 
 
         
 
    def update_time(self): 
        time_now = time.time() 
        real_time_from_start = time_now - self.game_config.start_time 
        self.time_from_start = int(real_time_from_start) 
 
    def draw(self) -> None: 
        self.update_time() 
        # rotated_image = pygame.transform.rotate(self.image, self.rot) 
        main_surf = pygame.Surface(self.game_config.score_module_size) 
        main_surf.fill((40, 70, 255)) 
 
        self.score = max(0, self.start_score - self.time_from_start) 
        self.draw_score(main_surf) 
 
        self.game_config.screen.blit(main_surf, self.game_config.score_module_location) 
 
    def draw_oct(self,start_x,start_y):
        return [[start_x, start_y+10*self.vh], [start_x, start_y+60*self.vh-10*self.vh], 
                [start_x+10*self.vh,start_y+60*self.vh], [start_x+17*self.vw-10*self.vh, start_y+60*self.vh],
                [start_x+17*self.vw,start_y+60*self.vh-10*self.vh],[start_x+17*self.vw,start_y+10*self.vh],
                [start_x+17*self.vw-10*self.vh,start_y],[start_x+10*self.vh,start_y]]
 
    def draw_frame(self,surf,start_x,start_y):
        pygame.draw.polygon(surf, (0,0,0), 
                    self.draw_oct(start_x+7,start_y+7))
        pygame.draw.polygon(surf, (255,255,255), 
                    self.draw_oct(start_x,start_y))
        pygame.draw.polygon(surf, (0,0,0), 
                    self.draw_oct(start_x,start_y),1)
    def draw_score(self, main_surf): 
        # self.game_config.level 
        # self.game_config.lifes 
        # self.score

        font = get_fonts("FiraSans-Regular.ttf")
        self.draw_frame(main_surf,3*self.vw,25*self.vh)
        img = font.render(f"level: {self.game_config.level}", True, "red") 
        main_surf.blit(img, (5*self.vw, 55*self.vh-12)) 
 

        img = font.render(f"lifes: {self.game_config.lifes}", True, "red") 
        main_surf.blit(img, (42*self.vw, 30*self.vh)) 
 
        img = font.render(f"time: {self.score}", True, "red") 
        main_surf.blit(img, (80*self.vw, 30*self.vh)) 
 
 
        ''' 
        так, тз этого модуля 
        надо красиво отверстать скор борд 
        (все размеры происходят относительно окна модуля и зависят от размеров этого окна, поэтому просто умножай на vw,vh) 
         
        '''