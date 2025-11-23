from constants import TILE_SIZE, WIDTH
from arena import TILES
from utils import AssetLoader

import pygame as pg


class Arena:
    def __init__(self, screen, map_name="arena_1" ) -> None:
        self.screen = screen

        self.map = AssetLoader.load_map(map_name)

        self.surface = pg.Surface((
            len(self.map[0]) * TILE_SIZE,
            len(self.map) * TILE_SIZE
        ))

        self.off_x = (WIDTH - TILE_SIZE * len(self.map[0])) / 2
        self.off_y = TILE_SIZE

        for y,row in enumerate(self.map):
            for x,num in enumerate(row):
                tile = TILES[num]
                rect = (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)

                self.surface.blit(tile, rect)

    def draw(self) -> None:
        self.screen.blit(self.surface, (self.off_x, self.off_y))

