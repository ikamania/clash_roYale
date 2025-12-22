from entities.card import Card
from constants import Side

from pygame import Surface


class Knight(Card):
    name = "Knight"
    health = 300.0
    damage = 20.0
    elixir = 3
    radius = 100
    speed = 1.1
    range = 10
    attack_cooldown = 60

    def __init__(self, screen: Surface, x: int, y: int, side: Side) -> None:
        super().__init__(
            screen=screen,
            x=x,
            y=y,
            side=side,
        )
