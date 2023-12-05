import pygame

def paint_object(screen, vw, vh, obj):
    surf = pygame.Surface((10, 10))
    surf.fill((100, 50, 200))
    screen.blit(surf, (obj["x"]*vw, obj["y"]*vh)) 

    

class Paint_side:
    


    @staticmethod
    def paint_elements(screen: pygame.Surface, vw, vh, logic_objects):
        for obj in logic_objects:
            paint_object(screen, vw, vh, obj)
        