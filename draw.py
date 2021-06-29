import pygame

def init(size):
    """Send the BORDER_X and BORDER_Y values used by pygame_border.display to this module"""
    
    global BORDER_X, BORDER_Y
    
    info = pygame.display.Info()
    SCREEN_SIZE = (info.current_w, info.current_h)

    BORDER_X = int((SCREEN_SIZE[0] - size[0]) / 2)
    BORDER_Y = int((SCREEN_SIZE[1] - size[1]) / 2)

def rect(*args):
    """rect(surface, color, rect) -> Rect
rect(surface, color, rect, width=0, border_radius=0, border_top_left_radius=-1, border_top_right_radius=-1, border_bottom_left_radius=-1, border_bottom_right_radius=-1) -> Rect
draw a rectangle
"""
    args = list(args)
    args[2].x += BORDER_X
    args[2].y += BORDER_Y
    
    rect = pygame.draw.rect(*args)
    rect.x -= BORDER_X
    rect.y -= BORDER_Y
    return rect

def polygon(surface, color, points, width=0):
    """polygon(surface, color, points) -> Rect
polygon(surface, color, points, width=0) -> Rect
draw a polygon
"""
    for x in range(len(points)):
        points[x] = list(points[x])
        points[x][0] += BORDER_X
        points[x][1] += BORDER_Y
    
    rect = pygame.draw.polygon(surface, color, points, width)
    rect.x -= BORDER_X
    rect.y -= BORDER_Y
    return rect

def circle(*args):
    """circle(surface, color, center, radius) -> Rect
circle(surface, color, center, radius, width=0, draw_top_right=None, draw_top_left=None, draw_bottom_left=None, draw_bottom_right=None) -> Rect
draw a circle
"""
    args = list(args)
    args[2] = list(args[2])
    args[2][0] += BORDER_X
    args[2][1] += BORDER_Y
    
    rect = pygame.draw.circle(*args)
    rect.x -= BORDER_X
    rect.y -= BORDER_Y
    return rect

def ellipse(surface, color, rect, width=0):
    """ellipse(surface, color, rect) -> Rect
ellipse(surface, color, rect, width=0) -> Rect
draw an ellipse
"""
    rect.x += BORDER_X
    rect.y += BORDER_Y
    
    rect = pygame.draw.ellipse(surface, color, rect, width)
    rect.x -= BORDER_X
    rect.y -= BORDER_Y
    return rect

def arc(*args):
    """arc(surface, color, rect, start_angle, stop_angle) -> Rect
arc(surface, color, rect, start_angle, stop_angle, width=1) -> Rect
draw an elliptical arc
"""
    args = list(args)
    args[2].x += BORDER_X
    args[2].y += BORDER_Y
    
    rect = pygame.draw.arc(*args)
    rect.x -= BORDER_X
    rect.y -= BORDER_Y
    return rect

def line(*args):
    """line(surface, color, start_pos, end_pos, width) -> Rect
line(surface, color, start_pos, end_pos, width=1) -> Rect
draw a straight line
"""
    args = list(args)
    args[2].x += BORDER_X
    args[2].y += BORDER_Y
    args[3].x += BORDER_X
    args[3].y += BORDER_Y
    
    rect = pygame.draw.line(*args)
    rect.x -= BORDER_X
    rect.y -= BORDER_Y
    return rect

def lines(*args):
    """lines(surface, color, closed, points) -> Rect
lines(surface, color, closed, points, width=1) -> Rect
draw multiple contiguous straight line segments
"""
    args = list(args)
    
    for x in range(len(args[3])):
        args[3][x] = list(args[3][x])
        args[3][x][0] += BORDER_X
        args[3][x][1] += BORDER_Y
    
    rect = pygame.draw.lines(*args)
    rect.x -= BORDER_X
    rect.y -= BORDER_Y
    return rect

def aaline(*args):
    """aaline(surface, color, start_pos, end_pos) -> Rect
aaline(surface, color, start_pos, end_pos, blend=1) -> Rect
draw a straight antialiased line
"""
    args = list(args)
    args[2].x += BORDER_X
    args[2].y += BORDER_Y
    args[3].x += BORDER_X
    args[3].y += BORDER_Y
    
    rect = pygame.draw.aaline(*args)
    rect.x -= BORDER_X
    rect.y -= BORDER_Y
    return rect

def aalines(*args):
    """aalines(surface, color, closed, points) -> Rect
aalines(surface, color, closed, points, blend=1) -> Rect
draw multiple contiguous straight antialiased line segments
"""
    args = list(args)
    
    for x in range(len(args[3])):
        args[3][x] = list(args[3][x])
        args[3][x][0] += BORDER_X
        args[3][x][1] += BORDER_Y
    
    rect = pygame.draw.aalines(*args)
    rect.x -= BORDER_X
    rect.y -= BORDER_Y
    return rect
