# need to add mouse click how active lever
# need to add check to win or new level

import pygame

from .engine import Playing, Greeting

from .utils import GameConfig

# from .utils import Window, Level


class Logic:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("LOGIC2.EXE")
        self.size_of_screen = (1920, 1200)
        # window = Window(288, 512)

        screen = pygame.display.set_mode(self.size_of_screen)
        self.config = GameConfig(
            screen=screen,
            size_of_screen = self.size_of_screen
        )
        

    def start(self):
        while True:
            match self.config.state:
                case "greeting":
                    Greeting(self.config)
                case "play":
                    Playing(self.config)
                
            
            



    
