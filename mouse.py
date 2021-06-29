import pygame

def init(size):
    """Send the BORDER_X and BORDER_Y values used by pygame_border.display to this module"""
    
    global BORDER_X, BORDER_Y
    
    info = pygame.display.Info()
    SCREEN_SIZE = (info.current_w, info.current_h)

    BORDER_X = int((SCREEN_SIZE[0] - size[0]) / 2)
    BORDER_Y = int((SCREEN_SIZE[1] - size[1]) / 2)

def get_pos():
    """get_pos() -> (x, y)
get the mouse cursor position
"""
    x, y = pygame.mouse.get_pos()
    return (x - BORDER_X, y - BORDER_Y)

def set_pos(pos):
    """set_pos([x, y]) -> None
set the mouse cursor position
"""
    pygame.mouse.set_pos([pos[0] + BORDER_X, pos[1] + BORDER_Y])
