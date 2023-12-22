import sys
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
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_mouse_click(event)
                elif event.type == pygame.KEYDOWN:
                    self.handle_lefr_right(event)
                    self.handle_enter_click(event)

            if self.config.state != "play":
                break

            self.background.draw()
            self.player.draw()
            self.schema.draw()
            self.platform.draw()
            self.score.draw()

            pygame.display.flip()

            clock.tick(self.config.fps)

    def check_quit_event(self, event):
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    def handle_lefr_right(self, event):
        # print(event.key)
        # + русские кнопки
        if event.key in [K_LEFT, K_a, 1073741916, 1092]:
            self.player.move_left()
            return
        if event.key in [K_RIGHT, K_d, 1073741918, 1074]:
            self.player.move_right()
            return

    def handle_enter_click(self, event):
        # need to add mouse click how active lever
        if event.key in [K_RETURN, K_SPACE]:
            self.player.activate()

    def handle_mouse_click(self, event):
        self.config.handle_click(event.pos)

# here game cycle in which draw picture
# in every iteration I:
#   catch any clicking or taping
#   call method "draw" in modules
