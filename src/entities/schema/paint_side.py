import pygame

FALSE_ID = -99
    

class Painting:
    def __init__(self, game_config):
        self.game_config = game_config

        self.main_surf = pygame.Surface(self.game_config.schema_module_size) 
        self.main_surf.fill((40, 100, 50)) 

        self.vw = self.game_config.schema_module_size[0] / 100
        self.vh = self.game_config.schema_module_size[1] / 100
        self.vc = min(self.vw, self.vh)

        self.size_logic_x = 8 * self.vc
        self.size_logic_y = 8 * self.vc


        self.painting()

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

            self.paint_logic_object(obj)

        self.paint_levers()
        self.game_config.screen.blit(self.main_surf, self.game_config.schema_module_location)

    def paint_logic_object(self, obj):

        type_obj = obj["type"]
        match type_obj:
            case "node":
                self.paint_node(obj["x"], obj["y"], obj["result_signal"])
            case "splitter":
                self.paint_node(obj["x"], obj["y"], obj["result_signal"])
            case _:
                surf = pygame.Surface((self.size_logic_x, self.size_logic_y))
                surf.fill((100, 50, 200))
                self.main_surf.blit(surf, (obj["x"] * self.vw, obj["y"] * self.vh))

    def paint_logic_wire(self, obj, next_id):
        # paint line
        if next_id != FALSE_ID:
            # start_pos = (obj["x"] * self.vw, obj["y"] * self.vh)
            next_x = self.game_config.level_config["logic_objects"][str(next_id)]["x"]
            next_y = self.game_config.level_config["logic_objects"][str(next_id)]["y"]
            start_pos = (obj["x"] * self.vw + self.size_logic_x / 2, obj["y"] * self.vh + self.size_logic_y / 2)
            end_pos = (next_x * self.vw + self.size_logic_x / 2, next_y * self.vh + self.size_logic_y / 2)
            if self.game_config.level_config["logic_objects"][str(next_id)]["type"] in ["and", "or"]:
                end_pos = (next_x * self.vw, start_pos[1])
            if obj["result_signal"]:
                color = (0, 250, 0)
            else:
                color = (0, 0, 0)
            pygame.draw.line(self.main_surf, color, start_pos, end_pos, 1)
            # print(obj["x"], obj["y"], next_x, next_y)
    
    def paint_wire_from_platforms(self, obj, next_id):
        start_x = self.game_config.level_config["logic_objects"][str(next_id)]["x"]
        start_y = self.game_config.level_config["logic_objects"][str(next_id)]["y"]
        start_pos = (start_x * self.vw + self.size_logic_x / 2, start_y * self.vh + self.size_logic_y / 2)
        end_pos = (100 * self.vw, obj["y"] * self.vh + self.size_logic_y / 2)
        if obj["activated"]:
            color = (0, 250, 0)
        else:
            color = (0, 0, 0)
        pygame.draw.line(self.main_surf, color, start_pos, end_pos, 1)

    def paint_wire_from_levers(self, obj, next_id):
        end_x = self.game_config.level_config["logic_objects"][str(next_id)]["x"]
        end_y = self.game_config.level_config["logic_objects"][str(next_id)]["y"]
        start_pos = (0, obj["y"] * self.vh + self.size_logic_y / 2)
        if self.game_config.level_config["logic_objects"][str(next_id)]["type"] in ["and", "or"]:
            end_pos = (end_x * self.vw + self.size_logic_x / 2, obj["y"] * self.vh + self.size_logic_y / 2)
        else:
            end_pos = (end_x * self.vw + self.size_logic_x / 2, end_y * self.vh + self.size_logic_y / 2)
        
        if obj["activated"]:
            color = (0, 250, 0)
        else:
            color = (0, 0, 0)
        pygame.draw.line(self.main_surf, color, start_pos, end_pos, 1)


    def paint_levers(self):
        levers = self.game_config.level_config["levers"]
        surf_0 = pygame.Surface((self.size_logic_x, self.size_logic_y))
        surf_0.fill((255, 0, 0))

        surf_1 = pygame.Surface((self.size_logic_x, self.size_logic_y))
        surf_1.fill((0, 255, 0))

        for object in levers:
            if object["activated"]:
                self.main_surf.blit(surf_1, (0, object["y"]*self.vh)) 
            else:
                self.main_surf.blit(surf_0, (0, object["y"]*self.vh)) 

# painting logic object
    def paint_node(self, x, y, activated):
        if activated:
            color = (0, 250, 0)
        else:
            color = (0, 0, 0)
        center_pos = (x * self.vw + self.size_logic_x / 2, y * self.vh + self.size_logic_y / 2)
        pygame.draw.circle(self.main_surf, color, center_pos, 5)