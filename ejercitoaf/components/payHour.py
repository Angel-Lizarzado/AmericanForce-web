import reflex as rx

def country_info(country_code: str, country: str, time: str) -> rx.Component:
    return rx.vstack(
        rx.image(src=f"https://flagcdn.com/w40/{country_code}.png", width="40px", height="30px"),
        rx.text(country, font_weight="bold"),
        rx.text(time),
        align_items="center",
        spacing="2",
    )

def payHour() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading("Países y Horas de Pago", size="5", margin_bottom="4", margin="auto"),
            rx.hstack(
                country_info("es", "España", "12:00"),
                country_info("ar", "Argentina", "09:00"),
                country_info("co", "Colombia", "07:00"),
                country_info("ve", "Venezuela", "07:30"),
                country_info("mx", "México", "06:00"),
                country_info("gt", "Guatemala", "06:00"),
                width="100%",
                justify="center",
                wrap="wrap",
            ),
            spacing="4",
            width="100%",
        ),
        bg=rx.color("red", 9),
        border_radius="1em",
        border="4px solid",
        border_color=rx.color("red", 5),
        padding=["1em", "1.5em", "2em"],
        width="95%",
        margin="0 auto",
        box_shadow=f"0 4px 6px {rx.color('red', 11)}",
        margin_top="4em"
    )