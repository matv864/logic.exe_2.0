import pygame

from .logic_side import Logic_side

class Schema(Logic_side):
    def __init__(self, config):
        self.game_config = config

        self.vw = self.game_config.schema_module_size[0] / 100
        self.vh = self.game_config.schema_module_size[1] / 100

        self.levers = self.game_config.level_config["levers"]
        self.logic_objects = self.game_config.level_config["logic_objects"]
        self.platforms = self.game_config.level_config["platforms"]

        self._queue_objects = []

    def draw(self) -> None:
        self.clear_signals()
        self.watch_lever()
        self.make_schema()
        self.activate_platforms()
        # rotated_image = pygame.transform.rotate(self.image, self.rot)
        main_surf = pygame.Surface(self.game_config.schema_module_size)
        main_surf.fill((0, 0, 0))
        self.game_config.screen.blit(main_surf, self.game_config.schema_module_location)





    def clear_signals(self):
        for item in self.logic_objects.values():
            item["activated"] = dict()
        self._queue_objects = []

    def watch_lever(self):
        random_id = 0
        for lever in self.levers:
            obj_to_activate = self.logic_objects.get(str(lever["turn_object"]))
            if obj_to_activate:
                if lever["activated"]:
                    obj_to_activate["activated"][str(random_id)] = True
                    random_id += 1
                self._queue_objects.append(obj_to_activate)
            else:
                pass
                # print("NO THIS ID", lever["turn_object"])

        

    def make_schema(self):
        random_id = 100
        while self._queue_objects:
            obj = self._queue_objects.pop()
            match obj["type"]:
                case "not":
                    Logic_side.func_not(self.logic_objects, obj, self._queue_objects, random_id)
                case "splitter":
                    Logic_side.func_splitter(self.logic_objects, obj, self._queue_objects, random_id)
                case "node":
                    Logic_side.func_node(self.logic_objects, obj, self._queue_objects, random_id)
                case _:
                    print("no this type", obj["type"])
            random_id += 2
        #     print(obj)
        # print("\n"*2)


                

    def activate_platforms(self):
        for platform in self.platforms:
            platform["activated"] = self.logic_objects[str(platform["activate_from_obj_id"])]["result_signal"]
        #     print(platform)
        # print("\n\n")



    '''
        так, тз этого модуля
        надо прописать отображение логической схемы и красиво сверстать
        что нужно ещё для схемы:
            скомуниздить конфиг левела и отрисовать все элементы
        (все размеры происходят относительно окна модуля и зависят от размеров этого окна, поэтому просто умножай на vw,vh)
        
    '''





    