import reflex as rx
from ejercitoaf.config import SupabaseDB
import datetime
import bcrypt
import requests
import json

class RegistroState(rx.State):
    username: str = ""
    password: str = ""
    confirm_password: str = ""
    rank=0
    now = datetime.datetime.now()
    date= now.strftime("%Y-%m-%d %H:%M:%S")


    def set_username(self, username: str):
        self.username = username

    def set_password(self, password: str):
        self.password = password

    def set_confirm_password(self, confirm_password: str):
        self.confirm_password = confirm_password

    def get_public_ip(self):
        response = requests.get("https://ident.me/")
        ip = response.text
        return ip

    def registrar(self):
        db = SupabaseDB()
        ip = self.get_public_ip()
        password_hash = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt())
        password_hash_str = password_hash.decode('utf-8')
        
        try:
            

            # Verificar si el nombre de usuario ya existe
            existing_user = db.get_user_by_username(self.username)
            if existing_user:
                return rx.toast.error("El nombre de usuario ya está en uso")
            
            # Verificar si la dirección IP ya existe
            existing_ip = db.get_users_by_ip(ip)
            if existing_ip:
                return rx.toast.error("La dirección IP ya está registrada")
            
            # Crear el nuevo usuario
            new_user = db.create_user(self.username, password_hash_str, self.date, self.rank, ip)
            user_id = new_user['id']
            
            # Crear registro de horarios para el nuevo usuario
            new_day_time = db.create_days_time(user_id, "00:00:00", "00:00:00", "00:00:00", "00:00:00", "00:00:00", "00:00:00")
            
            return rx.toast.success("Usuario registrado exitosamente")
        except Exception as e:
            return rx.toast.error(f"Error al crear la cuenta")
        
    def registrar_family(self, username, password):
        username = username
        password = password
        db = SupabaseDB()
        ip = "127.0.0.1"
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        password_hash_str = password_hash.decode('utf-8')
        
        try:
            existing_user = db.get_user_by_username(username)
            if existing_user:
                return rx.toast.error("El nombre de usuario ya está en uso")
            
            # Crear el nuevo usuario
            new_user = db.create_user(username, password_hash_str, self.date, self.rank, ip)
            user_id = new_user['id']
            
            # Crear registro de horarios para el nuevo usuario
            new_day_time = db.create_days_time(user_id, "00:00:00", "00:00:00", "00:00:00", "00:00:00", "00:00:00", "00:00:00")
            
            return rx.toast.success("Usuario registrado exitosamente")
        except Exception as e:
            return rx.toast.error(f"Error al crear la cuenta")