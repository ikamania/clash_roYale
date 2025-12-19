from utils import AssetLoader
from entities import Card, CARD_CLASSES
from random import shuffle


class Deck:
    def __init__(self) -> None:
        self.index = 0
        self.cards: list[type[Card]] = self.load_cards()

    def load_cards(self) -> list[type[Card]]:
        deck_str = AssetLoader.load_deck()
        deck_cls = []

        for card_name in deck_str:
            deck_cls.append(CARD_CLASSES[card_name])
        shuffle(deck_cls)

        return deck_cls

    def get_next_card(self) -> type[Card]:
        card = self.cards[self.index]

        self.index += 1
        if self.index == 8:
            self.index = 0

        return card
