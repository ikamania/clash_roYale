import pygame as pg


class Tower:
    def __init__(self, screen: pg.Surface, x: int, y: int, sprite_path: str) -> None:
        self.screen = screen

        self.image = pg.image.load(sprite_path).convert_alpha()
        self.rect = self.image.get_rect(x=x, y=y)

    def draw(self) -> None:
        self.screen.blit(self.image, self.rect)
