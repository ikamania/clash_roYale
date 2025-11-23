import json
from pygame import Surface

from constants import ARENA_PATH, DECK_PATH, CARD_WIDTH, CARD_HEIGHT, WIDTH, HEIGHT
from entities import CARD_CLASSES


class AssetLoader:
    @staticmethod
    def load_json(path: str) -> list:
        with open(path) as file:
            return json.load(file)

    @staticmethod
    def load_map(name: str) -> list:
        return AssetLoader.load_json(f"{ARENA_PATH}{name}.json")

    @staticmethod
    def load_deck(screen: Surface) -> list:
        deck_str = AssetLoader.load_json(f"{DECK_PATH}")
        deck_cls = []

        raw_x = WIDTH / 4
        raw_y = HEIGHT - CARD_HEIGHT - CARD_HEIGHT / 3
        for num, card_name in enumerate(deck_str):
            if num < 4:
                x = raw_x + (CARD_WIDTH + 10) * num
            else:
                x = -100

            deck_cls.append(CARD_CLASSES[card_name](
                screen, x, raw_y
            ))
        return deck_cls

