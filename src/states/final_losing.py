import pygame
import time

class Final_losing:
    def __init__(self, config):
        self.config = config
        surf = pygame.Surface(self.config.size_of_screen)
        surf.fill((0, 200, 200))
        self.config.screen.blit(surf, (0, 0))
        pygame.display.update()
        time.sleep(3)
        self.config.state = "play"
