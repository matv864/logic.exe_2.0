import pygame

from ..utils import get_image, get_gif, get_font

TEXT_RESET = '''сбросить результат'''

BLUE = (100, 50, 200)
COLOR_BACKGROUND = (106, 117, 111)
COLOR_MIDLINE = (65, 65, 65)
COEF_RESIZE_IMG = 6


class Player(pygame.sprite.Sprite):
    def __init__(self, config) -> None:
        self.game_config = config

        self.vw = self.game_config.player_module_size[0] / 100
        self.vh = self.game_config.player_module_size[1] / 100
        self.vc = min(self.vw, self.vh)

        self.pixel_font = get_font("pixel.ttf", int(self.vc * 15))

        # self.rect = self.image.get_rect()
        self.girl_gif = get_gif("right_girl.gif")
        self.frame_girl_index = 0
        self.sped_gif = 5

        self.player_pos = 0
        self.levers = self.game_config.level_config["levers"]

        self.y_lever_position = 68
        self.y_digit_position = 43

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

    def get_resized_digit(self, need_digit):
        path = f"digits_green/dig.{need_digit}.png"
        return self.resize_image(get_image(path))

    def draw(self) -> None:
        self.draw_background()
        self.draw_girl()
        self.draw_levers_and_digits()
        self.draw_button_help()

        self.game_config.screen.blit(
            self.main_surf,
            self.game_config.player_module_location
        )

    def draw_background(self):
        self.main_surf = pygame.Surface(self.game_config.player_module_size)
        self.main_surf.fill(COLOR_BACKGROUND)
        midline = pygame.Surface((100 * self.vw, 5 * self.vh))
        midline.fill(COLOR_MIDLINE)
        self.main_surf.blit(midline, (0 * self.vw, 96 * self.vh))

    def draw_girl(self):
        girl = self.girl_gif[self.frame_girl_index // self.sped_gif]
        girl = self.resize_image(girl)
        self.main_surf.blit(
            girl,
            (5 * self.vw, 95 * self.vh - girl.get_height())
        )
        self.frame_girl_index = (self.frame_girl_index + 1) % \
            (len(self.girl_gif) * self.sped_gif)

    def draw_selected_now(self):
        first_pos = 15
        now_player_pos = first_pos + 10 * self.player_pos

        player_obvodka = get_image("obvodka.png")
        player_obvodka = self.resize_image(player_obvodka)
        self.main_surf.blit(
            player_obvodka,
            (
                (now_player_pos - 0.4) * self.vw,
                (self.y_lever_position - 1.3) * self.vh
            )
        )

    def draw_levers_and_digits(self):
        self.draw_selected_now()

        now_pos = 15

        lever_off = get_image("lever_off.png")
        lever_off = self.resize_image(lever_off)

        lever_on = get_image("lever_on.png")
        lever_on = self.resize_image(lever_on)

        for digit, object in enumerate(self.levers, start=1):
            if object["activated"]:
                self.main_surf.blit(
                    lever_off,
                    (now_pos * self.vw, self.y_lever_position * self.vh)
                )
            else:
                self.main_surf.blit(
                    lever_on,
                    (now_pos * self.vw, self.y_lever_position * self.vh)
                )
            self.main_surf.blit(
                self.get_resized_digit(digit),
                (now_pos * self.vw, self.y_digit_position * self.vh)
            )
            now_pos += 10

    def draw_button_help(self):
        button = self.pixel_font.render(TEXT_RESET, True, BLUE)
        surf_to_text = pygame.Surface((int(22 * self.vw), int(20 * self.vh)))
        surf_to_text.fill(COLOR_MIDLINE)
        surf_to_text.blit(button, (10, 0))
        self.main_surf.blit(
            surf_to_text,
            (
                78 * self.vw,
                77 * self.vh
            )
        )

        coords_button = (
            78 * self.vw,
            77 * self.vh,
            (78 + 22) * self.vw,
            (77 + 20) * self.vh
        )

        self.game_config.buttons[coords_button] = \
            lambda config: (config.set_state("greeting"))

    # logic part ---------------------------
    def move_left(self):
        self.player_pos = max(0, self.player_pos - 1)

    def move_right(self):
        self.player_pos = min(len(self.levers) - 1, self.player_pos + 1)

    def activate(self):
        self.levers[self.player_pos]["activated"] = \
            not (self.levers[self.player_pos]["activated"])
    # logic part end ------------------------
