from constants import NAME, WIDTH, HEIGHT, FPS, Side
from arena import Arena
from ui import CardManager

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
        card_manager = CardManager(WINDOW, arena, Side.PLAYER_1)

        while looping:
            WINDOW.fill("WHITE")

            arena.run()
            card_manager.run()

            pg.display.flip()
            clock.tick(FPS)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                if not pg.display.get_init():
                    looping = False
                    break
                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    card_manager.check_card_select(True)
                if event.type == pg.MOUSEBUTTONUP and event.button == 1:
                    card_manager.check_card_select(False)
