import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# NOMBRE DE NUESTRO ARCHIVO SQLITE
sqlite_file_name = "../database.sqlite"

# OBTENEMOS LA RUTA DE NUESTRO ARCHIVO SQLITE
# __file__ ES UNA VARIABLE QUE CONTIENE EL NOMBRE DEL ARCHIVO DEL DIRECTORIO ACTUAL
base_dir = os.path.dirname(os.path.realpath(__file__))

# CREAMOS LA URL DE NUESTRA BASE DE DATOS
database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"

# CREAMOS EL MOTOR DE NUESTRA BASE DE DATOS E INDICAMOS QUE IMPRIMA
engine = create_engine(database_url, echo=True)

# CREAMOS LA SESIÓN DE NUESTRA BASE DE DATOS
Session = sessionmaker(bind=engine)

# MANIPULAR NUESTRA BASE DE DATOS CON MODELOS
Base = declarative_base()