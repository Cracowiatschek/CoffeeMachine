import reflex as rx


def coffee_desk():
    return rx.box(
        rx.card(
            rx.flex(
                rx.inset(
                    rx.image(
                        src="/20-28.png",
                        alt="kawa",
                        width="500px",
                        heigth="500px"
                    ),
                    side="left",
                    pr="current"
                ), rx.vstack(
                    rx.flex(
                    rx.text("Moc parzenia"),
                        rx.button("+"),
                        rx.text("test"),
                        rx.button("-"),
                        direction = "row",
                        width = "100%"
                    ), rx.flex(
                    rx.text("Moc parzenia"),
                        rx.button("+"),
                        rx.text("test"),
                        rx.button("-"),
                        direction = "row",
                        width = "100%"
                    ), rx.flex(
                    rx.text("Moc parzenia"),
                        rx.button("+"),
                        rx.text("test"),
                        rx.button("-"),
                        direction = "row",
                        width = "100%"
                    )
                ),
                direction = "row",
                width = "100%"
            ),
        ),
         width="100%"
    )
