import pygame


class Schema:
    def __init__(self, config):
        self.game_config = config

        self.vw = self.game_config.schema_module_size[0] / 100
        self.vh = self.game_config.schema_module_size[1] / 100

    def draw(self) -> None:
        # rotated_image = pygame.transform.rotate(self.image, self.rot)
        main_surf = pygame.Surface(self.game_config.schema_module_size)
        main_surf.fill((0, 0, 0))
        self.game_config.screen.blit(main_surf, self.game_config.schema_module_location)

    def activate_lever(self, lever_id):
        last_state = self.game_config.level_config["levers"][lever_id]["activated"]
        self.game_config.level_config["levers"][lever_id]["activated"] = not(last_state)

        need_to_turn = self.game_config.level_config["levers"][lever_id]["turn_object"]
        print(f"need to activate {need_to_turn}")



    '''
        так, тз этого модуля
        надо прописать отображение логической схемы 
        что нужно для схемы:
            скомуниздить конфиг левела и отрисовать все элементы
            проходить всю логику этой схемы
        (систему парсинга json с левелом я ещё не придумал)
        (все размеры происходят относительно окна модуля и зависят от размеров этого окна, поэтому просто умножай на vw,vh)
        
    '''





    