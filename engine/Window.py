import pygame
import threading





class Window:
    def __init__(self):
        pygame.init()
        self.size_screen = (1200, 800)
        self.__screen = pygame.display.set_mode(self.size_screen)
        self.__font = pygame.font.Font("files/font_1.ttf", 40)

        self.render_text = lambda text: self.__font.render(text, False, "Red")

        self.__launch_daemon_game()


    def insert_surface(self, surface_with_coords):
        self.__screen.blit(*surface_with_coords)
        pygame.display.update()



    def __daemon_of_game(self):
        pygame.display.update()
        while True:
            for evevnt in pygame.event.get():
                if evevnt.type == pygame.QUIT:
                    pygame.quit()
                    return

    def __launch_daemon_game(self):
        threading.Thread(target=self.__daemon_of_game).start()

