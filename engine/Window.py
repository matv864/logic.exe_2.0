import pygame
import threading





class Window:
    def __init__(self):
        pygame.init()
        self.size_screen = (1200, 800)
        self.__screen = pygame.display.set_mode(self.size_screen)
        self.__font = pygame.font.Font("files/font_1.ttf", 40)
        self.__surface_to_render = pygame.Surface(self.size_screen)
        self.__handlers_on_surface = None

        self.render_text = lambda text: self.__font.render(text, False, "Red")

        self.__launch_daemon_game()

    def set_new_surface(self, surface, handlers):
        self.__surface_to_render = surface
        self.__handlers_on_surface = handlers
        


    def __daemon_of_game(self):
        while True:
            self.__screen.blit(self.__surface_to_render, (0, 0))
            pygame.display.update()
            for evevnt in pygame.event.get():
                if evevnt.type == pygame.QUIT:
                    pygame.quit()
                    return

    def __launch_daemon_game(self):
        threading.Thread(target=self.__daemon_of_game).start()

