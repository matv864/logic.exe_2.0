import time
import pygame




class Player:
    def __init__(self, config) -> None:
        self.game_config = config

        self.vw = self.game_config.player_module_size[0] / 100
        self.vh = self.game_config.player_module_size[1] / 100

        self.player_pos = 0
        self.levers = self.game_config.level_config["levers"]

    def draw(self) -> None:
        # rotated_image = pygame.transform.rotate(self.image, self.rot)
        main_surf = pygame.Surface(self.game_config.player_module_size)
        main_surf.fill((0, 255, 120))

        surf_player = pygame.Surface((50, 50))
        surf_player.fill((255, 255, 255))

        surf_0 = pygame.Surface((50, 50))
        surf_0.fill((255, 0, 0))

        surf_1 = pygame.Surface((50, 50))
        surf_1.fill((0, 255, 0))

        for object in self.levers:
            if object["activated"]:
                main_surf.blit(surf_1, (self.game_config.player_module_size[0]/3, object["y"]*self.vh)) 
            else:
                main_surf.blit(surf_0, (self.game_config.player_module_size[0]/3, object["y"]*self.vh))
        main_surf.blit(surf_player, (self.game_config.player_module_size[0]/3, self.levers[self.player_pos]["y"]*self.vh)) 
        
        


        self.game_config.screen.blit(main_surf, self.game_config.player_module_location)

    def move_up(self):
        self.player_pos = max(0, self.player_pos - 1)

    def move_down(self):
        self.player_pos = min(len(self.levers)-1, self.player_pos + 1)

    def activate(self):
        return self.player_pos
    

    '''
        так, тз этого модуля
        надо верстать
        (все размеры происходят относительно окна модуля и зависят от размеров этого окна, поэтому просто умножай на vw,vh)
        
    '''

