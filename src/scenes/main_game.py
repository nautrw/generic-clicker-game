import math
from collections import defaultdict
from typing import TYPE_CHECKING

import pygame

import src.core.config as Config
from src.core.buildings import BUILDINGS
from src.core.scenes_manager import Scene
from src.entities.clickerbutton import ClickerButton
from src.gui.button import CUSTOM_BUTTON_CLICKED
from src.gui.container import ElementContainer
from src.gui.gui_manager import GUIManager
from src.gui.placement_system import RectAnchorMode
from src.gui.text import Text
from src.gui.utils import make_building_container

if TYPE_CHECKING:
    from src.app import GameApp


class MainGameSceneGUIManager(GUIManager["MainGameScene"]):
    def update_coin_dependent_ui(self):
        self.get_element_by_id("CoinsDisplay", Text).update_text(
            f"Coins: {self.scene.coins}"
        )

    def refresh(self) -> None:
        self.elements = []

        assert self.scene.click_button.rect is not None

        coins_display = Text(
            id="CoinsDisplay",
            text=f"Coins: {self.scene.coins}",
            x=self.scene.click_button.rect.centerx,
            y=Config.SCREEN_HEIGHT * 0.25,
            anchor=RectAnchorMode.CENTER,
        )

        building_shop_container = ElementContainer(
            id="building_shop_container",
            x=Config.SCREEN_WIDTH / 2,
            y=Config.ELEMENT_OUTER_PADDING,
            width=(Config.SCREEN_WIDTH / 2) - Config.ELEMENT_OUTER_PADDING,
            height=Config.SCREEN_HEIGHT - Config.ELEMENT_OUTER_PADDING * 2,
            border=6,
        )

        # Initial vertical position inside the shop container
        current_y = Config.ELEMENT_OUTER_PADDING * 2

        # Spacing between building buttons
        button_spacing = Config.ELEMENT_OUTER_PADDING

        for name, stats in BUILDINGS.items():
            building_button = make_building_container(
                id=f"{name}_building",
                x=Config.ELEMENT_OUTER_PADDING * 2,
                y=current_y,
                name=name,
                amount_owned=self.scene.buildings_owned[name],
                cost=self.scene.get_building_cost(name),
                points_per_second=stats["coins_per_second"],
            )

            building_shop_container.add_element(building_button)

            # Move the next button below the previous one
            current_y += building_button.height + button_spacing

        self.add_element(coins_display)
        self.add_element(building_shop_container)

    def handle_event(self, event: pygame.Event) -> None:
        if event.type == CUSTOM_BUTTON_CLICKED:  # noqa: SIM102
            if event.button.id.endswith("_building_buy_button"):
                building_name = event.button.id[:-20]
                cost = self.scene.get_building_cost(building_name)

                if self.scene.coins >= cost:
                    self.scene.buildings_owned[building_name] += 1
                    self.scene.coins -= cost

                    self.refresh()


class MainGameScene(Scene):
    def __init__(self, game: "GameApp"):
        super().__init__(game)

        self.click_button = ClickerButton(
            Config.SCREEN_WIDTH * 0.25, Config.SCREEN_HEIGHT / 2
        )

        self.coins = 0
        self.buildings_owned = defaultdict(int)

        self.gui_manager = MainGameSceneGUIManager(self)

    def get_building_cost(self, name: str) -> int:
        building = BUILDINGS[name]
        base_cost = building["base_cost"]
        growth = building["cost_growth"]
        owned = self.buildings_owned[name]
        return math.ceil(base_cost * (growth**owned))

    def handle_events(self, events: list[pygame.Event]) -> None:
        assert self.click_button.rect is not None

        for event in events:
            if (
                event.type == pygame.MOUSEBUTTONDOWN
                and self.click_button.rect.collidepoint(pygame.mouse.get_pos())
            ):
                self.coins += 1
                self.gui_manager.update_coin_dependent_ui()

            self.gui_manager.handle_event(event)

    def render(self, surface: pygame.Surface) -> None:
        self.gui_manager.render_elements(surface)
        self.click_button.draw(surface)

    def update(self, delta_time: float) -> None:
        self.click_button.update(delta_time)

        self.gui_manager.update_elements(delta_time, pygame.mouse.get_pos())
