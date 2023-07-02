from pydantic import BaseModel, Field

from typing import Optional


# HEREDAR DE BASEMODEL PARA CREAR NUESTRA CLASE (ESQUEMA DE PELICULAS, VALIDACIONES Y EJEMPLO DE SWAGGER)
class Movie(BaseModel):
    id: Optional[int] = None  # DEFINIR UN ATRIBUTO OPCIONAL Y ENTERO
    title: str = Field(min_length=5, max_length=15, default="Mi película")
    overview: str = Field(min_length=15, max_length=50, default="Descripción de la película")
    year: int = Field(ge=1900, le=2023)
    rating: float = Field(ge=0, le=10)
    category: str = Field(min_length=5, max_length=15)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Mi película",
                "overview": "Descripción de la película",
                "year": 2022,
                "rating": 9.8,
                "category": "Acción"
            }
        }
