import pygame

screen = None
pygame.init()

def set_mode(window_size, flags=0, depth=0, display=0, vsync=0):
    """set_mode(size=(0, 0), flags=0, depth=0, display=0, vsync=0) -> Surface
Initialize a window or screen for display

Your entire screen will be used, but you will only be able to draw in the center part.
The black borders around the game window kind of do not exist.
The actual window in which you can draw is the center part, without the black borders.
So the (0, 0) point is not at the top left of your screen, it is actually on the top left of the drawable window.
"""

    global SCREEN_SIZE, BORDER_X, BORDER_Y, screen
    
    info = pygame.display.Info()
    SCREEN_SIZE = (info.current_w, info.current_h)
    WINDOW_SIZE = window_size # the window size you want
    screen = pygame.display.set_mode(SCREEN_SIZE, flags, depth, display, vsync)

    if WINDOW_SIZE[0] > SCREEN_SIZE[0]:
        raise ValueError("The border is wider than the screen")
    if WINDOW_SIZE[1] > SCREEN_SIZE[1]:
        raise ValueError("The border is taller than the screen")

    BORDER_X = int((SCREEN_SIZE[0] - WINDOW_SIZE[0]) / 2)
    BORDER_Y = int((SCREEN_SIZE[1] - WINDOW_SIZE[1]) / 2)

    return screen

def draw_borders():
    """This function is automatically called by pygame_border.display.flip() and pygame_border.display.update().
It simply draws the borders around the drawable screen, to mask anything that could go out of it.
Also, this function keeps the mouse in the drawable screen."""
    
    assert screen is not None, "You must call pygame_border.display.set_mode() before using this function"

    x, y = pygame.mouse.get_pos()
    w, h = screen.get_size()
    x = min(w + BORDER_X, max(BORDER_X, x))
    y = min(h + BORDER_Y, max(BORDER_Y, y))
    pygame.mouse.set_pos((x, y))
    
    rects = [pygame.Rect((0, 0), (w, BORDER_Y)),
             pygame.Rect((0, h - BORDER_Y), (w, BORDER_Y)),
             pygame.Rect((0, BORDER_Y), (BORDER_X, h - 2 * BORDER_Y)),
             pygame.Rect((w - BORDER_X, BORDER_Y), (BORDER_X, h - 2 * BORDER_Y))]

    for rect in rects:
        pygame.draw.rect(screen, (0, 0, 0), rect)

def flip():
    """flip() -> None
Update the full display Surface to the screen"""
    draw_borders()
    pygame.display.flip()

def update(*args):
    """update(rectangle=None) -> None
update(rectangle_list) -> None
Update portions of the screen for software displays
"""
    draw_borders()
    if len(args):
        rectangle_list = list(args)
        for x in range(len(rectangle_list)):
            rectangle_list[x].x = rectangle_list[x].x + BORDER_X
            rectangle_list[x].y = rectangle_list[x].y + BORDER_Y
        pygame.display.update(rectangle_list)
    else:
        pygame.display.update()

def blit(surface, pos):
    """blit(source, dest, area=None, special_flags=0) -> Rect
draw one image onto another
"""
    rect = screen.blit(surface, (pos[0] + BORDER_X, pos[1] + BORDER_Y))
    rect.x -= BORDER_X
    rect.y -= BORDER_Y
    return rect
