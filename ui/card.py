from constants import CARD_HEIGHT, CARD_WIDTH
import pygame as pg


class Card:
    def __init__(self, screen: pg.Surface, x: int | float, y: int | float) -> None:
        self.screen = screen
        self.x = x
        self.y = y
        self.rect = pg.Rect(x, y, CARD_WIDTH, CARD_HEIGHT)

    def draw(self) -> None:
        pg.draw.rect(
            self.screen, "RED", self.rect, border_radius=10
        )

