import reflex as rx
from ejercitoaf.config import SupabaseDB




db = SupabaseDB()

class DashboardState(rx.State):

    timeLunes : str = ""
    timeMartes : str = ""
    timeMiercoles : str = ""
    timeJueves : str = ""
    timeViernes : str = ""
    timeSabado : str = ""
    
    def checkTime(self):
        print(UserState.user_id)
        times = db.get_Usertimes(UserState.user_id)
        print(times)