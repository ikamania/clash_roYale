from constants import CARD_HEIGHT, HEIGHT, WIDTH
import pygame as pg


class ElixirBar:
    def __init__(self, screen: pg.Surface) -> None:
        self.screen = screen

        self.w = WIDTH / 1.5
        self.h = 10
        self.off_x = WIDTH / 4
        self.off_y = HEIGHT - CARD_HEIGHT - CARD_HEIGHT / 2

        self.rect = pg.Rect(self.off_x, self.off_y, self.w, self.h)

        self.elixir = 0
        self.time = 0

    def use_elixir(self, count: int) -> None:
        self.elixir -= count

    def draw(self) -> None:
        pg.draw.rect(self.screen, "GRAY", self.rect)
        pg.draw.rect(
            self.screen,
            "BLUE",
            pg.Rect(self.off_x, self.off_y, self.elixir * (self.w / 10), self.h),
        )

    def run(self) -> None:
        self.draw()

        if self.elixir != 10:
            self.time += 1

            if self.time > 100:
                self.elixir += 1
                self.time = 0
