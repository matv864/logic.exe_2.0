import sys
import time
import pygame

from pygame.locals import QUIT, K_LEFT, K_RIGHT, K_a, K_d, K_RETURN, K_SPACE
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
                    self.handle_lefr_right(event)
                    self.handle_enter_click(event)
            
            if self.config.state != "play":
                break

            self.background.draw()
            self.player.draw()
            self.schema.draw()
            self.platform.draw()
            self.score.draw()
            
            pygame.display.update()

            clock.tick(self.config.fps)


    def handle_lefr_right(self, event):
        # print(event.key)
        if event.key in [K_LEFT, K_a, 1073741916]:
            self.player.move_left()
            return
        if event.key in [K_RIGHT, K_d, 1073741918]:
            self.player.move_right()
            return

    def handle_enter_click(self, event):
        # need to add mouse click how active lever
        if event.key in [K_RETURN, K_SPACE]:
            self.player.activate()

    def check_quit_event(self, event):
        if event.type == QUIT:
            pygame.quit()
            sys.exit()