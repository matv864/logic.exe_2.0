import time
import pygame




class Player:
    def __init__(self, config) -> None:
        self.game_config = config

        self.player_pos = 0
        self.variable_positions = [0, 50, 100, 150, 200, 400, 600]

    def draw(self) -> None:
        # rotated_image = pygame.transform.rotate(self.image, self.rot)
        main_surf = pygame.Surface(self.game_config.player_module_size)
        main_surf.fill((0, 255, 120))
        # self.game_config.screen.blit(surf, (50, self.player_pos*50))

        surf2 = pygame.Surface((50, 50))
        surf2.fill((255, 255, 255))
        main_surf.blit(surf2, (self.game_config.player_module_size[0]/3, self.variable_positions[self.player_pos])) 
        self.game_config.screen.blit(main_surf, self.game_config.player_module_location)

    def move_up(self):
        self.player_pos = max(0, self.player_pos - 1)

    def move_down(self):
        self.player_pos = min(len(self.variable_positions)-1, self.player_pos + 1)

    def click(self):
        print("it was click")

