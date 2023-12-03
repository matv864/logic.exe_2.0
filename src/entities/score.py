import pygame



class Score:
    def __init__(self, config):
        self.game_config = config
        self.score = 0
        self.lifes = 0
        self.level = 0
        self.time = 0

    def draw(self) -> None:
        # rotated_image = pygame.transform.rotate(self.image, self.rot)
        main_surf = pygame.Surface(self.game_config.score_module_size)
        main_surf.fill((40, 70, 255))
        self.game_config.screen.blit(main_surf, self.game_config.score_module_location)



    