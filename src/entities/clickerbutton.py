import math

import pygame
from pygame import sprite

import src.core.custom_config as CustomConfig
from src.core.utils import load_asset

CLICKER_BUTTON_ANIMATION_PRESETS: dict[str, dict[str, float]] = {
    "smooth": {
        "hover_scale_percent": 1.1,
        "pressed_scale_percent": 0.9,
        "animation_speed": 18,
    },
    "dramatic": {
        "hover_scale_percent": 1.25,
        "pressed_scale_percent": 0.75,
        "animation_speed": 20,
    },
    "snappy": {
        "hover_scale_percent": 1.1,
        "pressed_scale_percent": 0.9,
        "animation_speed": 40,
    },
    "gentle": {
        "hover_scale_percent": 1.05,
        "pressed_scale_percent": 0.95,
        "animation_speed": 8,
    },
    "reverse": {
        "hover_scale_percent": 0.9,
        "pressed_scale_percent": 1.1,
        "animation_speed": 20,
    },
}


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

        button_animation = CustomConfig.CLICKER_BUTTON_ANIMATION
        if button_animation not in CLICKER_BUTTON_ANIMATION_PRESETS:
            raise ValueError("invalid clicker button animation preset")

        self.hover_scale_percent, self.pressed_scale_percent, self.animation_speed = CLICKER_BUTTON_ANIMATION_PRESETS[button_animation].values()

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
            self.scale, self.target_scale, min(self.animation_speed * delta_time, 1)
        )

        size = pygame.Vector2(self.original_image.size) * self.scale
        self.image = pygame.transform.smoothscale(self.original_image, size)
        assert self.image is not None
        self.rect = self.image.get_frect(center=self.rect.center)
