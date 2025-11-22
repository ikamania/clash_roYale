from constants import ASSETS_PATH, TILE_SIZE
import pygame as pg
import os

EMPTY = 0
GRASS_1 = 1
GRASS_2 = 2
CONCRETE_1 = 3
CONCRETE_2 = 4


def load_image(name: str) -> pg.Surface:
    path = os.path.join(ASSETS_PATH, name)

    return pg.image.load(path)


def color_surface(color: tuple) -> pg.Surface:
    surface = pg.Surface((TILE_SIZE, TILE_SIZE))
    surface.fill(color)

    return surface


TILES = {
    EMPTY: color_surface((0, 128, 0)),
    GRASS_1: color_surface((34, 177, 76)),
    GRASS_2: color_surface((0, 100, 0)),
    CONCRETE_1: color_surface((150, 150, 150)),
    CONCRETE_2: color_surface((110, 110, 110)),
}
