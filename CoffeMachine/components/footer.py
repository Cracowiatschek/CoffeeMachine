import reflex as rx


def footer():
    return rx.vstack(
        rx.box(height = "20px"),
        rx.hstack(
            rx.image(
                src="/20-28.png",
                width="2em",
                height="auto",
                border_radius="25%",
            ),
            rx.text(
                "© 2024 Piotr Baran",
                size="3",
                white_space="nowrap",
                weight="medium",
            ),
            spacing="2",
            align="center",
            justify_content=[
                "center",
                "center",
                "start",
            ],
            width="100%",
        )
    )
