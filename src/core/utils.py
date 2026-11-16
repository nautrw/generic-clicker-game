import json
import math
import sys
from pathlib import Path
from typing import TypedDict

import pygame

import src.core.config as Config


def resource(relative_path: str) -> str:
    base_path = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parent.parent))
    return str(base_path / relative_path)


SPRITES_DICT = {
    file.name.removesuffix(".png"): file
    for file in Path(resource("assets")).rglob("*.png")
}
MAPS_DICT = {
    file.name.removesuffix(".json"): file
    for file in Path(resource("maps")).rglob("*.json")
}
FONTS_DICT = {
    file.name.removesuffix(".ttf"): file
    for file in Path(resource("assets/fonts")).rglob("*.ttf")
}
SOUNDS_DICT = {
    file.name.removesuffix(".mp3"): file
    for file in Path(resource("assets/sounds")).rglob("*.mp3")
}

def load_asset(name: str) -> pygame.Surface:
    return pygame.image.load(SPRITES_DICT[name]).convert_alpha()


# fractional scaling isn't supported so size should stay an int
def load_scaled_asset(
    asset_name: str,
    new_size: tuple[int, int] = (Config.GUI_ICON_SIZE, Config.GUI_ICON_SIZE),
) -> pygame.Surface:
    return pygame.transform.scale(load_asset(asset_name), new_size)