import string
from xml.etree.ElementTree import tostring
from cgitb import text
from pygame.examples.eventlist import font
from src.entities.clickerbutton import ClickerButton
import src.core.config as Config
from typing import TYPE_CHECKING
from src.core.scenes_manager import SceneManager, Scene
import pygame

if TYPE_CHECKING:
    from src.app import GameApp

class MainGameScene(Scene):
    def __init__(self, game: "GameApp"):
        super().__init__(game)

        # Coin Setup
        self.font = pygame.font.SysFont("Arial", 25)

        self.click_button = ClickerButton(Config.SCREEN_WIDTH / 2, Config.SCREEN_HEIGHT / 2)
        self.coins = 0
        
    def handle_events(self, events: list[pygame.Event]) -> None:
        assert self.click_button.rect is not None

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and self.click_button.rect.collidepoint(pygame.mouse.get_pos()):
                self.coins += 1
                print(self.coins)

    def render(self, surface: pygame.Surface) -> None:
        self.click_button.draw(surface)

        text_surface = self.font.render(f"Coins: {str(self.coins)}", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(Config.SCREEN_WIDTH / 2, Config.SCREEN_HEIGHT * .25))

        surface.blit(text_surface, text_rect)

    def update(self, delta_time: float) -> None:
        pass 