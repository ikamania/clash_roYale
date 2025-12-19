from constants import CARD_HEIGHT, CARD_WIDTH, WIDTH, HEIGHT
from entities import Card
from arena import Arena
from .deck import Deck

import pygame as pg


class CardManager:
    def __init__(self, screen: pg.Surface, arena: Arena) -> None:
        self.screen = screen
        self.arena = arena
        self.deck = Deck()
        self.cards: list[Card] = self.load_cards(4)
        self.selected: Card | None = None
        self.clicked = False

    def load_cards(self, count: int) -> list[Card]:
        cards = []
        raw_x = WIDTH / 4
        raw_y = HEIGHT - CARD_HEIGHT - CARD_HEIGHT / 3

        for num in range(count):
            cards.append(
                self.deck.get_next_card()(
                    self.screen, raw_x + (CARD_WIDTH + 5) * num, raw_y
                )
            )
        return cards

    def check_card_select(self, click: bool) -> None:
        self.clicked = click
        mouse_position = pg.mouse.get_pos()

        if not click and self.selected:
            if self.arena.rect.collidepoint(mouse_position):
                self.arena.spawn(self.selected)

                self.load_new_card()
            else:
                self.selected.reset_n_pop_image_location()

            return

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

        self.selected.rect.x = int(mouse_x - self.selected.rect.w / 2)
        self.selected.rect.y = int(mouse_y - self.selected.rect.h / 2)

    def load_new_card(self) -> None:
        if not self.selected:
            return
        self.cards.remove(self.selected)

        new_card = self.deck.get_next_card()(
            self.screen, self.selected.x, self.selected.y
        )
        self.cards.append(new_card)
        self.selected = None

    def draw(self) -> None:
        for card in self.cards:
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
