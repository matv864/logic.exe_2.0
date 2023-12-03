import pygame
import time


class Score:
    def __init__(self, config):
        self.game_config = config

        vw = self.game_config.platform_module_size[0] / 100
        vh = self.game_config.platform_module_size[1] / 100

        self.score = 0
        self.lifes = 0
        self.level = 0
        self.time = 0

    def draw(self) -> None:
        # rotated_image = pygame.transform.rotate(self.image, self.rot)
        main_surf = pygame.Surface(self.game_config.score_module_size)
        main_surf.fill((40, 70, 255))
        self.game_config.screen.blit(main_surf, self.game_config.score_module_location)



    