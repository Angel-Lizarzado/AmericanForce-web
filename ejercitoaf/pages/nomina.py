import reflex as rx
from ejercitoaf.components.navbar import navbar
from typing import Dict, Any
from ejercitoaf.state.userState import UserState
from ejercitoaf.config import SupabaseDB

class nominaState(UserState):
    nomina: list[dict[str, Any]] = []

    @rx.background
    async def on_mount(self):
        db = SupabaseDB()
        users = db.get_users()
        async with self:
            self.nomina = users


def tableNomina(nomi: dict[str, Any]):
    return rx.table.row(
        rx.table.row_header_cell(nomi['id']),
        rx.table.cell(nomi['username']),
        rx.table.cell(nomi['registerDate']),
        rx.table.cell(nomi['rank_name']),  # Usamos rank_name en lugar de rank
        rx.table.cell(f"{nomi['total_hours']:.2f}"),
        rx.table.cell(nomi['publis']),
        rx.table.cell(nomi['times']),
        rx.table.cell(
            rx.dialog.root(
                rx.dialog.trigger(rx.button(rx.icon("square-pen"), "Editar", color_scheme="yellow")),
                rx.dialog.content(
                    rx.dialog.title("Edit User"),
                    rx.dialog.description(
                        "Edit user details below."
                    ),
                    rx.input(placeholder="Username", value=str(nomi['username'])),
                    rx.input(placeholder="Register Date", value=str(nomi['registerDate'])),
                    rx.input(placeholder="Rank", value=str(nomi['rank_name'])),  # Usamos rank_name aquí también
                    rx.dialog.close(rx.button("Save")),
                    rx.dialog.close(rx.button("Cancel")),
                ),
            )
        ),
        rx.table.cell(rx.button(rx.icon("square-arrow-up"), "Ascender", color_scheme="red")),
        rx.table.cell(rx.button(rx.icon("square-user"), "Sumar Publicidad", color_scheme="cyan")),
    )

@rx.page(on_load=nominaState.on_mount)
def nomina():
    return rx.vstack(
        navbar(),
        rx.cond(
            UserState.is_authenticated,
            rx.center(
                rx.vstack(
                    rx.table.root(
                        rx.table.header(
                            rx.table.row(
                                rx.table.column_header_cell("#id"),
                                rx.table.column_header_cell("Habbo User"),
                                rx.table.column_header_cell("Register Date"),
                                rx.table.column_header_cell("Rank"),
                                rx.table.column_header_cell("Total Hours"),
                                rx.table.column_header_cell("Publicidades"),
                                rx.table.column_header_cell("Time's"),
                                rx.table.column_header_cell("Modificar"),
                                rx.table.column_header_cell("Ascender"),
                                rx.table.column_header_cell("Publicidad"),
                                
                            ),
                        ),
                        rx.table.body(
                            rx.foreach(
                                nominaState.nomina,
                                tableNomina
                            ),
                        ),
                    width= "90%",
                    margin= "auto",
                    margin_top="auto"),
                    width="100%",
                    height="100vh",
                    overflow="auto",
                ),
                
            height="100vh",
            width="100vw"
        ),
        rx.vstack(
                 rx.text("Redirigiendo a la página principal..."),
                 rx.script("window.location.href = '/'"),
                ),
        ),
    )