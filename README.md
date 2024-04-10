# black-borders-around-game

Used here: https://stackoverflow.com/q/68156731#68159521

Adds a black border around the game window, to use it in fullscreen to provide a 1.9.6 pygame-like rendering.

You can put all of these files in a single pygame_border folder, and use it like pygame:

> [!WARNING]\
> Make sure to use `pygame_border.display.blit()` instead of `screen.blit()` when you blit something on the screen.

At this point, only `pygame.draw`, `pygame.display` are rewritten, and you need to manually import each submodule.

I may have missed a function, and something like `get_at()` might not work as expected. Let me know any issue so that I can fix it.

The mouse will be stuck in the drawable window, and everything will act as if you had a tiny screen.
The `(0, 0)` point is not on the top left of the total screen, but on the top left of the drawable window.

```py
# draw the French flag

import pygame

import pygame_border.display
import pygame_border.draw

size = (640, 480)

pygame_border.draw.init(size) # make this module know about the border size

screen = pygame_border.display.set_mode(size)

#---------

screen.fill((255, 255, 255))
pygame_border.draw.rect(screen, (0, 0, 127), pygame.Rect((0, 0), (213, 480)))
pygame_border.draw.rect(screen, (255, 0, 0), pygame.Rect((427, 0), (213, 480)))
pygame_border.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
```
