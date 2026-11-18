from pygame.typing import ColorLike

THEMES: dict[str, dict[str, ColorLike]] = {
    "dark": {
        "background": "#101010",
        "container_bg": "#FFFFFF4B",
        "text": "#F5F5F5",

        "button_normal_bg": "#383838",
        "button_hovered_bg": "#484848",
        "button_pressed_bg": "#292929",

        "button_green_bg": "#287A45",
        "button_green_hovered_bg": "#329653",
        "button_green_pressed_bg": "#1E6036",

        "border_color": "#FFFFFF18",
    },
    "light": {
        "background": "#F0F0F0",
        "container_bg": "#00000008",
        "text": "#171717",

        "button_normal_bg": "#C7C7C7",
        "button_hovered_bg": "#AAAAAA",
        "button_pressed_bg": "#969696",

        "button_green_bg": "#34834D",
        "button_green_hovered_bg": "#419C5D",
        "button_green_pressed_bg": "#28683D",

        "border_color": "#00000018",
    },
}
