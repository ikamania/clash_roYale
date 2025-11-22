from constants import CARD_HEIGHT, CARD_WIDTH
import pygame as pg


class Card:
    def __init__(
        self,
        screen: pg.Surface,
        x: int | float,
        y: int | float,
        name: str,
        elixir: int,
        cover_path: str
    ) -> None:
        self.screen = screen
        self.x = x
        self.y = y
        self.rect = pg.Rect(x, y, CARD_WIDTH, CARD_HEIGHT)

        self.cover_image = pg.image.load(cover_path).convert_alpha()
        self.cover_image = pg.transform.smoothscale(
            self.cover_image, (CARD_WIDTH, CARD_HEIGHT)
        )

    def draw(self) -> None:
        self.screen.blit(self.cover_image, self.rect)

