import time
import pygame

from ..utils import get_image

COLOR_BACKGROUND = (106, 117, 111)
COLOR_MIDLINE = (65, 65, 65)
COEF_RESIZE_IMG = 6


class Player(pygame.sprite.Sprite):
    def __init__(self, config) -> None:
        self.game_config = config

        self.vw = self.game_config.player_module_size[0] / 100
        self.vh = self.game_config.player_module_size[1] / 100

        # self.rect = self.image.get_rect()

        self.player_pos = 0
        self.levers = self.game_config.level_config["levers"]


    def resize_image(self, image):
        return pygame.transform.scale(image, (image.get_width() * COEF_RESIZE_IMG, image.get_height() * COEF_RESIZE_IMG))
    
    def draw(self) -> None:
        self.draw_background()
        self.draw_girl()
        self.draw_levers()
        


        self.game_config.screen.blit(self.main_surf, self.game_config.player_module_location)


    def draw_background(self):
        self.main_surf = pygame.Surface(self.game_config.player_module_size)
        self.main_surf.fill(COLOR_BACKGROUND)
        midline = pygame.Surface((100 * self.vw, 5 * self.vh))
        midline.fill(COLOR_MIDLINE)
        self.main_surf.blit(midline, (0 * self.vw, 96 * self.vh))

    def draw_girl(self):
        girl = get_image("girl.png")
        girl = self.resize_image(girl)
        self.main_surf.blit(girl, (5 * self.vw, 95 * self.vh - girl.get_height()))

    def draw_levers(self):
        now_pos = first_pos = 15

        now_player_pos = first_pos + 10 * self.player_pos
        player_surf = pygame.Surface((30, 30))
        player_surf.fill((0, 0, 0))
        self.main_surf.blit(player_surf, (now_player_pos * self.vw, 50 * self.vh)) 


        surf_0 = pygame.Surface((20, 20))
        surf_0.fill((255, 0, 0))

        surf_1 = pygame.Surface((20, 20))
        surf_1.fill((0, 255, 0))

        for object in self.levers:
            if object["activated"]:
                self.main_surf.blit(surf_1, (now_pos * self.vw, 50 * self.vh)) 
            else:
                self.main_surf.blit(surf_0, (now_pos * self.vw, 50 * self.vh))
            now_pos += 10

        



    # logic part ---------------------------
    def move_left(self):
        self.player_pos = max(0, self.player_pos - 1)

    def move_right(self):
        self.player_pos = min(len(self.levers)-1, self.player_pos + 1)

    def activate(self):
        self.levers[self.player_pos]["activated"] = not(self.levers[self.player_pos]["activated"])
        print(f"activated {self.player_pos}")
    # logic part end ------------------------
    

    '''
        так, тз этого модуля
        надо верстать
        (все размеры происходят относительно окна модуля и зависят от размеров этого окна, поэтому просто умножай на vw,vh)
        
    '''

