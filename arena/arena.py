from constants import TILE_SIZE, WIDTH
from arena import TILES
from utils import AssetLoader
from entities import Card

import pygame as pg


class Arena:
    def __init__(self, screen, map_name="arena_1") -> None:
        self.screen = screen
        self.cards = []

        self.map = AssetLoader.load_map(map_name)

        self.off_x = (WIDTH - TILE_SIZE * len(self.map[0])) / 2
        self.off_y = TILE_SIZE

        self.surface = pg.Surface(
            (len(self.map[0]) * TILE_SIZE, len(self.map) * TILE_SIZE)
        )
        self.rect = self.surface.get_rect(topleft=(self.off_x, self.off_y))

        self.width = self.surface.get_width()
        self.height = self.surface.get_height()

        for y, row in enumerate(self.map):
            for x, num in enumerate(row):
                tile = TILES[num]
                rect = (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)

                self.surface.blit(tile, rect)

    def check_tile_collide(self) -> bool:
        x, y = pg.mouse.get_pos()
        if (
            self.off_x > x
            or self.off_x + TILE_SIZE * len(self.map[0]) < x
            or self.off_y > y
            or self.off_y + TILE_SIZE * len(self.map) < y
        ):
            return False

        return True

    def draw(self) -> None:
        self.screen.blit(self.surface, (self.off_x, self.off_y))

        for card in self.cards:
            card.draw()

    def spawn(self, hero: Card) -> None:
        self.cards.append(hero)
