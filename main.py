import pygame
from pygame.locals import *

BORDER_X = 100
BORDER_Y = 70
SCREEN_SIZE = (640, 480)
# if you change these values, call Display.__init__() again

if BORDER_X * 2 >= SCREEN_SIZE[0]:
    raise ValueError("The border is wider than the screen")
if BORDER_Y * 2 >= SCREEN_SIZE[1]:
    raise ValueError("The border is taller than the screen")

class Display:
    def __init__(self, color=(0, 0, 0)):
        self.color = color
        self.rects = [Rect((0, 0), (SCREEN_SIZE[0], BORDER_Y)),
                      Rect((0, SCREEN_SIZE[1] - BORDER_Y), (SCREEN_SIZE[0], BORDER_Y)),
                      Rect((0, BORDER_Y), (BORDER_X, SCREEN_SIZE[1] - 2 * BORDER_Y)),
                      Rect((SCREEN_SIZE[0] - BORDER_X, BORDER_Y), (BORDER_X, SCREEN_SIZE[1] - 2 * BORDER_Y))]

    def _draw_borders(self):
        for rect in self.rects:
            pygame.draw.rect(screen, self.color, rect)

    def flip(self):
        self._draw_borders()
        pygame.display.flip()

    def update(self, *args):
        self._draw_borders()
        pygame.display.update(*args)

def blit(surface, pos):
    screen.blit(surface, (pos[0] + BORDER_X, pos[1] + BORDER_Y))

screen = pygame.display.set_mode(SCREEN_SIZE)

display = Display()

# main loop here
