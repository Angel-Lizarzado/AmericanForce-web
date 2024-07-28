import reflex as rx
from ejercitoaf.state.userState import UserState



@rx.page(on_load=UserState.check_auth)
def login() -> rx.Component:
    return rx.center(
        rx.cond(
            UserState.is_authenticated,
            rx.cond(
                UserState.user_rank != 0,
                rx.vstack(
                     rx.text("Redirigiendo al dashboard..."),
                     rx.script("window.location.href = '/dashboard'"),
                 ),
                rx.vstack(
                     rx.heading("Por favor espera a que un supervisor confirme su registro"),
                     width="100%",
                     height="100vh",
                     align="center",
                     justify="center",
                 ),
                  
            ),
            rx.vstack(
                 rx.text("Redirigiendo a la página principal..."),
                 rx.script("window.location.href = '/'"),
             )
        )
    )



# rx.cond(
#             UserState.is_authenticated,
#             rx.cond(
#                 UserState.user_rank is None,
#                 rx.vstack(
#                     rx.heading("Por favor espera a que un supervisor confirme su registro"),
#                     width="100%",
#                     height="100vh",
#                     align="center",
#                     justify="center",
#                 ),
#                 rx.vstack(
#                     rx.text("Redirigiendo al dashboard..."),
#                     rx.script("window.location.href = '/dashboard'"),
#                 )
#             ),
#             rx.vstack(
#                 rx.text("Redirigiendo a la página principal..."),
#                 rx.script("window.location.href = '/'"),
#             )
#         )