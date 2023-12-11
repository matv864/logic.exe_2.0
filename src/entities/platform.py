import pygame

COLOR_BACKGROUND = (23, 28, 25)

class Platform:
    def __init__(self, config):
        self.game_config = config
        self.vw = self.game_config.platform_module_size[0] / 100
        self.vh = self.game_config.platform_module_size[1] / 100 

        self.platforms = self.game_config.level_config["platforms"]
        self.apple_is_broken = False
        self.apple_pos = 0
        self.max_apple_pos = len(self.platforms)

        self.winning = False

    def draw(self) -> None:
        self.drawing_platforms()
        self.falling_apple()
        


    def drawing_platforms(self):
        main_surf = pygame.Surface(self.game_config.platform_module_size)
        main_surf.fill(COLOR_BACKGROUND)

        
        surf0 = pygame.Surface((15, 15))
        surf0.fill((100, 0, 0))
        surf1 = pygame.Surface((100, 15))
        surf1.fill((0, 100, 0))

        apple = pygame.Surface((30, 30))
        apple.fill((255, 0, 0))

        broken_apple = pygame.Surface((30, 30))
        broken_apple.fill((0, 0, 0))

        for obj in self.platforms:
            if obj["activated"]:
                main_surf.blit(surf1, (0, obj["y"]*self.vh)) 
                # print(obj["object_id"])
            else:
                main_surf.blit(surf0, (0, obj["y"]*self.vh))
        if self.apple_is_broken:
            main_surf.blit(broken_apple, (0, self.platforms[self.apple_pos]["y"]*self.vh)) 
        else:
            main_surf.blit(apple, (0, self.platforms[self.apple_pos]["y"]*self.vh)) 
        


        self.game_config.screen.blit(main_surf, self.game_config.platform_module_location)


    def falling_apple(self):
        counter_of_falling = 0
        if self.platforms[self.apple_pos]["activated"]:
            return
        if self.winning:
            self.game_config.state = "winning"
            print("win")
            return
            # here need animation of falling to portal or other
        for _ in range(self.apple_pos, self.max_apple_pos):
            if self.platforms[self.apple_pos]["activated"]:
                if counter_of_falling >= 2:
                    self.game_config.state = "losing"
                    self.apple_pos = 0
                    self.game_config.update_level_config()
                    print("lose")
                    return 
            else:
                self.apple_pos = min(self.apple_pos + 1, self.max_apple_pos - 1)
                counter_of_falling += 1

        if self.apple_pos >= self.max_apple_pos - 1:
            self.winning = True
            print("winning")


        
        


    '''
        так, тз этого модуля
        надо прописать платформы и падение кристалика (аккуратное/неаккуратное)
        что нужно для платформ:
            отрисовать платформы
            cмоделировать падение
        (все размеры происходят относительно окна модуля и зависят от размеров этого окна, поэтому просто умножай на vw,vh)
        
    '''



