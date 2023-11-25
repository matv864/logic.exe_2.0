import time
import pygame

class Player_config:
    def __init__(self):
        self.player_pos = 0
        self.variable_positions = []

    def count_positions(self, size_of_screen, count_player_pos):
        pass

class Player:
    def __init__(self, config) -> None:
        self.game_config = config
        self.player_config = Player_config()
        self.player_config.count_positions(self.game_config.size_of_screen, self.game_config.count_player_pos)

    def draw(self) -> None:
        # rotated_image = pygame.transform.rotate(self.image, self.rot)
        surf = pygame.Surface((50, 50))
        surf.fill((255, 255, 255))
        self.game_config.screen.blit(surf, (50, self.player_config.player_pos*50))

    def move_up(self):
        self.player_config.player_pos = min(self.game_config.count_player_pos, self.player_config.player_pos + 1)
            

    def move_down(self):
        self.player_config.player_pos = max(0, self.player_config.player_pos - 1)

