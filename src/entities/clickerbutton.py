import pygame

from pygame import sprite
from src.core.utils import load_asset

class ClickerButton(sprite.Sprite):
    def __init__(self, x: float, y: float):
        sprite.Sprite.__init__(self)

        self.image = load_asset("click_button")
        assert self.image is not None
        self.rect = self.image.get_frect(center=(x, y))
    
    def draw(self, surface: pygame.Surface) -> None:
        assert self.image is not None
        assert self.rect is not None

        surface.blit(self.image, self.rect)