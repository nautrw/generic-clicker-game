import src.core.custom_config as CustomConfig
import src.core.config as Config
from src.gui.container import ElementContainer
from src.gui.button import Button
from src.gui.text import Text
from src.gui.placement_system import RectAnchorMode

def make_building_container(id, x, y, name, cost, amount_owned, points_per_second: int, anchor: RectAnchorMode = RectAnchorMode.TOPLEFT):
    container = ElementContainer(
        id=f"{id}_building_container",
        x=x,
        y=y,
        anchor=anchor,
        width=600,
        height=67
    )
    
    name_text = Text(
        id=f"{id}_text",
        text=name,
        x=Config.ELEMENT_OUTER_PADDING,
        y=Config.ELEMENT_OUTER_PADDING,
        size=Config.FONT_SIZE_SMALL,
    )
    info_text = Text(
        id=f"{id}_info_text",
        text=f"{points_per_second} {CustomConfig.CURRENCY_NAME}/s | {amount_owned} owned",
        x=Config.ELEMENT_OUTER_PADDING,
        y=name_text.rect.bottom,
        size=Config.FONT_SIZE_SMALL,
    )

    buy_button = Button(
        id=f"{id}_buy_button",
        x=container.rect.width - Config.ELEMENT_OUTER_PADDING,
        y=Config.ELEMENT_OUTER_PADDING,
        width=100,
        height=50,
        anchor=RectAnchorMode.TOPRIGHT,  
        text=Text(
            id=f"{id}_buy_button_text",
            text=f"{cost}",
            x=100/2,
            y=50/2,
            size=Config.FONT_SIZE_SMALL,
            anchor=RectAnchorMode.CENTER,
        )
    )
    
    container.add_element(name_text)
    container.add_element(info_text)
    container.add_element(buy_button)

    return container
