import pygame
import time


class Winning:
    def __init__(self, config):
        self.config = config

        self.config.level += 1
        self.config.update_level_config()
        if self.config.level_config:
            self.temp_win()
        else:
            self.full_winning()

    def temp_win(self):
        surf = pygame.Surface(self.config.size_of_screen)
        surf.fill((0, 0, 0))
        self.config.screen.blit(surf, (0, 0))
        time.sleep(1)
        pygame.display.update()
        self.config.saving_info()
        self.config.state = "play"

    def full_winning(self):
        self.config.state = "final_winning"

# it's state when user win level and I check user win only level or all game
