import reflex as rx


def coffe_picker(item) -> rx.Component:
    return rx.card(
        rx.link(
            rx.center(
                rx.image(
                    src = item[2],
                    width = "150px",
                    height = "150px",
                    border_radius = "75px 75px",
                    border = "5px solid #555",
                    alt = item[1],
                    text_align = "center",
                ),
                rx.heading(item[0]),
                direction = 'column',
            ),
            color_scheme = "gray",
            high_contrast = True
        ),
    )


def idx(Coffees):
    return rx.grid(
        rx.foreach(
            Coffees.coffee,
            coffe_picker,
        ),
        columns="3",
        spacing="4",
        width="100%",
    )



