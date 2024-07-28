import reflex as rx
from rxconfig import config
from ejercitoaf.pages.index import index
from ejercitoaf.pages.rangos import rangos
from ejercitoaf.pages.login import login
from ejercitoaf.pages.dashboard import dashboard
from ejercitoaf.pages.times import Times
from ejercitoaf.pages.nomina import nomina
from ejercitoaf.state.userState import UserState




class State(UserState):
    pass

app = rx.App(
    theme=rx.theme(
        appearance="dark",
        accent_color="red",
    )
)
# Public routes
app.add_page(index, route="/")
app.add_page(login, route="/login")
app.add_page(rangos, route="/rangos")

# Protected routes
app.add_page(dashboard, route="/dashboard", on_load=UserState.check_auth)
app.add_page(Times, route="/times", on_load=UserState.check_auth)
app.add_page(nomina, route="/nomina", on_load=UserState.check_auth)