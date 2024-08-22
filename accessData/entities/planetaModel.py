from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

BaseDeDatos = declarative_base()

class Galaxia(BaseDeDatos):
    __tablename__ = "galaxias"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), unique=True, index=True)
    tipo = Column(String(50))
    # Relación uno a muchos con Planeta
    planetas = relationship("Planeta", back_populates="galaxia")

class Planeta(BaseDeDatos):
    __tablename__ = "planetas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), unique=True, index=True)
    tipo = Column(String(50))
    masa = Column(Integer)
    distancia_al_sol = Column(Integer)
    galaxia_id = Column(Integer, ForeignKey('galaxias.id'))

    # Relación muchos a uno con Galaxia
    galaxia = relationship("Galaxia", back_populates="planetas")


# Define la URL de conexión a la base de datos
DATABASE_URL = "mysql+mysqlconnector://root:admin@localhost:3307/instituto"

# Crea el motor de la base de datos
engine = create_engine(DATABASE_URL)

# Crea todas las tablas en la base de datos
BaseDeDatos.metadata.create_all(engine)

print("Tablas de galaxias y planetas creadas exitosamente.")
