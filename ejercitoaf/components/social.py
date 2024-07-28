import reflex as rx

def card(item: dict):
    return rx.box(
        rx.text(item["nombre"]),
        rx.text(item["descripcion"]),
        padding="4",
        border="1px solid",
        border_radius="md",
    )


def social() -> rx.Component:
    return rx.hstack(
        rx.spacer(),
        rx.box(
            rx.vstack(
                rx.heading("Dioses", text_align="center"),
                rx.grid(
                    # Aquí irán las tarjetas de los dioses
                    columns="3",
                    spacing="4",
                    width="100%",
                ),
                rx.heading("Pows", text_align="center"),
                rx.grid(
                    # Aquí irán las tarjetas de los pows
                    columns="3",
                    spacing="4",
                    width="100%",
                ),
            ),
         ),
         rx.spacer(),
        rx.box(
            rx.html(
                """
                <iframe src="https://discord.com/widget?id=1241159428602855424&theme=dark" width="350" height="500" allowtransparency="true" frameborder="0" sandbox="allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts"></iframe>
                """
            ),
            width="auto",
        ),
        spacing="4",
        justify="end",
        width="95%",
        margin_top="4em",
    )