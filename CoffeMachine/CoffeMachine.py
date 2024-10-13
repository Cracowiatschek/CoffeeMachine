"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from .components import navbar as nv
# from .components import coffe_picker as cp
from .components import footer as ft
from .views import idx
from rxconfig import config
from typing import List, Dict
from .views import coffee_desk as cd



class Coffees(rx.State):
    coffee: List[str]  = [
        ["Espresso","kawa","/20-28.png"],
        ["Cappuccino","kawa","/20-28.png"],
        ["Latte Macchiato","kawa","/20-28.png"],
        ["Espresso", "kawa", "/20-28.png"],
        ["Cappuccino", "kawa", "/20-28.png"],
        ["Latte Macchiato", "kawa", "/20-28.png"],
        ["Espresso", "kawa", "/20-28.png"],
        ["Cappuccino", "kawa", "/20-28.png"],
        ["Latte Macchiato", "kawa", "/20-28.png"],
    ]

class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.box(
            rx.aspect_ratio(
            rx.container(
                nv.navbar(),
                idx.idx(Coffees),
                ft.footer()
            ),
            ratio=5 / 7,
        ),
        width = "100%",
        height = "100vh",  # Ustaw wysokość na 100% widoku
        padding = "0",
        margin = "0",
        overflow = "hidden"
    )

def coffee_desk():
    return rx.box(
        rx.aspect_ratio(
            rx.container(
                nv.navbar(),
                cd.coffee_desk(),
                ft.footer()
            ),
            ratio = 5 / 7,
        ),
        width = "100%",
        height = "100vh",  # Ustaw wysokość na 100% widoku
        padding = "0",
        margin = "0",
        overflow = "hidden"
    )

app = rx.App()
app.add_page(index)
app.add_page(coffee_desk, route="/coffee")
