import pygame
from . import window


LOGO_SIZE = ()
MENU_SIZE = (400, 500)
BUTTON_SIZE = (100, 50)

def get_center_coords(parent_coord, child_coord):
    return tuple([parent//2-child//2 for (parent, child) in zip(parent_coord, child_coord)]) 



def make_button(text, button_size):
    button_surface = pygame.Surface(button_size)
    button_surface.fill("Grey")
    text_sur = window.render_text(text)
    button_surface.blit(text_sur, (5, 5))
    return button_surface




def make_menu_buttons():
    menu_surface = pygame.Surface(MENU_SIZE)
    menu_surface.blit(make_button("ok", BUTTON_SIZE), get_center_coords(MENU_SIZE, BUTTON_SIZE))
    return menu_surface, get_center_coords(window.size_screen, MENU_SIZE)

def make_main_surface():
    main_surface = pygame.Surface(window.size_screen)
    main_surface.fill("Blue")

    menu_buttons, coords_menu_buttons = make_menu_buttons()
    main_surface.blit(menu_buttons, coords_menu_buttons)

    return main_surface
    # print(window.size_screen)


def launch():
    window.set_new_surface(make_main_surface(), None)
    



