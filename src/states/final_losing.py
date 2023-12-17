import pygame
import time

class Final_losing:
    def __init__(self, config):
        self.game_config = config
        self.cleaning_config()

        surf = pygame.Surface(self.game_config.size_of_screen)
        surf.fill((0, 200, 200))
        self.game_config.screen.blit(surf, (0, 0))
        pygame.display.flip()
        time.sleep(3)
        self.game_config.state = "play"




    def cleaning_config(self):
        self.game_config.start_time = time.time()
        self.game_config.score_now = 0
        self.game_config.lifes = 3
        self.game_config.level = 1

        self.game_config.update_level_config()

