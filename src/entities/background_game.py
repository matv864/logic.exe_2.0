import pygame


class Background:
    def __init__(self, config):
        self.game_config = config

    def draw(self):
        surf = pygame.Surface(self.game_config.size_of_screen)
        surf.fill((100, 100, 100))
        self.game_config.screen.blit(surf, (0, 0))