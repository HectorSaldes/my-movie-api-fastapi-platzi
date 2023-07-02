# FASTAPI YA TIENE UN MODULO PARA CREAR RUTAS
from fastapi import APIRouter

from fastapi import Path, Query, status, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from typing import List

from starlette.responses import JSONResponse

from config.database import Session
from models.movie import Movie as MovieModel

from schemas.movie import Movie

from services.movie import MovieService

# CREAMOS UNA INSTANCIA Y ESTE NOMBRE DE VARIABLE, SERÁ REMPLAZADO POR EL NOMBRE DE LA RUTA app -> movie_router
movie_router = APIRouter()


@movie_router.get('/movies', tags=['movies'], response_model=List[Movie], status_code=200,
                  # dependencies=[Depends(JWTBearer())]
                  )
def get_movies() -> JSONResponse:
    db = Session()
    all_movies = MovieService(db).get_movies()
    result = jsonable_encoder(all_movies)
    return JSONResponse(status_code=200, content=result)


# COLOCAR PATHS EN LA RUTA CON {VAR}
@movie_router.get('/movies/{id}', tags=['movies'], response_model=Movie, status_code=status.HTTP_200_OK)
# Y PARA OBETENERLAS ES CON EL MISMO NOMBRE DE LA PATH COMO PARAMETRO DE LA FUNCION
def get_movie(id: int = Path(ge=1, le=200)) -> JSONResponse:
    try:

        # movie = list(filter(lambda m: m['id'] == id, movies))
        db = Session()
        one_movie = MovieService(db).get_movie(id)

        if one_movie:
            result = jsonable_encoder(one_movie)
            return JSONResponse(status_code=status.HTTP_200_OK, content=result)
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Movie not found')
    except HTTPException as e:
        return JSONResponse(status_code=e.status_code, content={'error': e.detail})


# CUANDO FASTAPI RECIBE UNA PETICION CON UN PARAMETRO QUE NO ESTA EN LA RUTA
# LO TOMA COMO QUERY PARAMS
@movie_router.get('/movies/', tags=['movies'], response_model=List[Movie], status_code=status.HTTP_200_OK)
def get_movies_by_category(category: str = Query(min_length=5, max_length=15)) -> JSONResponse:
    try:
        # category = list(filter(lambda m: m['category'] == category, movies))

        db = Session()

        one_category = MovieService(db).get_movies_by_category(category)
        result = jsonable_encoder(one_category)
        if category:
            return JSONResponse(status_code=status.HTTP_200_OK, content=result)
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Category not found')
    except HTTPException as e:
        return JSONResponse(status_code=e.status_code, content={'error': e.detail})


# SE UTILIZA BODY PARA QUE FASTAPI SEPA QUE LOS PARAMETROS VIENEN EN EL CUERPO DE LA PETICION
@movie_router.post('/movies', tags=['movies'], response_model=dict, status_code=201)
def create_movie(movie: Movie) -> JSONResponse:
    db = Session()
    MovieService(db).create_movie(movie)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"message": "Pelicula creada"})


@movie_router.put('/movies/{id}', tags=['movies'], response_model=dict, status_code=status.HTTP_200_OK)
def update_movie(id: int, movie: Movie) -> JSONResponse:
    # for item in movies:
    #     if item['id'] == id:
    #         item['title'] = movie.title
    #         item['overview'] = movie.overview
    #         item['year'] = movie.year
    #         item['rating'] = movie.rating
    #         item['category'] = movie.category
    #         item['category'] = movie.category
    #         return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Pelicula actualizada"})

    db = Session()
    one_movie = MovieService(db).get_movie(id)

    if one_movie:
        MovieService(db).update_movie(id, movie)
        return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Pelicula actualizada"})
    else:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Pelicula no encontrada"})


@movie_router.delete('/movies/{id}', tags=['movies'], response_model=dict, status_code=status.HTTP_200_OK)
def delete_movie(id: int) -> JSONResponse:
    # for item in movies:
    #     if item['id'] == id:
    #         movies.remove(item)
    #         return JSONResponse(status_code=200, content={"message": "Pelicula eliminada"})
    db = Session()
    one_movie = MovieService(db).get_movie(id)

    if one_movie:
        MovieService(db).delete_movie(id)
        return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Pelicula eliminada"})
    else:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Pelicula no encontrada"})
