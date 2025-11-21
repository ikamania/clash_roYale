from constants import NAME, WIDTH, HEIGHT, TILE_SIZE, FPS
from arena import Arena

import pygame as pg


class Game:
    def __init__(self) -> None:
        pass

    def run(self) -> None:
        pg.init()

        WINDOW = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(NAME)
        clock = pg.time.Clock()

        looping = True

        arena = Arena(WINDOW)

        while looping:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                if not pg.display.get_init():
                    looping = False
                    break
                
                arena.draw()

                pg.display.flip()
                clock.tick(FPS)
