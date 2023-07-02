from config.database import Base
from sqlalchemy import Column, Integer, String, Float

# CON BASE DECIMOS QUE SERÁ NUESTRA ENTIDAD EN LA BASE DE DATOS
class Movie(Base):
    # CON __tablename__ INDICAMOS EL NOMBRE DE NUESTRA TABLA
    __tablename__ = "movies"

    id = Column(
        Integer,
        primary_key=True,
    )

    title = Column(
        String,
    )

    overview = Column(
        String,
    )

    year = Column(Integer)

    rating = Column(Float)

    category = Column(String)

