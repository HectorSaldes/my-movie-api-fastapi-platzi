from fastapi import APIRouter
from fastapi import status, HTTPException
from fastapi.responses import JSONResponse

from schemas.user import User

from utils.jwt_manager import create_token

# CREAR UN ROUTER
login_router = APIRouter()


@login_router.post('/login', tags=['auth'], status_code=status.HTTP_200_OK)
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(user.dict())
        return JSONResponse(status_code=status.HTTP_200_OK, content=token)
    else:
        return HTTPException(status_code=401, detail={"message": "Credenciales inválidas, intente de nuevo"})
