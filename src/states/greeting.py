import pygame
import time

class Greeting:
    def __init__(self, config):
        self.config = config
        surf = pygame.Surface(self.config.size_of_screen)
        surf.fill((50, 100, 200))
        self.config.screen.blit(surf, (0, 0))
        time.sleep(1)
        self.config.state = "play"
