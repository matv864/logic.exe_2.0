# need to add mouse click how active lever
# need to add check to win or new level

import pygame

from .states import Playing, Greeting, Losing, Winning, Final_winning, Final_losing

from .utils import GameConfig

# from .utils import Window, Level


class Logic:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("LOGIC2.EXE")
        self.size_of_screen = (1000, 500)
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
                case "losing":
                    Losing(self.config)
                case "final_losing":
                    Final_losing(self.config)
                case "winning":
                    Winning(self.config)
                case "final_winning":
                    Final_winning(self.config)
                
            
            



    
