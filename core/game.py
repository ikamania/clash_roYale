from constants import NAME, WIDTH, HEIGHT, TILE_SIZE, FPS
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

        while looping:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                if not pg.display.get_init():
                    looping = False
                    break

                pg.display.flip()
                clock.tick(FPS)
