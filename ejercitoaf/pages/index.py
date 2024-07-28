import reflex as rx
from ejercitoaf.components.navbar import navbar
from ejercitoaf.components.header import header
from ejercitoaf.components.payHour import payHour
from ejercitoaf.components.social import social
from ejercitoaf.config import SupabaseDB


class indexState(rx.State):
    dioses: list[dict] = []
    pows: list[dict] = []
    devs: list[dict] = []

    def load_data(self):
        db = SupabaseDB()
        self.dioses = db.get_Dioses()
        self.pows = db.get_Pows()
        self.devs = db.get_Devs()


def card(item: dict):
    return rx.card(
        rx.vstack(
            rx.image(
                src=f"https://www.habbo.es/habbo-imaging/avatarimage?direction=2&head_direction=2&size=l&user={item['username']}",
                border_radius="md",
                box_shadow="lg",
            ),
            rx.text(
                item["username"],
                font_weight="bold",
                color="var(--red-9)",
            ),
            rx.text(
                item["name_rank"],
                font_weight="bold",
                color="var(--white-9)",
            ),
            spacing="3",
            align_items="center",
        ),
        size="2",
        variant="surface",
        border="1px solid var(--red-6)",
        border_radius="xl",
        padding="4",
        bg="var(--red-1)",
        _hover={
            "transform": "scale(1.05)",
            "transition": "transform 0.2s",
            "box_shadow": "xl",
        },
    )

def card2(item: dict):
    return rx.card(
        rx.vstack(
            rx.image(
                src=f"https://www.habbo.es/habbo-imaging/avatarimage?direction=2&head_direction=2&size=l&user={item['username']}",
                border_radius="md",
                box_shadow="lg",
            ),
            rx.text(
                item["username"],
                font_weight="bold",
                color="var(--blue-9)",
            ),
            rx.text(
                item["name_rank"],
                font_weight="bold",
                color="var(--white-9)",
            ),
            spacing="3",
            align_items="center",
        ),
        size="2",
        variant="surface",
        border="1px solid var(--blue-6)",
        border_radius="xl",
        padding="4",
        bg="var(--blue-1)",
        _hover={
            "transform": "scale(1.05)",
            "transition": "transform 0.2s",
            "box_shadow": "xl",
        },
    )

def card3(item: dict):
    return rx.card(
        rx.vstack(
            rx.image(
                src=f"https://www.habbo.es/habbo-imaging/avatarimage?direction=2&head_direction=2&size=l&user={item['username']}",
                border_radius="md",
                box_shadow="lg",
            ),
            rx.text(
                item["username"],
                font_weight="bold",
                color="var(--yellow-9)",
            ),
            rx.text(
                "Desarrollador web",
                font_weight="bold",
                color="var(--yellow-9)",
            ),
            spacing="3",
            align_items="center",
        ),
        size="2",
        variant="surface",
        border="1px solid var(--yellow-6)",
        border_radius="xl",
        padding="4",
        bg="var(--yellow-1)",
        _hover={
            "transform": "scale(1.05)",
            "transition": "transform 0.2s",
            "box_shadow": "xl",
        },
    )
@rx.page(on_load=indexState.load_data)
def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.box(
            rx.vstack(
                header(),
                width="100%",
                spacing="1",
            ),
            padding_top="4em", 
            width="100%",
        ),
        rx.box(
            rx.vstack(
                payHour(),
                width="100%",
                spacing="1",
            ),
            width="100%",
        ),
        rx.box(
            rx.center(
                rx.vstack(
                    rx.hstack(
                        rx.spacer(),
                        rx.box(
                            rx.vstack(
                                rx.heading("Dioses", text_align="center"),
                                rx.grid(
                                    rx.foreach(
                                        indexState.dioses,
                                        card
                                    ),
                                    columns="3",
                                    spacing="4",
                                    width="100%",
                                ),
                                rx.heading("Pows", text_align="center"),
                                rx.grid(
                                    rx.foreach(
                                        indexState.pows,
                                        card2
                                    ),
                                    columns="3",
                                    spacing="4",
                                    width="100%",
                                ),
                                rx.heading("Web developer", text_align="center"),
                                rx.grid(
                                    rx.foreach(
                                        indexState.devs,
                                        card3
                                    ),
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
                    ),
                width="100%",
                spacing="1",
            ),
            ),
            width="100%",
        ),
        bg=rx.color("black", 3),
        width="100vw",
        min_height="100vh", 
    )