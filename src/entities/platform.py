import pygame
import time

from ..utils import get_image

COLOR_BACKGROUND = (23, 28, 25)
X_POS_CRYSTAL = 33
TUBE_POSITION = (X_POS_CRYSTAL - 5, 80)
SIZE_TUBE = (23, 28)
COEF_RESIZE_IMG = 6.5


class Platform:
    def __init__(self, config):
        self.game_config = config
        self.vw = self.game_config.platform_module_size[0] / 100
        self.vh = self.game_config.platform_module_size[1] / 100

        self.platforms = self.game_config.level_config["platforms"].copy()
        self.platforms.append({
            "y": 74,
            "activated": True
        })
        self.platforms.append({
            "y": 90,
            "activated": True
        })
        self.max_crystall_pos = len(self.platforms)
        self.crystall_is_broken = False

        self.pos_low_platform = 0
        self.y_low_platform = self.platforms[self.pos_low_platform]["y"]

        self.y_position = self.platforms[0]["y"]
        self.crystall_is_broken = False

        self.pos_low_platform = 0
        self.y_low_platform = self.platforms[self.pos_low_platform]["y"]

        self.y_position = self.platforms[0]["y"]

        self.counter_skipped_platforms = 0

        # self.winning = False

    def draw(self) -> None:
        self.draw_background()
        self.draw_platforms()
        if self.crystall_is_broken:
            self.draw_broken_crystall()
            self.game_config.state = "losing"

            self.game_config.screen.blit(
                self.main_surf,
                self.game_config.platform_module_location
            )
            return
        self.falling_crystall()
        self.draw_crystall()
        self.draw_tube()

        self.game_config.screen.blit(
            self.main_surf,
            self.game_config.platform_module_location
        )

    def draw_background(self):
        self.main_surf = pygame.Surface(self.game_config.platform_module_size)
        self.main_surf.fill(COLOR_BACKGROUND)

    def draw_crystall(self):
        crystall = get_image("crystall.png")
        crystall = self.resize_image(crystall)
        # (50, 50)
        self.main_surf.blit(
            crystall,
            (X_POS_CRYSTAL * self.vw, (self.y_position - 3) * self.vh)
        )

    def draw_broken_crystall(self):
        crystall = get_image("crystall.png")
        crystall = self.resize_image(crystall, (5, 5))
        self.main_surf.blit(
            crystall,
            (X_POS_CRYSTAL * self.vw, self.y_position * self.vh)
        )

    def draw_platforms(self):
        platform_on = self.resize_image(get_image("platform_on.png"))
        platform_off = self.resize_image(get_image("platform_off.png"))
        for obj in self.platforms:
            if obj["activated"]:
                self.main_surf.blit(
                    platform_on,
                    (0, obj["y"] * self.vh + self.game_config.size_logic_y / 2)
                )
            else:
                self.main_surf.blit(
                    platform_off,
                    (0, obj["y"] * self.vh + self.game_config.size_logic_y / 2)
                )

    def draw_tube(self):
        tube_sprite = get_image("tube.png")
        tube_sprite = self.resize_image(
            tube_sprite,
            (SIZE_TUBE[0] * self.vw, SIZE_TUBE[1] * self.vh)
        )

        self.main_surf.blit(
            tube_sprite,
            (TUBE_POSITION[0] * self.vw, TUBE_POSITION[1] * self.vh)
        )

    def falling_crystall(self):
        if self.y_position < self.y_low_platform:
            # crystall is flying now
            self.y_position += 1
            return

        if not self.platforms[self.pos_low_platform]["activated"]:
            # crystall is flying now above not activated platform
            self.y_position += 1
            self.pos_low_platform += 1
            self.y_low_platform = self.platforms[self.pos_low_platform]["y"]
            self.counter_skipped_platforms += 1
            return

        # crystall land or situated on activated platform
        if self.counter_skipped_platforms <= 1:
            self.counter_skipped_platforms = 0
            # crystall have good falling && check to win level
            if self.pos_low_platform == self.max_crystall_pos - 2:
                self.platforms.pop(-2)
                self.max_crystall_pos -= 1
                self.pos_low_platform -= 1
                time.sleep(0.5)
                return
            if self.pos_low_platform == self.max_crystall_pos - 1:
                self.game_config.state = "winning"
            return

        # crystall is broken
        self.crystall_is_broken = True

    def resize_image(self, image, sizes=None):
        if sizes:
            return pygame.transform.scale(image, sizes)
        return pygame.transform.scale(
            image,
            (
                image.get_width() * COEF_RESIZE_IMG,
                image.get_height() * COEF_RESIZE_IMG
            )
        )
