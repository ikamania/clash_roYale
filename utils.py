import json

from constants import ARENA_PATH, DECK_PATH


class AssetLoader:
    @staticmethod
    def load_json(path: str) -> list:
        with open(path) as file:
            return json.load(file)

    @staticmethod
    def load_map(name: str) -> list:
        return AssetLoader.load_json(f"{ARENA_PATH}{name}.json")

    @staticmethod
    def load_deck() -> list[str]:
        return AssetLoader.load_json(f"{DECK_PATH}")
