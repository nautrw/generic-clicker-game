from src.gui.placement_system import RectAnchorMode
from cmath import rect
from src.gui.text import Text
from src.gui.gui_manager import GUIManager
from src.entities.clickerbutton import ClickerButton
import src.core.config as Config
from typing import TYPE_CHECKING
from src.core.scenes_manager import SceneManager, Scene
import pygame
from src.gui.container import ElementContainer

if TYPE_CHECKING:
    from src.app import GameApp

class MainGameSceneGUIManager(GUIManager["MainGameScene"]):
    def update_coin_dependent_ui(self):
        self.get_element_by_id("CoinsDisplay", Text).update_text(f"Coins: {self.scene.coins}")
        
    def refresh(self) -> None:
        self.elements = []
        
        assert self.scene.click_button.rect is not None
        coins_display = Text(
            id="CoinsDisplay",
            text=f"Coins: {self.scene.coins}",
            x=self.scene.click_button.rect.centerx,
            y=Config.SCREEN_HEIGHT * .25,
            anchor=RectAnchorMode.CENTER
        )

        building_shop_container = ElementContainer(
            id="building_shop_container",
            x=Config.SCREEN_WIDTH / 2,
            y=Config.ELEMENT_OUTER_PADDING,
            width=(Config.SCREEN_WIDTH / 2) - Config.ELEMENT_OUTER_PADDING,
            height=Config.SCREEN_HEIGHT - Config.ELEMENT_OUTER_PADDING * 2,
            border=6,
        )
        
        self.add_element(coins_display)
        self.add_element(building_shop_container)
    
    def handle_event(self, event: pygame.Event) -> None:
        pass

class MainGameScene(Scene):
    def __init__(self, game: "GameApp"):
        super().__init__(game)

        self.click_button = ClickerButton(Config.SCREEN_WIDTH * .25, Config.SCREEN_HEIGHT / 2)
        self.coins = 0
        self.gui_manager = MainGameSceneGUIManager(self)
        
    def handle_events(self, events: list[pygame.Event]) -> None:
        assert self.click_button.rect is not None

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and self.click_button.rect.collidepoint(pygame.mouse.get_pos()):
                self.coins += 1
                self.gui_manager.update_coin_dependent_ui()

            self.gui_manager.handle_event(event)

    def render(self, surface: pygame.Surface) -> None:
        self.gui_manager.render_elements(surface)

        self.click_button.draw(surface)

    def update(self, delta_time: float) -> None:
        self.click_button.update(delta_time)

        self.gui_manager.update_elements(delta_time, pygame.mouse.get_pos())
