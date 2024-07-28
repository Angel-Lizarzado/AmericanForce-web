import reflex as rx
from typing import List, Dict, Any


def show_day(day: Dict[str, Any]) -> rx.Component:
    return rx.center(
            rx.tablet_and_desktop(
                    rx.hstack(

                    rx.table.root(
                        rx.table.header(
                            rx.table.row(
                                rx.table.column_header_cell("Lunes"),
                                rx.table.column_header_cell("Martes"),
                                rx.table.column_header_cell("Miercoles"),
                                rx.table.column_header_cell("Jueves"),
                                rx.table.column_header_cell("Viernes"),
                                rx.table.column_header_cell("Sabado"),
                            ),
                        ),
                        rx.table.body(
                            rx.table.row(
                                rx.table.cell(day['Lunes']),
                                rx.table.cell(day['Martes']),
                                rx.table.cell(day['Miercoles']),
                                rx.table.cell(day['Jueves']),
                                rx.table.cell(day['Viernes']),
                                rx.table.cell(day['Sabado']),
                            ),
                        ),
                        margin="auto",
                        variant="surface",
                        border="4px solid",
                        color_scheme="red",
                        border_color=rx.color("blue", 5),
                    ),



            border_radius="1em",
            border="4px solid",
            border_color=rx.color("red", 5),
            box_shadow=f"0 4px 6px {rx.color('red', 11)}",
            width="100%",
            height="auto",
            padding="2em"),
                width="100%"),
            rx.mobile_only(
                rx.vstack(

                    rx.table.root(
                        rx.table.header(
                            rx.table.row(
                                rx.table.column_header_cell("Lunes"),
                                rx.table.row_header_cell(day['Lunes']),
                            ),
                        width="100%"),
                        rx.table.header(
                            rx.table.row(
                                rx.table.column_header_cell("Martes"),
                                rx.table.row_header_cell(day['Martes']),
                            ),
                        ),
                        rx.table.header(
                            rx.table.row(
                                rx.table.column_header_cell("Miercoles"),
                                rx.table.row_header_cell(day['Miercoles']),
                            ),
                        ),
                        rx.table.header(
                            rx.table.row(
                                rx.table.column_header_cell("Jueves"),
                                rx.table.row_header_cell(day['Jueves']),
                            ),
                        ),
                        rx.table.header(
                            rx.table.row(
                                rx.table.column_header_cell("Viernes"),
                                rx.table.row_header_cell(day['Viernes']),
                            ),
                        ),
                        rx.table.header(
                            rx.table.row(
                                rx.table.column_header_cell("Sabado"),
                                rx.table.row_header_cell(day['Sabado']),
                            ),
                        ),

                        margin="auto",
                        variant="surface",
                        border="4px solid",
                        border_color=rx.color("blue", 5),
                        width="100%"
                    ),



            border_radius="1em",
            border="4px solid",
            border_color=rx.color("red", 5),
            box_shadow=f"0 4px 6px {rx.color('red', 11)}",
            width="95%",
            height="auto",
            margin="auto",
            padding="2em")
            ),
    width="95%",
    margin="auto")
