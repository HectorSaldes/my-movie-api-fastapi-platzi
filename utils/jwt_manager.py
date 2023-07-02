# IMPORTANCIÓN DEL SISTEMA
import os
# IMPORTANCIÓN DEL MODULO JWT
from jwt import encode, decode
# IMPORTACIÓN DE LA CLAVE SECRETA
from dotenv import load_dotenv

load_dotenv()


# REGRESAMOS EL TOKEN
def create_token(data: dict) -> str:
    token: str = encode(
        payload=data,
        key=os.getenv('SECRET_KEY'),  # CREAMOS UNA LLAVE PARA DESCIFRAR EL TOKEN DESPUÉS
        algorithm='HS256'  # ALGORITMO DE CIFRADO
    )
    return token


def validate_token(token: str) -> dict:
    data: dict = decode(
        token, # PASAR EL TOKEN
        os.getenv('SECRET_KEY'), # PASAR LA LLAVE
        algorithms=['HS256'] # PASAR EL ALGORITMO
    )
    return data