from fastapi import status, HTTPException, Request
from fastapi.security import HTTPBearer
from utils.jwt_manager import validate_token


# HEREDAR DE HTTPBEARER PARA MANDAR A LLAMAR NUESTRA CLASE DE AUTENTICACIÓN
class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data['email'] != "admin@gmail.com":
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={"message": "No tienes permiso"})
