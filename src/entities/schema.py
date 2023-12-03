import pygame


class Schema:
    def __init__(self, config):
        self.game_config = config

    def draw(self) -> None:
        # rotated_image = pygame.transform.rotate(self.image, self.rot)
        main_surf = pygame.Surface(self.game_config.schema_module_size)
        main_surf.fill((0, 0, 0))
        self.game_config.screen.blit(main_surf, self.game_config.schema_module_location)



    