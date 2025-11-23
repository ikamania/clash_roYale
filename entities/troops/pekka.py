from entities.card import Card
from constants import COVER_PATH

import pygame as pg


class Pekka(Card):
    def __init__(self, screen: pg.Surface, x: int | float, y: int | float) -> None:
        super().__init__(
            screen = screen,
            x = x,
            y = y,
            name = "Pekka",
            elixir = 7,
            cover_path=f"{COVER_PATH}/pekka.png"
        )
