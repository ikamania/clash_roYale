from constants import CARD_HEIGHT, CARD_WIDTH, WIDTH, HEIGHT, Side
from entities import Card
from arena import Arena
from .deck import Deck
from .elixir_bar import ElixirBar

import pygame as pg


class CardManager:
    def __init__(self, screen: pg.Surface, arena: Arena, side: Side) -> None:
        self.screen = screen
        self.arena = arena
        self.side = side
        self.deck = Deck()
        self.elixir_bar = ElixirBar(self.screen)
        self.cards: list[Card] = self.load_cards(4)
        self.selected: Card | None = None
        self.clicked = False

    def load_cards(self, count: int) -> list[Card]:
        cards = []
        raw_x = int(WIDTH / 4)
        raw_y = int(HEIGHT - CARD_HEIGHT - CARD_HEIGHT / 3)

        for num in range(count):
            cards.append(
                self.deck.get_next_card()(
                    self.screen, raw_x + (CARD_WIDTH + 5) * num, raw_y, self.side
                )
            )
        return cards

    def check_card_select(self, click: bool) -> None:
        self.clicked = click
        mouse_position = pg.mouse.get_pos()

        if not click and self.selected:
            if (
                self.selected.elixir <= self.elixir_bar.elixir
                and self.arena.rect.collidepoint(mouse_position)
            ):
                self.arena.spawn(self.selected)
                self.elixir_bar.use_elixir(self.selected.elixir)

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
            self.screen, self.selected.x, self.selected.y, self.side
        )
        self.cards.append(new_card)
        self.selected = None

    def loop_through_cards(self):
        collide = self.arena.check_tile_collide()

        for card in self.cards:
            card.run(
                self.arena.cards,
                self.clicked,
                card == self.selected,
                collide,
            )

    def run(self) -> None:
        self.update_selected_card_position()

        self.elixir_bar.run()
        self.loop_through_cards()
