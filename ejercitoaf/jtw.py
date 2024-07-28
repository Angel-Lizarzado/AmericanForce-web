import jwt
from datetime import datetime, timedelta


# Configuración de la clave secreta
SECRET_KEY = '$2y$10$aHGf/mSUwoaLwxcP8pPRm.qjWx6LK.UBl1X7V20z8yOf4CYftr9j.'


def generate_token(user_id, username, registerDate, rank):
    # Generar el payload del token
    payload = {
        'user_id': user_id,
        'username': username,
        'registerDate': registerDate,
        'rank' : rank,
        'exp': datetime.utcnow() + timedelta(minutes=60)  # Token válido por 60 minutos
    }

    # Generar el token JWT
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

