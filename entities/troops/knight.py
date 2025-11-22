from entities.card import Card

import pygame as pg


class Knight(Card):
    def __init__(self, screen: pg.Surface, x: int | float, y: int | float) -> None:
        super().__init__(
            screen = screen,
            x = x,
            y = y,
            name = "Knight",
            elixir = 3,
            cover_path="assets/covers/knight.png"
        )
