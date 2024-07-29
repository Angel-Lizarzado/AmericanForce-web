from supabase import create_client, Client
import datetime
from datetime import timezone,timedelta, datetime
from dateutil import parser
import pytz


    
class SupabaseDB:
    def __init__(self):
        self.url: str = "https://iodwzgwzkaguexxtiuvg.supabase.co"
        self.key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlvZHd6Z3d6a2FndWV4eHRpdXZnIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjA2NTg1MjgsImV4cCI6MjAzNjIzNDUyOH0.G7NCy0qdIMyK2IzKfxMnBbSbKJK-Rfh8w-TT1pwAukg"
        self.supabase: Client = create_client(self.url, self.key)
#### USERS
    def get_users(self):
        response = self.supabase.table("Users").select("*").execute()
        users = response.data
        for user in users:
            rank_id = user['rank']
            rank_name = self.get_nameRank(rank_id)
            user['rank_name'] = rank_name
            
            hours_response = self.supabase.table("DaysTime").select("Lunes, Martes, Miercoles, Jueves, Viernes, Sabado").eq("user_id", user['id']).execute()
            if hours_response.data:
                hours_data = hours_response.data[0]
                try:
                    total_seconds = sum(self.convert_to_seconds(hours_data.get(day, '00:00:00')) for day in ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado'])
                    hours, remainder = divmod(total_seconds, 3600)
                    minutes, seconds = divmod(remainder, 60)
                    user['total_hours'] = f"{hours:02d}:{minutes:02d}"
                except Exception as e:
                    print(f"Error calculating total hours for user {user['id']}: {e}")
                    user['total_hours'] = "00:00"
            else:
                user['total_hours'] = "00:00"
        
        return users

    def convert_to_seconds(self, time_str):
        try:
            # Split the time string and take only the first three parts
            parts = time_str.split(':')[:3]
            if len(parts) == 3:
                hours, minutes, seconds = map(int, parts)
                return hours * 3600 + minutes * 60 + seconds
            else:
                print(f"Invalid time format: {time_str}")
                return 0
        except ValueError:
            print(f"Error converting time: {time_str}")
            return 0

    def get_Usertimes(self, user_id):
            response = self.supabase.table("DaysTime").eq("user_id", user_id).execute()
            return response.data[0]
    
    def get_user_by_id(self, user_id: int):
        response = self.supabase.table("Users").select("*").eq("id", user_id).execute()
        return response.data[0] if response.data else None
    
    def get_user_by_username(self, username: str):
        response = self.supabase.table("Users").select("*").eq("username", username).execute()
        return response.data[0] if response.data else None
    
    def get_users_by_ip(self, ip:str):
        response = self.supabase.table("Users").select("Public_ip").eq("Public_ip", ip).execute()
        return response.data[0] if response.data else None

    def get_Dioses(self):
        response = self.supabase.table("Users").select("id", "username", "rank").eq("Dios", 1).execute()
        data = response.data if response.data else []
        result = []
        for item in data:
            rank_id = item['rank']
            rank_name = self.get_rank_name(rank_id)
            item['name_rank'] = rank_name
            result.append(item)
        return result

    def get_Pows(self):
        response = self.supabase.table("Users").select("id","username", "rank").eq("pow", 1).execute()
        data = response.data if response.data else []
        result = []
        for item in data:
            rank_id = item['rank']
            rank_name = self.get_rank_name(rank_id)
            item['name_rank'] = rank_name
            result.append(item)
        return result
    
    def get_Devs(self):
        response = self.supabase.table("Users").select("id","username", "rank").eq("dev", 1).execute()
        data = response.data if response.data else []
        result = []
        for item in data:
            rank_id = item['rank']
            rank_name = self.get_rank_name(rank_id)
            item['name_rank'] = rank_name
            result.append(item)
        return result
    
    def get_rank_name(self, id):
        response = self.supabase.table("Rank").select("rank").eq("id", id).execute()
        return response.data[0]['rank'] if response.data else None
    
    def create_user(self, username: str, password: str, date : str, rank : int, ip : str):
        response = self.supabase.table("Users").insert({
            "username": username, 
            "password": password, 
            "registerDate" : date, 
            "rank" : rank,
            "Public_ip" : ip,
            }).execute()
        return response.data[0]

    def update_user(self, user_id: int, name: str, email: str):
        response = self.supabase.table("Users").update({"name": name, "email": email}).eq("id", user_id).execute()
        return response.data[0]

    def delete_user(self, user_id: int):
        response = self.supabase.table("Users").delete().eq("id", user_id).execute()
        return response.data[0]
    
#### USERS - TIMES SEMANALES
    

### Users Ranks
    def get_Rank(self, userID: int):
            try:
                data = self.supabase.table("Users").select("rank").eq("id", userID).execute()
                if data.data:
                    return data.data[0]["rank"]
                else:
                    return "Rank not found"
            except Exception as e:
                print(f"Error: {e}")
                return None
    def get_nameRank(self, rank_id: int):
        try:
            data = self.supabase.table("Rank").select("rank").eq("id", rank_id).execute()
            if data.data:
                return data.data[0]["rank"]
            else:
                return "Rank not found"
        except Exception as e:
            print(f"Error: {e}")
            return None
        
    ### Users Times
    def get_Times(self, userID: int):
        try:
            data = self.supabase.table("DaysTime").select("*").eq("user_id", userID).execute()
            if data.data:
                return data.data  # Esto ya es una lista de diccionarios
            else:
                return None
        except Exception as e:
            print(f"Error: {e}")
            return None
        
    def get_ranksList(self):
        try:
            data = self.supabase.table("Rank").select("*").execute()
            if data.data:
                return data.data  # Esto ya es una lista de diccionarios
            else:
                return None
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def update_rank(self, hb_user, rank_id: int):
        response = self.supabase.table("Users").update({
            "rank": int(rank_id),
        }).eq("username", hb_user).execute()

            


### TIME QUERY

    def add_time(self, username:str, time:str, timer_username):
        if self.get_user_by_username(username):
            response = self.supabase.table("Times").insert({
                "user_hb": username, 
                "status": "Iniciado", 
                "start_time" : time, 
                "timerBy" : timer_username}).execute()
            return response.data[0]
        else:
            return None

    def create_days_time(self, username:str, Lunes:str,Martes:str, Miercoles:str,Jueves:str,Viernes:str,Sabado:str):
        response = self.supabase.table("DaysTime").insert({
            "user_id": username, 
            "Lunes": Lunes,
            "Martes": Martes,
            "Miercoles": Miercoles,
            "Jueves": Jueves,
            "Viernes": Viernes,
            "Sabado": Sabado}).execute()
        return response.data[0]

    def get_times(self):
        response = self.supabase.table("Times").select("*").execute()
        return response.data
    
    def get_time_for_user(self, user_hb):
        response = self.supabase.table("Times").select("*").eq("user_hb", user_hb).execute()
        return response.data if response.data else [{'status': 'Sin time', 'total_time': 'Time cerrado'}]

    def pause_time(self, username: str, elapsed_time: timedelta):
        response = self.supabase.table("Times").select("total_time").eq("user_hb", username).execute()
        if not response.data:
            print(f"No se encontró registro para el usuario {username}")
            return None

        # Convertir elapsed_time a formato HH:MM:SS
        total_seconds = int(elapsed_time.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        total_time_str = f"{hours:02}:{minutes:02}:{seconds:02}"

        # Actualizar la base de datos con el nuevo tiempo total
        response = self.supabase.table("Times").update({
            "status": "Pausado",
            "start_time": "0",
            "total_time": total_time_str
        }).eq("user_hb", username).execute()

        return response.data




    def play_time(self, hb_user, hora_inicio):
        # Obtenemos el tiempo total actual
        response = self.supabase.table("Times").select("total_time").eq("user_hb", hb_user).execute()
        if response.data:
            current_total_time = response.data[0]['total_time']
        else:
            current_total_time = "00:00:00"

        # Convertimos current_total_time a timedelta
        h, m, s = map(int, current_total_time.split(':'))
        total_time_delta = timedelta(hours=h, minutes=m, seconds=s)

        # Convertimos hora_inicio a datetime using dateutil.parser
        start_time = parser.parse(hora_inicio)

        # Restamos el total_time_delta de start_time
        adjusted_start_time = start_time - total_time_delta

        # Actualizamos la base de datos con el nuevo estado y la hora de inicio ajustada
        response = self.supabase.table("Times").update({
            "status": "Iniciado",
            "start_time": adjusted_start_time.isoformat(),
            "total_time": current_total_time  # Mantenemos el tiempo total acumulado
        }).eq("user_hb", hb_user).execute()

        print(response.data)
        return response.data
    
    def close_time(self, hb_user, day):
        try:
            user_data = self.get_user_by_username(hb_user)
            id_user = user_data['id']

            # Obtenemos el tiempo total actual
            response = self.supabase.table("Times").select("total_time").eq("user_hb", hb_user).execute()
            if response.data:
                current_total_time = response.data[0]['total_time']
            else:
                current_total_time = "00:00:00"

            # Construir la consulta de actualización
            update_query = self.supabase.table("DaysTime").update({
                day: current_total_time
            }).eq("user_id", id_user)
            
            # Imprimir la consulta antes de ejecutarla
            print(f"Consulta de actualización: {update_query}")

            # Ejecutar la consulta de actualización
            update_response = update_query.execute()
            print(f"Respuesta de actualización: {update_response}")

            # Si no se actualizó ningún registro, insertar uno nuevo
            if not update_response.data:
                insert_query = self.supabase.table("DaysTime").insert({
                    "user_id": id_user,
                    day: current_total_time
                })
                
                # Imprimir la consulta antes de ejecutarla
                print(f"Consulta de inserción: {insert_query}")

                # Ejecutar la consulta de inserción
                insert_response = insert_query.execute()
                print(f"Respuesta de inserción: {insert_response}")

            
        except Exception as e:
            print(f"Error al actualizar la base de datos: {e}")
            print(f"Detalles del error: {e.args}")
