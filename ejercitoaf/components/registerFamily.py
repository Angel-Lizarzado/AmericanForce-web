import reflex as rx
from ejercitoaf.state.registerState import RegistroState

class FamilyState(rx.State):
    username: str = ""
    password: str = ""

    def submit(self, form_data: dict):
        self.username = form_data.get("username", "")
        self.password = form_data.get("password", "")
        return RegistroState.registrar_family(self.username, self.password)

def family_form():
    return rx.center(
        rx.form(
            rx.vstack(
                rx.hstack(
                    rx.icon('triangle-alert', color="orange"),
                    rx.heading("Registrar usuario por ip ocupada", size="5", font_size="1em"),
                ),
                rx.input(
                    placeholder="Habbo username",
                    name="username",
                ),
                rx.input(
                    placeholder="Password",
                    type_="password",
                    name="password",
                ),
                rx.button(
                    "Crear cuenta",
                    type_="submit",
                    color_scheme="blue",
                ),
                spacing="4",
                padding="2em",
                border="4px solid",
                border_color=rx.color("blue", 5),
                border_radius="1em",
                box_shadow=f"0 4px 6px {rx.color('blue', 11)}",
                width="300px",
            ),
            on_submit=FamilyState.submit,
        )
    )