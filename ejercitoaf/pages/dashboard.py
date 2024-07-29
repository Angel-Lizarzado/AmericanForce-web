import reflex as rx
from ejercitoaf.components.navbar import navbar
from ejercitoaf.state.userState import UserState
from ..components.infoAccount import infoAccount
from ..components.hoursWorked import show_day
from ..components.asignrank import asignar_rank
from ..components.registerFamily import family_form
#from ejercitoaf.state.asign_rank import updateRank
from ejercitoaf.config import SupabaseDB
from typing import List, Dict, Any

class DashState(UserState):
    daysworked: List[Dict[str, Any]] = []
    timeData: List[Dict[str, Any]] = []
    getRanks: List[Dict[str, Any]] = []
    hb_user: str = ""
    selected_rank_id: str = ""
    selected_rank_value: str = "Seleccione un rango"

    def set_selected_rank(self, value: str):
        self.selected_rank_id = value
        for rank in self.getRanks:
            if rank["id"] == value:
                self.selected_rank_value = rank["rank"]
                break

    def updateUserRank(self):
        db = SupabaseDB()
        hb_user = self.hb_user
        rank_id: int = self.selected_rank_id
        try:
            existing_user = db.get_user_by_username(self.hb_user)
            if existing_user:
                response = db.update_rank(hb_user, rank_id)
                return rx.toast.success(f"El rango de {hb_user} ha sido actualizado correctamente.")
            else: 
                return rx.toast.error("Compruebe nombre de usuario, el ingresado no existe.")
        except Exception as e:
            return rx.toast.error("Error al ascender al usuario.")


        
    def on_mount(self):
        db = SupabaseDB()
        self.check_auth()
        if self.is_authenticated:
            self.daysworked = db.get_Times(self.user_id)
            self.timeData = db.get_time_for_user(self.username)
            self.getRanks = db.get_ranksList()
        else:
            return rx.redirect("/")
        



@rx.page(on_load=DashState.on_mount)
def dashboard() -> rx.Component:
    return rx.center(
        rx.box(
            navbar(),
            rx.box(
                rx.foreach(
                    DashState.timeData,
                    infoAccount
                ),
            margin_top="6em",
            width="90"
            ),
            rx.box(
                rx.cond(UserState.user_rank >= 156,
                        rx.center(
                            rx.hstack(
                                family_form(),
                                rx.card(
                                    rx.vstack(
                                        rx.heading("Formulario de selección"),
                                        rx.input(placeholder="Ingrese el usuario", on_change=DashState.set_hb_user),
                                         rx.select.root(
                                            rx.select.trigger(placeholder=DashState.selected_rank_value),
                                            rx.select.content(
                                                rx.foreach(
                                                    DashState.getRanks,
                                                    lambda rank: rx.select.item(
                                                        rank["rank"], value=f"{rank['id']}"  # Convertimos el id a string
                                                    )
                                                )
                                            ),
                                            value=DashState.selected_rank_id,
                                            on_change=DashState.set_selected_rank,
                                            color_scheme="orange",
                                            variant="soft",
                                            radius="full",
                                            width="30%",
                                        ),
                                        rx.button("Enviar", on_click=DashState.updateUserRank),
                                        spacing="4",
                                    ),
                                    spacing="4",
                                    padding="2em",
                                    border="2px solid red",
                                    border_radius="10px",
                                    box_shadow="lg",
                                ),
                            )
                        ),
                        rx.foreach(
                            DashState.daysworked,
                            show_day
                            ),
                            ),
            margin_top="6em",
            width="90"
            ),
        width="100%")
    )