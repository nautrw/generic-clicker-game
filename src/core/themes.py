from pygame.typing import ColorLike

THEMES: dict[str, dict[str, ColorLike]] = {
    "dark": {
        "background": "#121212",
        "container_bg": "#242424",
        "text": "#F5F5F5",
        "button_normal_bg": "#333333",
        "button_hovered_bg": "#454545",
        "button_pressed_bg": "#555555",
        "border_color": "#555555",
    },
    "light": {
        "background": "#F5F5F5",
        "container_bg": "#FFFFFF",
        "text": "#171717",
        "button_normal_bg": "#E5E5E5",
        "button_hovered_bg": "#D4D4D4",
        "button_pressed_bg": "#C4C4C4",
        "border_color": "#D0D0D0",
    },
}