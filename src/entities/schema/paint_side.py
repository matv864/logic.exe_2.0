import pygame

FALSE_ID = -99
    

class Painting:
    def __init__(self, game_config):
        self.game_config = game_config

        self.main_surf = pygame.Surface(self.game_config.schema_module_size) 
        self.main_surf.fill((40, 100, 50)) 

        self.vw = self.game_config.schema_module_size[0] / 100
        self.vh = self.game_config.schema_module_size[1] / 100
        self.vc = (self.vw + self.vh) / 2

        self.size_logic_x = 4 * self.vc
        self.size_logic_y = 4 * self.vc


        self.painting()

    def painting(self):
        for obj in self.game_config.level_config["logic_objects"].values():
            type_logic = obj["type"]
            if type_logic == "splitter":
                for next_id in obj["turn_object"]:
                    self.paint_logic_object(obj, next_id)
            else:
                self.paint_logic_object(obj, obj["turn_object"])

        for obj in self.game_config.level_config["platforms"]:
            self.paint_wire_from_platforms(obj, obj["activate_from_obj_id"])

        self.game_config.screen.blit(self.main_surf, self.game_config.schema_module_location)

    def paint_logic_object(self, obj, next_id):
        surf = pygame.Surface((self.size_logic_x, self.size_logic_y))
        surf.fill((100, 50, 200))
        self.main_surf.blit(surf, (obj["x"] * self.vw, obj["y"] * self.vh))
        if next_id != FALSE_ID:
            # start_pos = (obj["x"] * self.vw, obj["y"] * self.vh)
            next_x = self.game_config.level_config["logic_objects"][str(next_id)]["x"]
            next_y = self.game_config.level_config["logic_objects"][str(next_id)]["y"]
            if obj["y"] == next_y:
                start_pos = (obj["x"] * self.vw + self.size_logic_x, obj["y"] * self.vh + self.size_logic_y / 2)
                end_pos = (next_x * self.vw + self.size_logic_x, next_y * self.vh + self.size_logic_y / 2)
            elif obj["x"] == next_x:
                start_pos = (obj["x"] * self.vw + self.size_logic_x / 2, obj["y"] * self.vh + self.size_logic_y)
                end_pos = (next_x * self.vw + self.size_logic_x / 2, next_y * self.vh + self.size_logic_y)
            else:
                # print("diagonal")
                # print(obj["x"], obj["y"], next_x, next_y)
                start_pos = (obj["x"] * self.vw + self.size_logic_x / 2, obj["y"] * self.vh + self.size_logic_y / 2)
                end_pos = (next_x * self.vw + self.size_logic_x / 2, next_y * self.vh + self.size_logic_y / 2)
            
            if obj["result_signal"]:
                color = (0, 250, 0)
            else:
                color = (0, 0, 0)
            pygame.draw.line(self.main_surf, color, start_pos, end_pos, 1)
            # print(obj["x"], obj["y"], next_x, next_y)
    
    def paint_wire_from_platforms(self, obj, next_id):
        start_x = self.game_config.level_config["logic_objects"][str(next_id)]["x"]
        start_y = self.game_config.level_config["logic_objects"][str(next_id)]["y"]
        start_pos = (start_x * self.vw, start_y * self.vh + self.size_logic_y / 2)
        end_pos = (100 * self.vw, obj["y"] * self.vh + self.size_logic_y / 2)
        if obj["activated"]:
            color = (0, 250, 0)
        else:
            color = (0, 0, 0)
        pygame.draw.line(self.main_surf, color, start_pos, end_pos, 1)

        