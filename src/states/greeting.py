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
        self.darkness = 0
        self.step_of_darkness = 2
        
        # less of darkness
        while self.darkness < 100:
            self.darkness += self.step_of_darkness
            self.draw_intro()

        # self.draw_instruction()

        while self.not_clicked:
            for event in pygame.event.get():
                self.check_quit_event(event)
                self.check_tap_anything(event)

        while self.darkness > 0:
            self.darkness -= self.step_of_darkness
            self.draw_intro()

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

    def draw_intro(self):
        intro = get_image("intro.png", transparency=True)
        intro = self.resize_image(intro)
        
        transparent_image = pygame.Surface(self.game_config.size_of_screen, pygame.SRCALPHA)
        shade_color = (255, 255, 255, int(self.darkness * 2.55))
        transparent_image.fill(shade_color)  
        transparent_image.blit(intro, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        self.game_config.screen.fill((0, 0, 0)) 
        self.game_config.screen.blit(transparent_image, (0, 0))

        pygame.display.flip()











