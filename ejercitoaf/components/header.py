import reflex as rx


def header() -> rx.Component:
    return rx.box(
        
        bg=rx.color("red", 9),
        border_radius="1em",
        border="4px solid",
        border_color=rx.color("red", 5),
        padding=["1em", "1.5em", "2em"],
        width="95%",
        height="400px",
        margin="0 auto",
        box_shadow=f"0 4px 6px {rx.color('red', 11)}",
        margin_top="4em"
    )
