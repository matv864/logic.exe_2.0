import time
import pygame

from ..utils import get_image



class Player(pygame.sprite.Sprite):
    def __init__(self, config) -> None:
        self.game_config = config

        self.vw = self.game_config.player_module_size[0] / 100
        self.vh = self.game_config.player_module_size[1] / 100

        self.player_avatar = get_image("pngwing.com.png")
        self.animation = [get_image("anim1.png"), get_image("anim2.png")]
        self.framenum = 0
        self.image_change_interval = 2*self.vh

        self.rect = self.image.get_rect()

        self.player_pos = 0
        self.levers = self.game_config.level_config["levers"]

    def draw(self) -> None:
        # rotated_image = pygame.transform.rotate(self.image, self.rot)
        main_surf = pygame.Surface(self.game_config.player_module_size)
        main_surf.fill((0, 255, 120))

        # surf_player = pygame.Surface((20, 20))
        # surf_player.fill((255, 255, 255))
        main_surf.blit(self.image,(self.game_config.player_module_size[0]/6, self.levers[self.player_pos]["y"]*self.vh-3*self.vh))
        self.move_to(main_surf, 3*self.vh,40*self.vh)
        surf_0 = pygame.Surface((20, 20))
        surf_0.fill((255, 0, 0))

        surf_1 = pygame.Surface((20, 20))
        surf_1.fill((0, 255, 0))
        for object in self.levers:
            if object["activated"]:
                main_surf.blit(surf_1, (self.game_config.player_module_size[0]/3, object["y"]*self.vh)) 
            else:
                main_surf.blit(surf_0, (self.game_config.player_module_size[0]/3, object["y"]*self.vh))
            # print(object["y"]*self.vh)
        # main_surf.blit(surf_player, (self.game_config.player_module_size[0]/3, self.levers[self.player_pos]["y"]*self.vh)) 
        
        


        self.game_config.screen.blit(main_surf, self.game_config.player_module_location)
    def move_to(self,main_surf, start_pos, end_pos):
        for i in range(8):
            self.counter += 1
            if self.counter == self.image_change_interval:
                self.current_frame = (self.current_frame + 1) % 2
                self.image = self.animation[self.current_frame]
                self.counter = 0
            time.sleep(1)
        

    def move_up(self):
        self.player_pos = max(0, self.player_pos - 1)

    def move_down(self):
        self.player_pos = min(len(self.levers)-1, self.player_pos + 1)

    def activate(self):
        self.levers[self.player_pos]["activated"] = not(self.levers[self.player_pos]["activated"])
        print(f"activated {self.player_pos}")
    

    '''
        так, тз этого модуля
        надо верстать
        (все размеры происходят относительно окна модуля и зависят от размеров этого окна, поэтому просто умножай на vw,vh)
        
    '''

