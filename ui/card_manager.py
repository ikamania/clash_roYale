from constants import CARD_HEIGHT, CARD_WIDTH 
from entities import Card

import pygame as pg
from utils import AssetLoader


class CardManager:
    def __init__(self, screen: pg.Surface) -> None:
        self.screen = screen
        self.cards: list[Card] = []
        self.selected: Card | None = None
        self.clicked = False

        self.cards = AssetLoader.load_deck(screen)

    def check_card_select(self, click: bool) -> None:
        self.clicked = click
        if not click and self.selected:
            self.selected.rect.y = self.selected.y - 20
            self.selected.rect.x = self.selected.x

            return

        mouse_position = pg.mouse.get_pos()
        for i in range(4):
            card = self.cards[i]

            if card.rect.collidepoint(mouse_position):
                if self.selected:
                    self.selected.rect.y = self.selected.y

                self.selected = card

    def update_selected_card(self) -> None:
        if not self.selected or not self.clicked:
            return
        mouse_x, mouse_y = pg.mouse.get_pos()

        self.selected.rect.x = mouse_x - CARD_WIDTH / 2
        self.selected.rect.y = mouse_y - CARD_HEIGHT / 2

    def draw(self) -> None:
        for i in range(4):
            card = self.cards[i]

            card.draw()

    def run(self) -> None:
        self.update_selected_card()

        self.draw()
