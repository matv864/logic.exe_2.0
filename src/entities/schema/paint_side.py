import pygame

from ...utils import get_image

FALSE_ID = -99
COLOR_BACKGROUND = (23, 28, 25)
COLOR_WIRE_OFF = (190, 80, 80)
COLOR_WIRE_ON = (133, 222, 126)
WIRE_WIDTH = 5
COEF_RESIZE_IMG = 5
X_POS_LEVER = 10


class Painting:
    def __init__(self, game_config):
        self.game_config = game_config

        self.main_surf = pygame.Surface(self.game_config.schema_module_size)
        self.main_surf.fill(COLOR_BACKGROUND)

        self.vw = self.game_config.schema_module_size[0] / 100
        self.vh = self.game_config.schema_module_size[1] / 100
        self.vc = min(self.vw, self.vh)

        self.logic_objects = self.game_config.level_config["logic_objects"]

        self.painting()

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
        path = f"digits_yellow/dig.{need_digit}.png"
        return self.resize_image(get_image(path))

    def painting(self):
        for obj in self.game_config.level_config["platforms"]:
            self.paint_wire_from_platforms(obj, obj["activate_from_obj_id"])

        for obj in self.game_config.level_config["levers"]:
            self.paint_wire_from_levers(obj, obj["turn_object"])

        for obj in self.game_config.level_config["logic_objects"].values():
            type_logic = obj["type"]

            if type_logic == "splitter":
                for next_id in obj["turn_object"]:
                    self.paint_logic_wire(obj, next_id)
            else:
                self.paint_logic_wire(obj, obj["turn_object"])

        for obj in self.game_config.level_config["logic_objects"].values():
            self.paint_logic_object(obj)

        self.paint_levers()
        self.game_config.screen.blit(
            self.main_surf,
            self.game_config.schema_module_location
        )

    def paint_logic_object(self, obj):

        type_obj = obj["type"]
        match type_obj:
            # case "node":
            #     self.paint_node(obj["x"], obj["y"], obj["result_signal"])
            # case "splitter":
            #     self.paint_node(obj["x"], obj["y"], obj["result_signal"])
            case "not":
                self.paint_not(obj["x"], obj["y"])
            case "or":
                self.paint_or(obj["x"], obj["y"])
            case "and":
                self.paint_and(obj["x"], obj["y"])
            case _:
                pass

    def paint_logic_wire(self, obj, next_id):
        # paint line
        if next_id == FALSE_ID:
            return
            # start_pos = (obj["x"] * self.vw, obj["y"] * self.vh)
        next_x = self.logic_objects[str(next_id)]["x"]
        next_y = self.logic_objects[str(next_id)]["y"]
        start_pos = (
            obj["x"] * self.vw + self.game_config.size_logic_x / 2,
            obj["y"] * self.vh + self.game_config.size_logic_y / 2
        )
        end_pos = (
            next_x * self.vw + self.game_config.size_logic_x / 2,
            next_y * self.vh + self.game_config.size_logic_y / 2
        )
        if self.logic_objects[str(next_id)]["type"] in ["and", "or"]:
            end_pos = (next_x * self.vw, start_pos[1])
        if obj["result_signal"]:
            color = COLOR_WIRE_ON
        else:
            color = COLOR_WIRE_OFF
        pygame.draw.line(
            self.main_surf,
            color,
            start_pos,
            end_pos,
            WIRE_WIDTH
        )
        # print(obj["x"], obj["y"], next_x, next_y)

    def paint_wire_from_platforms(self, obj, next_id):

        start_x = self.logic_objects[str(next_id)]["x"]
        start_y = self.logic_objects[str(next_id)]["y"]
        start_pos = (
            start_x * self.vw + self.game_config.size_logic_x / 2,
            start_y * self.vh + self.game_config.size_logic_y / 2
        )
        end_pos = (
            100 * self.vw,
            obj["y"] * self.vh + self.game_config.size_logic_y / 2
        )
        if obj["activated"]:
            color = COLOR_WIRE_ON
        else:
            color = COLOR_WIRE_OFF
        pygame.draw.line(self.main_surf, color, start_pos, end_pos, WIRE_WIDTH)

    def paint_wire_from_levers(self, obj, next_id):
        end_x = self.logic_objects[str(next_id)]["x"]
        end_y = self.logic_objects[str(next_id)]["y"]
        start_pos = (
            X_POS_LEVER * self.vw,
            obj["y"] * self.vh + self.game_config.size_logic_y / 2
        )
        if self.logic_objects[str(next_id)]["type"] in ["and", "or"]:
            end_pos = (
                end_x * self.vw + self.game_config.size_logic_x / 2,
                obj["y"] * self.vh + self.game_config.size_logic_y / 2
            )
        else:
            end_pos = (
                end_x * self.vw + self.game_config.size_logic_x / 2,
                end_y * self.vh + self.game_config.size_logic_y / 2
            )

        if obj["activated"]:
            color = COLOR_WIRE_ON
        else:
            color = COLOR_WIRE_OFF
        pygame.draw.line(self.main_surf, color, start_pos, end_pos, WIRE_WIDTH)

    def paint_levers(self):
        levers = self.game_config.level_config["levers"]

        for digit, object in enumerate(levers, start=1):
            self.main_surf.blit(
                self.get_resized_digit(digit),
                (X_POS_LEVER * self.vw, object["y"] * self.vh)
            )

# painting logic object

    def paint_not(self, x, y):
        position = (x * self.vw, y * self.vh)
        # print(self.game_config.size_logic_x, self.game_config.size_logic_y)
        image_not = get_image("logic_objects/not.png")
        image_not = self.resize_image(image_not)
        self.main_surf.blit(image_not, position)

    def paint_or(self, x, y):
        position = (x * self.vw, y * self.vh)
        # print(self.game_config.size_logic_x, self.game_config.size_logic_y)
        image_or = get_image("logic_objects/plus.png")
        image_or = self.resize_image(image_or)
        self.main_surf.blit(image_or, position)

    def paint_and(self, x, y):
        position = (x * self.vw, y * self.vh)
        # print(self.game_config.size_logic_x, self.game_config.size_logic_y)
        image_and = get_image("logic_objects/multi.png")
        image_and = self.resize_image(image_and)
        self.main_surf.blit(image_and, position)
