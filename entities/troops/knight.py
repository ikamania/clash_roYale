from entities.card import Card
from constants import Side

from pygame import Surface


class Knight(Card):
    name = "Knight"
    elixir = 3
    radius = 5

    def __init__(self, screen: Surface, x: int, y: int, side: Side) -> None:
        super().__init__(
            screen=screen,
            x=x,
            y=y,
            side=side,
        )
