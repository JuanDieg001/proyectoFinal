from accessData.entities.planetaModel import Galaxia, Planeta
from accessData.conexionORM import Database
from dominio.entities.modelsOrm.planetaDTO import GalaxiaDTO, PlanetaDTO
from sqlalchemy.orm import joinedload
from servicio.logService import LogService
from abc import ABC, abstractmethod

class Crud(ABC):
    @abstractmethod
    def crear_galaxia(self, galaxia_dto: GalaxiaDTO):
        pass

    @abstractmethod
    def mostrar_galaxias(self):
        pass

    @abstractmethod
    def buscar_galaxia(self, id):
        pass

    @abstractmethod
    def actualizar_galaxia(self, galaxia_dto: GalaxiaDTO):
        pass

    @abstractmethod
    def borrar_galaxia(self, id):
        pass

class GalaxiaService(Crud):

    def __init__(self, database: Database):
            self.db = database
            self.log_service = LogService()

    def crear_galaxia(self, galaxia_dto: GalaxiaDTO):
        session = self.db.get_session()
        db_galaxia = Galaxia(nombre = galaxia_dto.nombre, tipo = galaxia_dto.tipo)
        session.add(db_galaxia)
        session.commit()
        session.refresh(db_galaxia)
        session.close()
        return db_galaxia
    
    def mostrar_galaxias(self):
        session = self.db.get_session()
        galaxias = session.query(Galaxia).all()
        session.close()
        return galaxias
    
    def buscar_galaxia(self, id):
        session = self.db.get_session()
        galaxia = session.query(Galaxia).filter(Galaxia.id == id).first()
        session.close()
        return galaxia
    
    def actualizar_galaxia(self, galaxia_dto: GalaxiaDTO):
        session = self.db.get_session()
        galaxia = session.query(Galaxia).filter(galaxia_dto.id == galaxia_dto.id).first()
        if galaxia_dto.nombre:
            galaxia.nombre = galaxia_dto.nombre
        if galaxia_dto.tipo:
            galaxia.tipo = galaxia_dto.tipo
        
        session.commit()
        session.refresh(galaxia)
        session.close()
        return galaxia
    
    def borrar_galaxia(self, id):
        session = self.db.get_session()
        galaxia = session.query(Galaxia).filter(Galaxia.id == id).first()
        session.delete(galaxia)
        session.commit()
        session.close()
        return {"galaxia eliminada"}
    
    def crear_planeta(self, planeta_dto: PlanetaDTO):
        session = self.db.get_session()
        db_planeta = Planeta(
        nombre=planeta_dto.nombre,
        tipo=planeta_dto.tipo,
        masa=planeta_dto.masa,
        distancia_al_sol=planeta_dto.distancia_al_sol,
        galaxia_id=planeta_dto.galaxia_id
        )
        session.add(db_planeta)
        session.commit()
        session.refresh(db_planeta)
        session.close()
        return db_planeta

    def mostrar_planetas(self):
        session = self.db.get_session()
        planetas = session.query(Planeta).all()
        session.close()
        return planetas
    
    def mostrar_galaxias_y_planetas(self):
        session = self.db.get_session()
        galaxias = session.query(Galaxia).options(joinedload(Galaxia.planetas)).all()
        return galaxias
    
    def buscar_planeta_en_galaxia(self, galaxia_id, planeta_id):
        session = self.db.get_session()
        planeta = session.query(Planeta).filter(
            Planeta.id == planeta_id,
            Planeta.galaxia_id == galaxia_id
        ).first()
        session.close()
        return planeta
    
    def actualizar_planeta(self, planeta_dto: PlanetaDTO):
        session = self.db.get_session()
        
        # Buscar el planeta en la galaxia específica
        planeta = session.query(Planeta).filter(
            Planeta.id == planeta_dto.id,
            Planeta.galaxia_id == planeta_dto.galaxia_id
        ).first()
        
        if not planeta:
            session.close()
            return None
        
        # Actualizar el planeta si se encuentra
        if planeta_dto.nombre:
            planeta.nombre = planeta_dto.nombre
        if planeta_dto.tipo:
            planeta.tipo = planeta_dto.tipo
        if planeta_dto.masa is not None:
            planeta.masa = planeta_dto.masa
        if planeta_dto.distancia_al_sol is not None:
            planeta.distancia_al_sol = planeta_dto.distancia_al_sol

        session.commit()
        session.refresh(planeta)
        session.close()
        
        return planeta
    
    def borrar_planeta(self, id):
        session = self.db.get_session()
        planeta = session.query(Planeta).filter(Planeta.id == id).first()
        session.delete(planeta)
        session.commit()
        session.close()
        return {"planeta eliminado"}

    def cerrarConexion(self):
        session = self.db.get_session()
        session.close()