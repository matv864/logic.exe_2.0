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
        self.lifes = 0
        self.level = 0
        self.time = 0


        

    def update_time(self):
        time_now = time.time()
        real_time_from_start = time_now - self.game_config.start_time
        self.time_from_start = int(real_time_from_start)

    def draw(self) -> None:
        self.update_time()
        # rotated_image = pygame.transform.rotate(self.image, self.rot)
        main_surf = pygame.Surface(self.game_config.score_module_size)
        main_surf.fill((40, 70, 255))



        font = pygame.font.SysFont(None, 24)
        img = font.render(str(self.time_from_start), True, "red")
        main_surf.blit(img, (20*self.vw, 50*self.vh))



        self.game_config.screen.blit(main_surf, self.game_config.score_module_location)

        '''
        так, тз этого модуля
        надо прописать скорборд 
        все значения будут лежать в главном конфиге
        с каждой прорисовкой экрана отрабатывает функция draw
        (все размеры происходят относительно окна модуля и зависят от размеров этого окна, поэтому просто умножай на vw,vh)
        
        '''



    