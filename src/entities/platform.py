import time
import pygame

from ..utils import get_image

COLOR_BACKGROUND = (23, 28, 25)

class Platform:
    def __init__(self, config):
        self.game_config = config
        self.vw = self.game_config.platform_module_size[0] / 100
        self.vh = self.game_config.platform_module_size[1] / 100 

        self.platforms = self.game_config.level_config["platforms"]
        self.crystal_is_broken = False
        self.crystal_pos = 0
        self.max_crystal_pos = len(self.platforms)

        self.all_x = 5
        self.now_y = 0
        self.target_y = -1

        self.winning = False

        



    def draw(self) -> None:
        while self.now_y != self.target_y:
            self.draw_background()
            self.drawing_platforms()
            self.falling_crystal()

        self.game_config.screen.blit(self.main_surf, self.game_config.platform_module_location)
        pygame.display.flip()
        
    def draw_background(self):
        self.main_surf = pygame.Surface(self.game_config.platform_module_size)
        self.main_surf.fill(COLOR_BACKGROUND)

    def draw_crystal(self, need_pos):

        crystal = get_image("crystal.png")
        crystal = self.resize_image(crystal, 30, 30)

        broken_crystal = pygame.Surface((30, 30))
        broken_crystal.fill((0, 0, 0))
        
        if self.crystal_is_broken:
            self.main_surf.blit(broken_crystal, (self.all_x * self.vw, need_pos * self.vh)) 
        else:
            self.main_surf.blit(crystal, (self.all_x * self.vw, need_pos * self.vh)) 



    def drawing_platforms(self):
        surf0 = pygame.Surface((15, 15))
        surf0.fill((100, 0, 0))
        surf1 = pygame.Surface((100, 15))
        surf1.fill((0, 100, 0))

        

        for obj in self.platforms:
            if obj["activated"]:
                self.main_surf.blit(surf1, (0, obj["y"] * self.vh + self.game_config.size_logic_y / 2))
            else:
                self.main_surf.blit(surf0, (0, obj["y"] * self.vh + self.game_config.size_logic_y / 2))


        


    def falling_crystal(self):
        last_pos = self.platforms[self.crystal_pos]["y"]
        counter_of_falling = 0
        if self.platforms[self.crystal_pos]["activated"]:
            self.now_y = self.target_y = last_pos
            self.draw_crystal()
        if self.winning:
            self.game_config.state = "winning"
            return
            # here need animation of falling to portal or other
        for _ in range(self.crystal_pos, self.max_crystal_pos):
            if self.platforms[self.crystal_pos]["activated"]:
                if counter_of_falling >= 2:
                    self.game_config.state = "losing"
                    return 
            else:
                self.crystal_pos = min(self.crystal_pos + 1, self.max_crystal_pos - 1)
                counter_of_falling += 1

        if self.crystal_pos >= self.max_crystal_pos - 1:
            self.winning = True
        now_pos = self.platforms[self.crystal_pos]["y"]
        self.now_y = last_pos
        self.target_y = now_pos
        self.draw_animation_falling(last_pos, now_pos)
    

    def draw_animation_falling(self, start, end):
        print(start, end)
        for pos in range(start, end):
            self.draw_crystal(pos)
            time.sleep(0.5)

        
    def resize_image(self, image, x, y):
        return pygame.transform.scale(image, (x, y))


