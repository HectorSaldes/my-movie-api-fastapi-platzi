from fastapi import FastAPI, status
from fastapi.responses import HTMLResponse

from config.database import engine, Base

from middlewares.error_handler import ErrorHandler

# IMPORTAR ROUTERS DE OTROS MODULOS
from routers.movie import movie_router
from routers.login import login_router

# INSTANCIA DE FASTAPI
app = FastAPI()
app.title = "Mi aplicación con FastAPI"
app.version = "0.0.1"

# MIDDLEWARES
app.add_middleware(ErrorHandler)

# ROUTERS
app.include_router(movie_router)
app.include_router(login_router)


# CREACIÓN DE NUESTRAS BD Y TABLAS EN LA BASE DE DATOS
Base.metadata.create_all(bind=engine)



movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'
    },
    {
        'id': 2,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'
    }
]




@app.get('/', tags=['home'], status_code=status.HTTP_200_OK)
def message():
    return HTMLResponse('<h1>Hola mundo</h1>', status_code=status.HTTP_200_OK)


