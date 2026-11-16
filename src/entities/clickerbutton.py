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
        self.animation_speed = 25

        # self.hover_scale_percent = 0.9
        # self.pressed_scale_percent = 0.75
        self.hover_scale_percent = 1.15
        self.pressed_scale_percent = 0.9
    
    def draw(self, surface: pygame.Surface) -> None:
        assert self.image is not None
        assert self.rect is not None

        surface.blit(self.image, self.rect)

    def update(self, delta_time: float) -> None:
        assert self.rect is not None

        mouse_pressed = pygame.mouse.get_pressed()[0]
        hovered = self.rect.collidepoint(pygame.mouse.get_pos())

        if hovered and mouse_pressed:
            self.target_scale = self.pressed_scale_percent
        elif hovered:
            self.target_scale = self.hover_scale_percent
        else:
            self.target_scale = 1.0

        # rly cool, lowk dk how this works but rly cool
        # self.scale += (self.target_scale - self.scale) * min(
        #     self.animation_speed * delta_time, 1.0
        # )
        self.scale = pygame.math.lerp(
            self.scale,
            self.target_scale,
            min(self.animation_speed * delta_time, 1)
        )

        size = pygame.Vector2(self.original_image.size) * self.scale
        self.image = pygame.transform.smoothscale(
            self.original_image, size
        )
        assert self.image is not None
        self.rect = self.image.get_frect(center=self.rect.center)
