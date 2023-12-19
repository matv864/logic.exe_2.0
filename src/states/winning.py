import pygame
import time

from ..utils import get_font

TEXT_WINNING = "YEAH, you pass this level"


class Winning:
    def __init__(self, config):
        self.game_config = config

        self.game_config.level += 1
        self.game_config.update_level_config()

        self.continue_config_for_drawing()

        if self.game_config.level_config:
            self.temp_win()
        else:
            self.full_winning()

    def continue_config_for_drawing(self):
        self.vw = self.game_config.size_of_screen[0] / 100
        self.vh = self.game_config.size_of_screen[1] / 100
        self.vc = min(self.vw, self.vh)

        self.pixel_font = get_font("pixel.ttf", int(self.vc * 4.5))

        self.main_surf = pygame.Surface(self.game_config.size_of_screen)

    def temp_win(self):
        self.draw_screen()

        self.game_config.screen.blit(self.main_surf, (0, 0))
        pygame.display.flip()

        self.game_config.saving_info()
        self.game_config.state = "play"
        time.sleep(3)

    def full_winning(self):
        self.game_config.state = "final_winning"

    def draw_screen(self):
        self.main_surf.fill((0, 0, 0))
        text_of_winning = self.pixel_font.render(
            TEXT_WINNING,
            True,
            (255, 255, 255)
        )
        self.main_surf.blit(
            text_of_winning,
            (self.vw * 45, self.vh * 45)
        )

# it's state when user win level and I check user win only level or all game
