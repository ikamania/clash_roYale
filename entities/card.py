from constants import CARD_HEIGHT, CARD_WIDTH, CARD_IMAGE_PATH, HERO_IMAGE_PATH, Side
import pygame as pg


class Card:
    name: str
    elixir: int
    radius: int

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

        self.card_image = self.load_image(f"{CARD_IMAGE_PATH}/{self.name}.png", True)
        self.hero_image = self.load_image(f"{HERO_IMAGE_PATH}/{self.name}.png", False)

        self.image_n_rect = {
            "CARD": (self.card_image, self.card_image.get_rect(x=x, y=y)),
            "HERO": (self.hero_image, self.hero_image.get_rect(x=x, y=y)),
        }
        self.change_image_n_rect()

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

    def draw(self) -> None:
        image, rect = self.image_n_rect[self.state]

        self.screen.blit(image, rect)
