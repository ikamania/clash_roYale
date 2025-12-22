from constants import CARD_HEIGHT, CARD_WIDTH, CARD_IMAGE_PATH, HERO_IMAGE_PATH, Side
from math import hypot
import pygame as pg


class Card:
    name: str
    health: float
    damage: float
    elixir: int
    radius: int
    speed: float
    range: float

    def __init__(
        self,
        screen: pg.Surface,
        x: int,
        y: int,
        side: Side,
    ) -> None:
        self.screen = screen
        self.state = "CARD"
        self.x = x
        self.y = y
        self.side = side
        self.enemy = None
        self.alive = True

        self.card_image = self.load_image(f"{CARD_IMAGE_PATH}/{self.name}.png", True)
        self.hero_image = self.load_image(f"{HERO_IMAGE_PATH}/{self.name}.png", False)

        self.image_n_rect = {
            "CARD": (self.card_image, self.card_image.get_rect(x=x, y=y)),
            "HERO": (self.hero_image, self.hero_image.get_rect(x=x, y=y)),
        }
        self.change_image_n_rect()

    def attack(self) -> None:
        if not self.enemy:
            return

        ex, ey = self.enemy.rect.center

        dx = ex - self.rect.centerx
        dy = ey - self.rect.centery

        distance = hypot(dx, dy)
        if distance <= self.range:
            self.enemy.take_damage(self.damage)

            if not self.enemy.alive:
                self.enemy = None
            return

        dx /= distance
        dy /= distance

        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

    def die(self) -> None:
        self.alive = False

    def take_damage(self, damage: float) -> None:
        self.health -= damage

        if self.health <= 0:
            self.die()

    def deploy(self) -> None:
        self.is_placed = True

    def find_closest_enemy(self, cards_on_arena: list["Card"]) -> None:
        for card in cards_on_arena:
            if card is self:
                continue
            if card.alive and card.side != self.side and self.is_enemy_in_range(card):
                self.enemy = card

    def is_enemy_in_range(self, enemy: "Card") -> bool:
        dx = enemy.rect.centerx - self.rect.centerx
        dy = enemy.rect.centery - self.rect.centery

        distance_sq = dx * dx + dy * dy

        return distance_sq <= self.radius**2

    def load_image(self, path: str, scale: bool) -> pg.Surface:
        image = pg.image.load(path).convert_alpha()
        if scale:
            image = pg.transform.smoothscale(image, (CARD_WIDTH, CARD_HEIGHT))

        return image

    def change_image_n_rect(self) -> None:
        self.state = "CARD" if self.state == "HERO" else "HERO"
        self.rect = self.image_n_rect[self.state][1]

    def reset_n_pop_image_location(self) -> None:
        self.rect.x = self.x
        self.rect.y = self.y - 20

    def reset_image_y(self) -> None:
        self.rect.y = self.y

    def update_state_and_draw(
        self, is_mouse_clicked: bool, is_active: bool, is_over_arena: bool
    ) -> None:
        new_state = (
            "HERO" if is_mouse_clicked and is_active and is_over_arena else "CARD"
        )

        if new_state != self.state:
            self.reset_n_pop_image_location()
            self.change_image_n_rect()

        self.draw()

    def draw(self) -> None:
        image, rect = self.image_n_rect[self.state]

        self.screen.blit(image, rect)

    def run(
        self,
        cards_on_arena: list["Card"],
    ) -> None:
        if not self.alive:
            return

        self.find_closest_enemy(cards_on_arena)
        self.attack()
        self.draw()
