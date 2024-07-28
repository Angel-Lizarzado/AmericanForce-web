import reflex as rx
from ejercitoaf.components.navbar import navbar
from ejercitoaf.state.userState import UserState
from ..components.infoAccount import infoAccount
from ..components.hoursWorked import show_day
from ..components.registerFamily import family_form
from ejercitoaf.config import SupabaseDB
from typing import List, Dict, Any

class DashState(UserState):
    daysworked: List[Dict[str, Any]] = []
    timeData: List[Dict[str, Any]] = []


    def on_mount(self):
        db = SupabaseDB()
        self.check_auth()
        if self.is_authenticated:
            self.daysworked = db.get_Times(self.user_id)
            self.timeData = db.get_time_for_user(self.username)
            print(self.daysworked)
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