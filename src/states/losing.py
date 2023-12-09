import pygame
import time

class Losing:
    def __init__(self, config):
        self.config = config
        

        self.config.lifes -= 1
        print(self.config.lifes)

        if self.config.lifes == 0:
            self.full_losing()
        else:
            self.temp_death()
        

    def temp_death(self):
        self.main_surf = pygame.Surface(self.config.size_of_screen)
        self.main_surf.fill((200, 200, 200))
        self.config.screen.blit(self.main_surf, (0, 0))
        pygame.display.update()
        time.sleep(3)
        self.config.state = "play"



    def full_losing(self):
        self.config.state = "final_losing"
