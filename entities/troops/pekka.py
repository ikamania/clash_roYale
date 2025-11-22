from entities.card import Card

import pygame as pg


class Pekka(Card):
    def __init__(self, screen: pg.Surface, x: int | float, y: int | float) -> None:
        super().__init__(
            screen = screen,
            x = x,
            y = y,
            name = "Pekka",
            elixir = 4,
            cover_path="assets/covers/pekka.png"
        )
