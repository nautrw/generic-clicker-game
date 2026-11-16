import math
import pygame

from pygame import sprite
from src.core.utils import load_asset

class ClickerButton(sprite.Sprite):
    def __init__(self, x: float, y: float):
        sprite.Sprite.__init__(self)

        self.original_image = load_asset("click_button")
        assert self.original_image is not None
        self.rect = self.original_image.get_frect(center=(x, y))

        self.image = self.original_image.copy()
        assert self.image is not None

        self.pressed_last_frame = False

        self.scale = 1.0
        self.target_scale = 1.0
        self.min_scale = 0.85
        self.max_scale = 1.15
        self.animation_speed = 25
    
    def draw(self, surface: pygame.Surface) -> None:
        assert self.image is not None
        assert self.rect is not None

        surface.blit(self.image, self.rect)

    def update(self, delta_time: float) -> None:
        assert self.rect is not None

        mouse_pressed = pygame.mouse.get_pressed()[0]
        hovered = self.rect.collidepoint(pygame.mouse.get_pos())

        if hovered:
            self.target_scale = self.min_scale
        else:
            self.target_scale = 1.0

        if mouse_pressed and not self.pressed_last_frame: # noqa: SIM102
            if hovered:
                self.target_scale = self.max_scale

        if self.min_scale - 0.01 <= self.scale >= self.max_scale - 0.01:
            self.target_scale = 1.0

        # rly cool, lowk dk how this works but rly cool
        # NO LIMIT TO THE LERP
        self.scale += (self.target_scale - self.scale) * min(
            self.animation_speed * delta_time, 1.0
        )

        size = pygame.Vector2(self.original_image.size) * self.scale
        self.image = pygame.transform.smoothscale(
            self.original_image, size
        )
        assert self.image is not None
        self.rect = self.image.get_frect(center=self.rect.center)
