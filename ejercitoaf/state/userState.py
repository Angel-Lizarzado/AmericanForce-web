import reflex as rx
from ejercitoaf.jtw import SECRET_KEY
import jwt
from typing import Optional
from ejercitoaf.config import SupabaseDB


class UserState(rx.State):
    auth_token: str = rx.Cookie()
    is_authenticated: bool = False
    user_id: int = 0
    username: str = ""
    #registerDate: str = ""
    user_rank: Optional[int] = ""
    rank_name: Optional[str] = ""


    def authenticate(self, token: str):
        self.auth_token = token
        self.check_auth()
        if self.is_authenticated:
            return rx.redirect("/dashboard")  # Redirige al dashboard o la página principal
        else:
            return rx.redirect("/login")  # Redirige a la página de inicio de sesión

    def check_auth(self):
        if self.auth_token:
            try:
                db = SupabaseDB()
                payload = jwt.decode(self.auth_token, algorithms=["HS256"], key=SECRET_KEY)
                self.user_id = payload["user_id"]
                self.username = payload["username"]
                self.user_rank = db.get_Rank(self.user_id)
                self.rank_name = db.get_nameRank(self.user_rank)
                self.is_authenticated = True
            except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
                self.logout()
                return rx.redirect("/login")
        else:
            self.is_authenticated = False
            return rx.redirect("/login")

    def check_auth_and_redirect(self):
        self.check_auth()
        if not self.is_authenticated:
            return True
        return False
        
    def logout(self):
        self.auth_token = ""
        self.is_authenticated = False
        self.user_id = 0
        self.username = ""
        self.user_rank = ""
        
        return [rx.remove_cookie("auth_token"), rx.redirect("/")]
    

