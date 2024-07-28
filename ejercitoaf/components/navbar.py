import reflex as rx
from ejercitoaf.state.registerState import RegistroState
from ejercitoaf.state.loginState import LoginState
from ejercitoaf.state.userState import UserState

class NavState(rx.State):
    show_register: bool = False
    show_login: bool = False

    def toggle_register(self):
        self.show_register = not self.show_register

    def toggle_login(self):
        self.show_login = not self.show_login


def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(
            text,
            size="4",
            weight="medium",
            color=ROJO_CLARO,
            _hover={"color": TEXTO_CLARO},
        ),
        href=url,
    )


def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="https://www.habbo.es/habbo-imaging/badge/b09134s42064s11107s44114s38171e752b23c59d5b71746f9e27b9d0c43a6.png",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "American Force", size="7", weight="bold", color=TEXTO_CLARO
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_link("Home", "/#"),
                    navbar_link("Rangos", "/rangos"),
                    navbar_link("Precios", "/precios"),
                    rx.cond(
                        UserState.user_rank >=69,
                        navbar_link("Times", "/times"),
                    ),
                    rx.cond(
                        UserState.user_rank >=80,
                        navbar_link("Nomina", "/nomina"),
                    ),
                    
                    rx.spacer(),
                    rx.cond(
                        UserState.is_authenticated,
                        rx.link(
                            rx.hstack(
                                rx.heading(f"{UserState.username}"),
                                rx.image(src=f"https://www.habbo.es/habbo-imaging/avatarimage?direction=2&headonly=1&head_direction=4&size=l&user={UserState.username}", width="35px"),
                                rx.button(
                                    "Cerrar session",
                                    on_click=UserState.logout,
                                    size="3",
                                    bg=ROJO_OSCURO,
                                    color=TEXTO_CLARO,
                                    _hover={"bg": ROJO_CLARO, "color": NEGRO_OSCURO},
                                    _focus={"outline": "none", "box_shadow": f"0 0 0 2px {ROJO_CLARO}"},
                                ),
                                spacing="4",
                                justify="end",
                            ),
                            href="/dashboard",
                            underline="none",
                            color="inherit",
                        ),
                        rx.hstack(
                            rx.button(
                                "Registrarse",
                                on_click=NavState.toggle_register,
                                size="3",
                                variant="outline",
                                color_scheme="red",
                                color=ROJO_CLARO,
                                border_color=ROJO_OSCURO,
                                _hover={"bg": ROJO_OSCURO, "color": TEXTO_CLARO},
                                _focus={"outline": "none", "box_shadow": f"0 0 0 2px {ROJO_OSCURO}"},
                            ),
                            rx.chakra.modal(
                                rx.chakra.modal_overlay(
                                    rx.chakra.modal_content(
                                        rx.chakra.modal_header("Registrarse"),
                                        rx.chakra.modal_body(
                                            rx.chakra.input(
                                                placeholder="Username Habbo",
                                                on_change=RegistroState.set_username,
                                            ),
                                            rx.chakra.input(
                                                placeholder="Password",
                                                type_="password",
                                                on_change=RegistroState.set_password,
                                            ),
                                            rx.chakra.input(
                                                placeholder="Confirmar Password",
                                                type_="password",
                                                on_change=RegistroState.set_confirm_password,
                                            ),
                                        ),
                                        rx.chakra.modal_footer(
                                            rx.chakra.button(
                                                "Registrarse",
                                                on_click=RegistroState.registrar,
                                            ),
                                            rx.chakra.button(
                                                "Cerrar",
                                                on_click=NavState.toggle_register,
                                            ),
                                        ),
                                    )
                                ),
                                is_open=NavState.show_register,
                            ),
                            rx.button(
                                "Iniciar sesión",
                                on_click=NavState.toggle_login,
                                size="3",
                                bg=ROJO_OSCURO,
                                color=TEXTO_CLARO,
                                _hover={"bg": ROJO_CLARO, "color": NEGRO_OSCURO},
                                _focus={"outline": "none", "box_shadow": f"0 0 0 2px {ROJO_CLARO}"},
                            ),
                    rx.chakra.modal(
                        rx.chakra.modal_overlay(
                            rx.chakra.modal_content(
                                rx.chakra.modal_header("Iniciar Sesión"),
                                rx.chakra.modal_body(
                                    rx.chakra.input(
                                        placeholder="Username Habbo",
                                        on_change=LoginState.set_username,
                                    ),
                                    rx.chakra.input(
                                        placeholder="Password",
                                        type_="password",
                                        on_change=LoginState.set_password,
                                    ),
                                ),
                                rx.chakra.modal_footer(
                                    rx.chakra.button(
                                        "Iniciar Sesión",
                                        on_click=LoginState.login
                                    ),
                                    rx.chakra.button(
                                        "Cerrar",
                                        on_click=NavState.toggle_login,
                                    ),
                                ),
                            )
                        ),
                        is_open=NavState.show_login,
                    ),
                    spacing="4",
                    justify="end",
                ),
                    ),
                    spacing="5",
                ),
                
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="https://www.habbo.es/habbo-imaging/badge/b09134s42064s11107s44114s38171e752b23c59d5b71746f9e27b9d0c43a6.png",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "American Force", size="6", weight="bold", color=TEXTO_CLARO
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30, color=ROJO_CLARO)
                    ),
                    rx.menu.content(
                        rx.menu.item("Home", color=TEXTO_CLARO),
                        rx.menu.item("Rangos", color=TEXTO_CLARO),
                        rx.menu.item("Precios", color=TEXTO_CLARO),
                        rx.menu.item("Contacto", color=TEXTO_CLARO),
                        rx.menu.separator(),
                        rx.menu.item("Registrarse",on_click=NavState.toggle_register, color=TEXTO_CLARO),
                        rx.menu.item("Iniciar sessión", on_click=NavState.toggle_login, color=TEXTO_CLARO),
                        bg=NEGRO_OSCURO,
                        border=f"1px solid {ROJO_OSCURO}",
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),





        bg=NEGRO_OSCURO,
        color=TEXTO_CLARO,
        padding="1em",
        position="fixed",
        z_index="5",
        width="100%",
        box_shadow=f"0 2px 4px {ROJO_OSCURO}",
        border_bottom=f"1px solid {ROJO_OSCURO}",
        top="0px"
    )



ROJO_CLARO = rx.color("red", 3)
ROJO_OSCURO = rx.color("red", 9)
NEGRO_OSCURO = rx.color("gray", 12)
TEXTO_CLARO = rx.color("gray", 1)

