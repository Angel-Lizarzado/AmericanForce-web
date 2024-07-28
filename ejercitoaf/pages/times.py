import reflex as rx
from ejercitoaf.components.navbar import navbar
from ejercitoaf.state.userState import UserState
from ejercitoaf.config import SupabaseDB
from datetime import datetime, timezone
from typing import List, Dict, Any
from dateutil import parser


class ChronometersState(rx.State):
    authenticated: bool
    username: str = ""
    hora_inicio: str = ""
    timeData: List[Dict[str, Any]] = []
    start_times: dict[str, Any] = {}
    day: str = ""

    

    def add_chronometer(self, timer_username):
        db = SupabaseDB()
        self.hora_inicio = datetime.now(timezone.utc).isoformat()
        if db.add_time(self.username, self.hora_inicio, timer_username):
            self.on_mount()
            return rx.toast.success(f"Time de {self.username} añadido exitosamente")
        else:
            return rx.toast.error(f"El usuario {self.username} no existe en la nomina")

    def play_timer(self, hb_user):
        db = SupabaseDB()
        self.hora_inicio = datetime.now(timezone.utc).isoformat()
        db.play_time(hb_user, self.hora_inicio)
        self.on_mount()
        return rx.toast.success(f"Time de {hb_user} reanudado exitosamente")

    def pause_timer(self, username: str, start_time: str):
        db = SupabaseDB()
        elapsed_time = self.get_elapsed_time(start_time)
        db.pause_time(username, elapsed_time)
        self.on_mount()
        return rx.toast.success(f"Se ha pausado el time de {username}")


    def get_elapsed_time(self, start_time: str):
        start_datetime = parser.parse(start_time).astimezone(timezone.utc)
        current_datetime = datetime.now(timezone.utc)
        elapsed_time = current_datetime - start_datetime
        return elapsed_time
    
    def close_timer(self, hb_user):
        db = SupabaseDB()
        db.close_time(hb_user, self.day)
    
        self.on_mount()
        return rx.toast.success(f"Time de {hb_user} se ha cerrado exitosamente")
    

    def get_day(self):
        fecha_actual = datetime.now()
    
        # Array con los días de la semana
        dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
        
        # Obtener el día de la semana (0 es lunes, 6 es domingo)
        dia_semana = dias[fecha_actual.weekday()]
        return dia_semana



    def on_mount(self):
        
        if UserState.authenticate:
            db = SupabaseDB()
            self.timer_username = UserState.username
            self.timeData = db.get_times()
            self.day = self.get_day()
        else: 
            return rx.redirect("/")

def display_time(time: dict):
    return rx.container(
       rx.hstack(
            rx.box(
                rx.hstack(
                    rx.image(src=f"https://www.habbo.es/habbo-imaging/avatarimage?direction=2&headonly=1&head_direction=4&size=l&user={time['user_hb']}", width="60px"),
                    rx.badge(f"{time['user_hb']}", color_scheme="blue", variant="surface"),
                    rx.text("Status:"),
                    rx.cond(
                        time['status'] == "Iniciado",
                        rx.badge("Iniciado", color_scheme="green"),
                        rx.badge("Pausado", color_scheme="red")
                    ),
                    spacing="2",
                ),
                overflow="hidden",
            ),
            rx.box(
                rx.cond(
                    time['status'] == "Iniciado",
                    rx.moment(
                        time['start_time'],
                        format="HH:mm:ss",
                        duration_from_now=True,
                        interval=1000,
                        tz="UTC"
                    ),
                    rx.text(f"Tiempo acumulado : {time['total_time']}"),
                ),
            ),
            rx.box(
                    rx.box(
                        rx.text(f"Time llevado por:"),
                        rx.badge(f"{time['timerBy']}", color_scheme="yellow", variant="surface"),   
                        overflow="hidden",
                        text_overflow="ellipsis",
                        white_space="nowrap",
                    ),
            ),
            rx.box(
                rx.hstack(
                    rx.cond(
                        time['status'] == "Iniciado",
                        rx.button(rx.icon("pause"), color_scheme="blue", on_click=lambda: ChronometersState.pause_timer(time['user_hb'], time['start_time'])),
                        rx.hstack(rx.button(rx.icon("play"), color_scheme="gray", on_click=lambda: ChronometersState.play_timer(time['user_hb'])),
                                rx.button(rx.icon("x"), color_scheme="red", on_click=lambda: ChronometersState.close_timer(time['user_hb'])),
                                spacing="2"),
                    ),
                    spacing="2",   
                ),
            ),
            width="100%",
            align_items="center",
            justify="between",
            spacing="4",
        ),
        max_width="1200px",
    )

@rx.page(on_load=[ChronometersState.on_mount])
def Times():
    return rx.flex(
        navbar(),
        rx.cond(
            UserState.is_authenticated,
                rx.cond(
                    UserState.user_rank >= 69,
                    rx.flex(
                        rx.vstack(
                            rx.heading(f"Tiempos del dia: {ChronometersState.day}", color="white"),
                            rx.hstack(
                                rx.input(
                                    placeholder="Ingresa HabboUser",
                                    value=ChronometersState.username,
                                    on_change=ChronometersState.set_username
                                ),
                                rx.el.input(
                                    type="hidden",
                                    name="username",
                                    value=UserState.username,
                                ),
                                rx.button(
                                    rx.icon("play"), 
                                    "Iniciar time",
                                    color_scheme="red", 
                                    on_click=lambda: ChronometersState.add_chronometer(UserState.username)
                                ),
                            ),

                            rx.hstack(
                                rx.card(
                                    rx.vstack(
                                        rx.foreach(
                                    ChronometersState.timeData,
                                    display_time,
                                )
                                    ),
                                ),
                            ),
                            border_radius="15px",
                            border_width="thick",
                            spacing="4",
                            align_items="center",
                            justify_content="center",
                            width="auto",
                        ),
                        flex="1",
                        justify="center",
                        align="center",
                    ),
                    rx.vstack(
                 rx.text("No cumples con el rango adecuado, retornando al dashboard..."),
                 rx.script("window.location.href = '/dashboard'"),
             ),
                ),
                rx.vstack(
                 rx.text("Redirigiendo a la página principal..."),
                 rx.script("window.location.href = '/'"),
             ),
                
                ),
        width="100vw",
        height="100vh",
        direction="column",
    )