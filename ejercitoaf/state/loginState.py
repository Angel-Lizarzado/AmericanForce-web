import reflex as rx
from ejercitoaf.config import SupabaseDB
from ejercitoaf.jtw import generate_token, SECRET_KEY
from .userState import UserState
import bcrypt


db = SupabaseDB()

class LoginState(rx.State):
    username: str = ""
    password: str = ""

    def set_username(self, username: str):
        self.username = username

    def set_password(self, password: str):
        self.password = password


    def login(self):
        login_user = db.get_user_by_username(self.username)
        if login_user:
            password_hash = login_user['password']
            if bcrypt.checkpw(self.password.encode('utf-8'), password_hash.encode('utf-8')):
                token = generate_token(login_user['id'], login_user['username'], login_user['registerDate'], login_user['rank'])
                return UserState.authenticate(token)
            else:
                return rx.window_alert("Credenciales incorrectas")
        else:
            return rx.window_alert("Credenciales incorrectas")
        


    def logout(self):
        self.auth_token = ""
        UserState.is_authenticated = False
        return [
        rx.remove_cookie("auth_token"),
        rx.redirect("/")
    ]

