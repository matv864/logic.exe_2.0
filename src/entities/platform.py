import pygame

class Platform:
    def __init__(self, config):
        self.game_config = config
        self.vw = self.game_config.platform_module_size[0] / 100
        self.vh = self.game_config.platform_module_size[1] / 100 

        self.platforms = self.game_config.level_config["platforms"]

        self.apple_pos = 0
        self.max_apple_pos = len(self.platforms)

    def draw(self) -> None:
        # rotated_image = pygame.transform.rotate(self.image, self.rot)
        main_surf = pygame.Surface(self.game_config.platform_module_size)
        main_surf.fill((200, 70, 20))

        
        surf0 = pygame.Surface((15, 100))
        surf0.fill((100, 0, 0))
        surf1 = pygame.Surface((100, 15))
        surf1.fill((0, 100, 0))
        for obj in self.platforms:
            if obj["activated"]:
                main_surf.blit(surf1, (0, obj["y"]*self.vh)) 
                # print(obj["object_id"])
            else:
                main_surf.blit(surf0, (0, obj["y"]*self.vh)) 


        self.game_config.screen.blit(main_surf, self.game_config.platform_module_location)



    '''
        так, тз этого модуля
        надо прописать платформы и падение кристалика (аккуратное/неаккуратное)
        что нужно для платформ:
            скомуниздить конфиг левела и отрисовать платформы
            активировать платформы по запросу
            моделировать падение
        (систему парсинга json с левелом я ещё не придумал)
        (все размеры происходят относительно окна модуля и зависят от размеров этого окна, поэтому просто умножай на vw,vh)
        
    '''



