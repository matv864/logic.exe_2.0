import sys
import pygame
import time

from pygame import MOUSEBUTTONDOWN, KEYDOWN
from pygame.locals import QUIT


from ..utils import get_image

class Greeting:
    def __init__(self, config):
        self.game_config = config
        self.main_surf = pygame.Surface(self.game_config.size_of_screen)
        self.not_clicked = True
        self.darkness = 100
        self.step_of_darkness = 5
        
        # while self.darkness > self.step_of_darkness:
        #     self.make_less_dark()
        #     time.sleep(1)
        self.draw_instruction()

        while self.not_clicked:
            for event in pygame.event.get():
                self.check_quit_event(event)
                self.check_tap_anything(event)

        # while self.darkness < 100:
        #     self.make_more_dark()
        


        self.game_config.state = "play"

    def check_quit_event(self, event):
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    def check_tap_anything(self, event):
        if event.type in [MOUSEBUTTONDOWN, KEYDOWN]:
            self.not_clicked = False
            
    
    def resize_image(self, image):
        width_x, width_y = self.game_config.size_of_screen
        width_x = int(width_x * 0.98)
        width_y = int(width_y * 0.98)
        sizes = (width_x, width_y)
        return pygame.transform.scale(image, sizes)

    def draw_instruction(self):
        instruction = get_image("intro.png")
        instruction = self.resize_image(instruction)
        self.game_config.screen.blit(instruction, (0, 0))
        
        # shade_surface = pygame.Surface(self.game_config.size_of_screen, pygame.SRCALPHA)
        # shade_color = (0, 0, 0, int(self.darkness * 2.55))
        # shade_surface.fill(shade_color)

        # self.game_config.screen.blit(shade_surface, (100, 100), special_flags=pygame.BLEND_RGBA_MULT)

        pygame.display.flip()


    # def make_less_dark(self):
    #     self.darkness -= self.step_of_darkness
    #     self.draw_instruction()
    #     # print(self.darkness)

    # def make_more_dark(self):
    #     self.darkness += self.step_of_darkness
    #     self.draw_instruction()
    #     # print(self.darkness)
    










