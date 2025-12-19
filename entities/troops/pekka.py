from entities.card import Card

from pygame import Surface


class Pekka(Card):
    name = "Pekka"
    elixir = 4

    def __init__(self, screen: Surface, x: int, y: int) -> None:
        super().__init__(
            screen=screen,
            x=x,
            y=y,
        )
