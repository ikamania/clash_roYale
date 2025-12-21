from enum import Enum, auto

NAME = "clash roYale"
TILE_SIZE = 20
CARD_WIDTH = 70
CARD_HEIGHT = 90
WIDTH = 22 * TILE_SIZE
HEIGHT = 36 * TILE_SIZE
FPS = 60
ASSETS_PATH = "assets/sprites/arena/"
CARD_IMAGE_PATH = "assets/covers"
HERO_IMAGE_PATH = "assets/sprites/troops"
ARENA_PATH = "data/"
DECK_PATH = "data/deck.json"


class Side(Enum):
    PLAYER_1 = auto()
    PLAYER_2 = auto()
