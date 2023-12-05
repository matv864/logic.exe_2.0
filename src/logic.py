# need to add mouse click how active lever
# need to add check to win or new level


import asyncio
import sys

import pygame
from pygame.locals import QUIT, K_DOWN, K_UP, K_w, K_s, K_RETURN, K_SPACE

from .utils import GameConfig
from .entities import Background, Player, Score, Schema, Platform
# from .utils import Window, Level


class Logic:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("LOGIC2.EXE")
        size_of_screen = (1920, 1200)
        # window = Window(288, 512)
        screen = pygame.display.set_mode(size_of_screen)
        # images = Images()
        self.config = GameConfig(
            screen=screen,
            size_of_screen = size_of_screen
        )

    def start(self):
        self.background = Background(self.config)
        self.player = Player(self.config)
        self.schema = Schema(self.config)
        self.platform = Platform(self.config)
        self.score = Score(self.config)
        self.play()



    def play(self):
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
                print("lose")

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
        if self.config.level_config:
            return False
        return True
    
    def check_to_lose(self):
        return self.config.player_lose


    def check_quit_event(self, event):
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
