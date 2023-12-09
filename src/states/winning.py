import pygame
import time

class Winning:
    def __init__(self, config):
        self.config = config
        surf = pygame.Surface(self.config.size_of_screen)
        surf.fill((0, 0, 0))
        self.config.screen.blit(surf, (0, 0))
        time.sleep(1)
        pygame.display.update()
        self.config.state = "winning"