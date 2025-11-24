from constants import CARD_HEIGHT, CARD_WIDTH, WIDTH, HEIGHT
from entities import Card, CARD_CLASSES
from arena import Arena

import pygame as pg
from utils import AssetLoader


class CardManager:
    def __init__(self, screen: pg.Surface, arena: Arena) -> None:
        self.screen = screen
        self.arena = arena
        self.cards: list[Card] = []
        self.selected: Card | None = None
        self.clicked = False
        self.cards = self.load_deck_n_objects()

    def load_deck_n_objects(self) -> list[Card]:
        deck_str = AssetLoader.load_deck()
        deck_cls = []

        raw_x = WIDTH / 4
        raw_y = HEIGHT - CARD_HEIGHT - CARD_HEIGHT / 3
        for num, card_name in enumerate(deck_str):
            if num < 4:
                x = raw_x + (CARD_WIDTH + 5) * num
            else:
                x = -100

            deck_cls.append(CARD_CLASSES[card_name](self.screen, x, raw_y))

        return deck_cls

    def check_card_select(self, click: bool) -> None:
        self.clicked = click
        if not click and self.selected:
            self.selected.reset_n_pop_image_location()

            return

        mouse_position = pg.mouse.get_pos()
        for i in range(4):
            card = self.cards[i]

            if card.rect.collidepoint(mouse_position):
                if self.selected:
                    self.selected.reset_image_y()

                self.selected = card

    def update_selected_card_position(self) -> None:
        if not self.selected or not self.clicked:
            return
        mouse_x, mouse_y = pg.mouse.get_pos()

        self.selected.rect.x = mouse_x - self.selected.rect.w / 2
        self.selected.rect.y = mouse_y - self.selected.rect.h / 2

    def draw(self) -> None:
        for i in range(4):
            card = self.cards[i]

            new_state = (
                "HERO"
                if (
                    self.clicked
                    and card == self.selected
                    and self.arena.check_tile_collide()
                )
                else "CARD"
            )

            if new_state != card.state:
                card.reset_n_pop_image_location()
                card.change_image_n_rect()

            card.draw()

    def run(self) -> None:
        self.update_selected_card_position()

        self.draw()
