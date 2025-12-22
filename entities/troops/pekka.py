from entities.card import Card
from constants import Side

from pygame import Surface


class Pekka(Card):
    name = "Pekka"
    health = 500.0
    damage = 100.0
    elixir = 4
    radius = 100
    speed = 1.6
    range = 10
    attack_cooldown = 200

    def __init__(self, screen: Surface, x: int, y: int, side: Side) -> None:
        super().__init__(
            screen=screen,
            x=x,
            y=y,
            side=side,
        )
