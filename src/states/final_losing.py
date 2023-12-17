import pygame
import time

class Final_losing:
    def __init__(self, config):
        self.game_config = config

        surf = pygame.Surface(self.game_config.size_of_screen)
        surf.fill((0, 200, 200))
        self.game_config.screen.blit(surf, (0, 0))
        pygame.display.flip()
        time.sleep(3)
        self.game_config.state = "play"




