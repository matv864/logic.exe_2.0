import pygame


class GameConfig:
    def __init__(self, screen: pygame.Surface, clock: pygame.time.Clock, size_of_screen: int) -> None:
        self.screen = screen
        self.clock = clock
        self.fps = 1

        self.size_of_screen = size_of_screen

        self.count_player_pos = 10


    def tick(self) -> None:
        self.clock.tick(self.fps)
