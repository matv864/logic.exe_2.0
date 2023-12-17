import pygame
import time

class Losing:
    def __init__(self, config):
        self.game_config = config
        

        self.game_config.lifes -= 1
        print(self.game_config.lifes)

        if self.game_config.lifes == 0:
            self.full_losing()
        else:
            self.temp_death()
        

    def temp_death(self):
        self.main_surf = pygame.Surface(self.game_config.size_of_screen)
        self.main_surf.fill((200, 200, 200))
        self.game_config.screen.blit(self.main_surf, (0, 0))

        self.game_config.update_level_config()

        pygame.display.flip()
        time.sleep(3)
        self.game_config.state = "play"



    def full_losing(self):
        self.game_config.state = "final_losing"
