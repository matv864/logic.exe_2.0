import pygame
import time

class Losing:
    def __init__(self, config):
        self.config = config
        surf = pygame.Surface(self.config.size_of_screen)
        surf.fill((200, 200, 200))
        self.config.screen.blit(surf, (0, 0))
        pygame.display.update()
        time.sleep(3)
        self.config.state = "play"
