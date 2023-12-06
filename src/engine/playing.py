import sys
import time
import pygame

from pygame.locals import QUIT, K_DOWN, K_UP, K_w, K_s, K_RETURN, K_SPACE
from ..entities import Background, Player, Score, Schema, Platform

class Playing:
    def __init__(self, config):
        self.config = config
        self.background = Background(self.config)
        self.player = Player(self.config)
        self.schema = Schema(self.config)
        self.platform = Platform(self.config)
        self.score = Score(self.config)

        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                self.check_quit_event(event)
                if event.type == pygame.KEYDOWN:
                    self.handle_up_down(event)
                    self.handle_enter_click(event)

            self.background.draw()
            self.player.draw()
            self.schema.draw()
            self.platform.draw()
            self.score.draw()
            
            pygame.display.update()
            # need to add check to win or new level
            # 1 - win, 0 - lose
            if self.check_to_win():
                print("win")
            if self.check_to_lose():
                self.losing()
                break

            clock.tick(self.config.fps)


    def handle_up_down(self, event):
        # print(event.key)
        # глюки с русскоязычной раскладкой и стрелочками нампада
        if event.key in [K_UP, K_w, 1094, 1073741920]:
            self.player.move_up()
            return
        if event.key in [K_DOWN, K_s, 1099, 1073741914]:
            self.player.move_down()
            return

    def handle_enter_click(self, event):
        # need to add mouse click how active lever
        if event.key in [K_RETURN, K_SPACE]:
            self.player.activate()
        
    def check_to_win(self):
        pass
    

    def check_to_lose(self):
        pass
    
    def losing(self):
        pass
        


    def check_quit_event(self, event):
        if event.type == QUIT:
            pygame.quit()
            sys.exit()