import pygame
import time

class Final_winning:
    def __init__(self, config):
        self.config = config
        surf = pygame.Surface(self.config.size_of_screen)
        surf.fill((200, 0, 0))
        self.config.screen.blit(surf, (0, 0))
        pygame.display.update()
        time.sleep(1)
        self.config.state = "final_winning"