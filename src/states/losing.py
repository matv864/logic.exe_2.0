import pygame
import time

from ..utils import get_font

TEXT_LOSING = '''SORRY?  Your heart is broken'''


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
        time.sleep(3)
        self.game_config.update_level_config()
        self.game_config.state = "play"

    def full_losing(self):
        self.game_config.state = "final_losing"

    def draw_screen(self):
        self.main_surf.fill((0, 0, 0))
        text_of_losing = self.pixel_font.render(
            TEXT_LOSING,
            True,
            (255, 255, 255)
        )
        self.main_surf.blit(
            text_of_losing,
            (20 * self.vw, 35 * self.vh)
        )

# it's state when user lost life
# and I check user lost only life or all his lifes
