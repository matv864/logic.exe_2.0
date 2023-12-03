import pygame

class Platform:
    def __init__(self, config):
        self.game_config = config
        vw = self.game_config.platform_module_size[0] / 100
        vh = self.game_config.platform_module_size[1] / 100


    def draw(self) -> None:
        # rotated_image = pygame.transform.rotate(self.image, self.rot)
        main_surf = pygame.Surface(self.game_config.platform_module_size)
        main_surf.fill((200, 70, 20))
        self.game_config.screen.blit(main_surf, self.game_config.platform_module_location)


    def activate_this(self, object_id):
        print(f"activate {object_id}")

    