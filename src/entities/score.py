import pygame
import time


class Score:
    def __init__(self, config):
        self.game_config = config

        self.time_from_start = 0
        # print(self.game_config.platform_module_size)
        self.vw = self.game_config.score_module_size[0] / 100
        self.vh = self.game_config.score_module_size[1] / 100

        self.score = 0
        self.start_score = 1000

        

    def update_time(self):
        time_now = time.time()
        real_time_from_start = time_now - self.game_config.start_time
        self.time_from_start = int(real_time_from_start)

    def draw(self) -> None:
        self.update_time()
        # rotated_image = pygame.transform.rotate(self.image, self.rot)
        main_surf = pygame.Surface(self.game_config.score_module_size)
        main_surf.fill((40, 70, 255))

        self.score = max(0, self.start_score - self.time_from_start)
        self.draw_score(main_surf)

        self.game_config.screen.blit(main_surf, self.game_config.score_module_location)




    def draw_score(self, main_surf):
        # self.game_config.level
        # self.game_config.lifes
        # self.score

        font = pygame.font.SysFont(None, 24)
        img = font.render(f"level: {self.game_config.level}", True, "red")
        main_surf.blit(img, (20*self.vw, 50*self.vh))

        font = pygame.font.SysFont(None, 24)
        img = font.render(f"lifes: {self.game_config.lifes}", True, "red")
        main_surf.blit(img, (30*self.vw, 50*self.vh))

        font = pygame.font.SysFont(None, 24)
        img = font.render(f"time: {self.score}", True, "red")
        main_surf.blit(img, (40*self.vw, 50*self.vh))


        '''
        так, тз этого модуля
        надо красиво отверстать скор борд
        (все размеры происходят относительно окна модуля и зависят от размеров этого окна, поэтому просто умножай на vw,vh)
        
        '''



    