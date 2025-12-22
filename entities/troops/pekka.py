from entities.card import Card
from constants import Side

from pygame import Surface


class Pekka(Card):
    name = "Pekka"
    elixir = 4
    radius = 100
    speed = 1.3
    range = 10

    def __init__(self, screen: Surface, x: int, y: int, side: Side) -> None:
        super().__init__(
            screen=screen,
            x=x,
            y=y,
            side=side,
        )
