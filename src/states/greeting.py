import sys
import pygame
import time

from pygame import MOUSEBUTTONDOWN, KEYDOWN
from pygame.locals import QUIT


from ..utils import get_image, get_font, get_record

TEXT_TO_CONTINUE = "Tap anything to continue..."

class Greeting:
    def __init__(self, config):
        self.game_config = config
        self.main_surf = pygame.Surface(self.game_config.size_of_screen)
        self.not_clicked = True
        

        self.vw = self.game_config.size_of_screen[0] / 100
        self.vh = self.game_config.size_of_screen[1] / 100
        self.vc = min(self.vw, self.vh)

        self.intro = get_image("intro.png", transparency=True)
        self.intro = self.resize_image(self.intro)
        self.darkness_intro = 0
        self.step_of_darkness_intro = 2

        self.pixel_font = get_font("pixel.ttf", int(self.vc * 4.5))

        self.size_text = (10 * self.vw, 3 * self.vh)
        self.location_text = (65 * self.vw, 0 * self.vh)
        self.darkness_text = 0
        self.step_of_darkness_text = 1

        self.size_record = (10 * self.vw, 3 * self.vh)
        self.location_record = (20 * self.vw, 0 * self.vh)
        self.darkness_record = 60
        self.step_of_darkness_record = 1
        self.record_value = get_record()

        
        
        # less of darkness
        while self.darkness_intro < 100:
            self.darkness_intro += self.step_of_darkness_intro
            self.draw()

        # self.draw_instruction()

        while self.not_clicked:
            for event in pygame.event.get():
                self.check_quit_event(event)
                self.check_tap_anything(event)
            
            self.draw()

        

            

        while self.darkness_intro > 0:
            self.darkness_intro -= self.step_of_darkness_intro
            self.draw()

        self.game_config.state = "play"



    def check_quit_event(self, event):
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    def check_tap_anything(self, event):
        if event.type in [MOUSEBUTTONDOWN, KEYDOWN]:
            self.not_clicked = False
            
    
    def resize_image(self, image):
        return pygame.transform.scale(image, self.game_config.size_of_screen)
    





    def draw(self):
        self.game_config.screen.fill((0, 0, 0)) 

        self.draw_intro()
        self.draw_record()
        self.draw_text_to_continue()

        pygame.display.flip()

    def draw_intro(self):
        transparent_image = pygame.Surface(self.game_config.size_of_screen, pygame.SRCALPHA)
        shade_color = (255, 255, 255, int(self.darkness_intro * 2.55))
        transparent_image.fill(shade_color)  
        transparent_image.blit(self.intro, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        self.game_config.screen.blit(transparent_image, (0, 0))

        

    def draw_record(self):
        if self.darkness_record >= (100 - self.step_of_darkness_record):
            self.darkness_record = -100
        self.darkness_record += self.step_of_darkness_record

        text_of_record = f"your record: {self.record_value}"

        main_color = int(abs(self.darkness_record) * 2.55)
        shade_color = (main_color, main_color, main_color)
        transparent_record = self.pixel_font.render(text_of_record, True, shade_color)
        self.game_config.screen.blit(transparent_record, self.location_record)

    def draw_text_to_continue(self):
        if self.darkness_text >= (100 - self.step_of_darkness_text):
            self.darkness_text = -100
        self.darkness_text += self.step_of_darkness_text

        main_color = int(abs(self.darkness_text) * 2.55)
        shade_color = (main_color, main_color, main_color)
        transparent_text = self.pixel_font.render(TEXT_TO_CONTINUE, True, shade_color)
        self.game_config.screen.blit(transparent_text, self.location_text)












