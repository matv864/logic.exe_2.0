import pygame


class GameConfig:
    def __init__(self, screen: pygame.Surface, clock: pygame.time.Clock, size_of_screen: int) -> None:
        self.screen = screen
        self.clock = clock
        self.fps = 1

        self.player_module_size = (0, 0)
        self.player_module_location = (0, 0)
        
        self.score_module_size = (0, 0), 
        self.score_module_location = (0, 0)

        self.size_of_screen = size_of_screen
        self.calculate_new_values()

        # size_x, size_y, x, y
        

    def calculate_new_values(self):
        vw = self.size_of_screen[0] / 100
        vh = self.size_of_screen[1] / 100

        self.player_module_size = (20 * vw, 100 * vh)
        self.player_module_location = (0 * vw, 0 * vh)

        self.schema_module_size = (60 * vw, 85 * vh)
        self.schema_module_location = (20 * vw, 15 * vh)

        self.platform_module_size = (20 * vw, 100 * vh)
        self.platform_module_location = (80 * vw, 0 * vh)

        self.score_module_size = (60 * vw, 15 * vh)
        self.score_module_location = (20 * vw, 0 * vh)

        


    def tick(self) -> None:
        self.clock.tick(self.fps)
