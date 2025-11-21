from constants import TILE_SIZE, WIDTH
from arena import TILE_COLORS

import pygame as pg
import json


class Arena:
    def __init__(self, screen, map_file="data/arena.json" ) -> None:
        self.screen = screen

        with open(map_file) as f:
            data = json.load(f)
        self.map = data["map"]

        self.off_x = (WIDTH - TILE_SIZE * len(self.map[0])) / 2
        self.off_y = TILE_SIZE

    def draw(self) -> None:
        for y, row in enumerate(self.map):
            for x, tile in enumerate(row):
                rect = pg.Rect(
                    x * TILE_SIZE + self.off_x,
                    y * TILE_SIZE + self.off_y,
                    TILE_SIZE,
                    TILE_SIZE,
                )
                pg.draw.rect(self.screen, TILE_COLORS[tile], rect)
