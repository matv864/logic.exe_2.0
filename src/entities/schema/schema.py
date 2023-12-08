import pygame

from .logic_side import Logic_side
from .paint_side import Painting

class Schema:
    def __init__(self, config):
        self.game_config = config

        self.levers = self.game_config.level_config["levers"]
        self.logic_objects = self.game_config.level_config["logic_objects"]
        self.platforms = self.game_config.level_config["platforms"]

        self._queue_objects = []

        self.broken = False
        self.winning = False

    def draw(self) -> None:
        self.clear_signals()
        self.watch_lever()
        self.make_schema()
        self.activate_platforms()
        Painting(self.game_config)



    def clear_signals(self):
        for item in self.logic_objects.values():
            item["activated"] = dict()
        self._queue_objects = []

    def watch_lever(self):
        for lever in self.levers:
            obj_to_activate = self.logic_objects.get(str(lever["turn_object"]))
            if obj_to_activate:
                obj_to_activate["activated"]["lever: " + str(lever["y"])] = lever["activated"]

                self._queue_objects.append(obj_to_activate)
            else:
                pass
                # print("NO THIS ID", lever["turn_object"])

        

    def make_schema(self):
        while self._queue_objects:
            obj = self._queue_objects.pop()
            match obj["type"]:
                case "not":
                    Logic_side.func_not(self.logic_objects, obj, self._queue_objects)
                case "splitter":
                    Logic_side.func_splitter(self.logic_objects, obj, self._queue_objects)
                case "node":
                    Logic_side.func_node(self.logic_objects, obj, self._queue_objects)
                case "and":
                    Logic_side.func_and(self.logic_objects, obj, self._queue_objects)
                case "or":
                    Logic_side.func_or(self.logic_objects, obj, self._queue_objects)
                case _:
                    print("no this type", obj["type"])
        #     print(obj)
        # print("\n"*2)


                

    def activate_platforms(self):
        for platform in self.platforms:
            obj = self.logic_objects.get(str(platform["activate_from_obj_id"]))
            if obj:
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





    