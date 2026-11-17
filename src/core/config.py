# Imports
from pathlib import Path

import pygame
from pygame.typing import ColorLike

import src.core.custom_config as CustomConfig
from src.core.themes import THEMES

# Setup
SCREEN_WIDTH: int = 1280
SCREEN_HEIGHT: int = 720
FLAGS: int = pygame.SCALED
FPS: int = 120

GUI_ICON_SIZE: int = 64

if not CustomConfig.THEME in THEMES:
    raise ValueError("invalid theme entered")
THEME_DICT = THEMES[CustomConfig.THEME]
BACKGROUND_COLOR: ColorLike = THEME_DICT["background"]
TEXT_COLOR: ColorLike = THEME_DICT["text"]

BUTTON_NORMAL_BG: ColorLike = "#17151640"
BUTTON_HOVERED_BG: ColorLike = "#171516BF"
BUTTON_PRESSED_BG: ColorLike = "#171516E1"

DARK_BG: ColorLike = "#17151650"

FONT_NORMAL: str = "Oleaguid"
FONT_SIZE_SMALL: int = 24
FONT_SIZE_SMALL: int = 24
FONT_SIZE_MEDIUM: int = 36
FONT_SIZE_LARGE: int = 48
FONT_SIZE_XLARGE: int = 60
FONT_SIZE_XXLARGE: int = 72
FONT_SIZE_XXXLARGE: int = 84

ASSET_PATH: Path = Path("src", "assets")
MAPS_PATH: Path = Path("src", "maps")
FONTS_PATH: Path = Path("src", "assets", "fonts")
SOUNDS_PATH: Path = Path("src", "assets", "sounds")

FONT_SIZE_SMALL: int = 24
FONT_SIZE_SMALL: int = 24
FONT_SIZE_MEDIUM: int = 36
FONT_SIZE_LARGE: int = 48
FONT_SIZE_XLARGE: int = 60
FONT_SIZE_XXLARGE: int = 72
FONT_SIZE_XXXLARGE: int = 84
