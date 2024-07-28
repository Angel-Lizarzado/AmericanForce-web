import reflex as rx
from typing import Optional
from ejercitoaf.config import SupabaseDB


class cronometrer(rx.State):
    user_id: int = 0
    username: str = ""
    start_time: Optional[str] = ""


    def authenticate(self, token: str):
        self.auth_token = token
        self.check_auth()
        if self.is_authenticated:
            return rx.redirect("/login")
        return None

    
    def logout(self):
        self.auth_token = ""
        self.is_authenticated = False
        self.user_id = 0
        self.username = ""
        self.user_rank = ""
        
        return [rx.remove_cookie("auth_token"), rx.redirect("/")]
    

def addTime(username: str, start_time: str):
    print("recibido")
      # Crea una instancia de SupabaseDB
    if db.get_user_by_username(username):
        try:
            cronometrer.username = username
            cronometrer.start_time = start_time
            db.add_time(cronometrer.username, cronometrer.start_time)
        except:
            print("Error2")
    else:
        print("error1")
