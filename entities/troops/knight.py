from entities.card import Card

from pygame import Surface


class Knight(Card):
    def __init__(self, screen: Surface, x: int | float, y: int | float) -> None:
        super().__init__(
            screen = screen,
            x = x,
            y = y,
            name = "Knight",
            elixir = 3,
        )
