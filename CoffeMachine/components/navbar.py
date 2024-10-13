import reflex as rx


def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"), href=url
    )

def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.hstack(
                rx.image(
                    src="/20-28.png",
                    width="2.25em",
                    height="auto",
                    border_radius="25%",
                    alt="logo"
                ),
                rx.heading(
                    "CoffeeMachine", size="7", weight="bold"
                ),
                align_items="center",
            ),
            rx.hstack(
                navbar_link("Temperature", "/#"),
                navbar_link("Milk", "/#"),
                navbar_link("Grind", "/#"),
                justify="end",
                spacing="5",
            ),
            justify="between",
            align_items="center",
        ),
        rx.box(height = "20px"),
    )