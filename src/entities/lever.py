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

        self.y_level_position = 68


    def resize_image(self, image, sizes=None):
        if sizes:
            return pygame.transform.scale(image, sizes)    
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
        player_surf.fill((255, 255, 255))
        self.main_surf.blit(player_surf, (now_player_pos * self.vw, self.y_level_position * self.vh)) 


        lever_off = get_image("lever_off.png")
        lever_off = self.resize_image(lever_off)

        lever_on = get_image("lever_on.png")
        lever_on = self.resize_image(lever_on)

        for object in self.levers:
            if object["activated"]:
                self.main_surf.blit(lever_off, (now_pos * self.vw, self.y_level_position * self.vh)) 
            else:
                self.main_surf.blit(lever_on, (now_pos * self.vw, self.y_level_position * self.vh))
            now_pos += 10

        



    # logic part ---------------------------
    def move_left(self):
        self.player_pos = max(0, self.player_pos - 1)

    def move_right(self):
        self.player_pos = min(len(self.levers)-1, self.player_pos + 1)

    def activate(self):
        self.levers[self.player_pos]["activated"] = not(self.levers[self.player_pos]["activated"])
    # logic part end ------------------------
    

    '''
        так, тз этого модуля
        надо верстать
        (все размеры происходят относительно окна модуля и зависят от размеров этого окна, поэтому просто умножай на vw,vh)
        
    '''

