import pygame
import time

from ..utils import get_font

TEXT_LOSING_1 = '''Не разбивай'''
TEXT_LOSING_2 = '''мой'''
TEXT_LOSING_3 = '''кристалик'''
TEXT_LOSING_4 = '''больше...'''
TEXT_LOSING_5 = '''пожалуйста...'''


class Losing:
    def __init__(self, config):
        self.game_config = config

        self.game_config.lifes -= 1

        self.continue_config_for_drawing()

        if self.game_config.lifes <= 0:
            self.game_config.full_losing()
            self.full_losing()
        else:
            self.temp_death()
        self.game_config.saving_info()

    def continue_config_for_drawing(self):
        self.vw = self.game_config.size_of_screen[0] / 100
        self.vh = self.game_config.size_of_screen[1] / 100
        self.vc = min(self.vw, self.vh)

        self.pixel_font = get_font("pixel.ttf", int(self.vc * 10))

        self.main_surf = pygame.Surface(self.game_config.size_of_screen)

    def temp_death(self):
        self.draw_screen()

        self.game_config.screen.blit(self.main_surf, (0, 0))
        pygame.display.flip()
        time.sleep(2)
        self.game_config.update_level_config()
        self.game_config.state = "play"

    def full_losing(self):
        self.game_config.state = "final_losing"

    def draw_screen(self):
        self.main_surf.fill((0, 0, 0))

        texts_of_losing = [self.pixel_font.render(
            text,
            True,
            (255, 255, 255)
        ) for text in [
            TEXT_LOSING_1,
            TEXT_LOSING_2,
            TEXT_LOSING_3,
            TEXT_LOSING_4,
            TEXT_LOSING_5
        ]]
        y = 20
        for message in texts_of_losing:
            self.main_surf.blit(
                message,
                (40 * self.vw, y * self.vh)
            )
            y += 10

# it's state when user lost life
# and I check user lost only life or all his lifes
