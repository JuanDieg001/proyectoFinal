#Definicion de un DTO (data transfer object) para Galaxia
class GalaxiaDTO:
    def __init__(self, id=None, nombre=None, tipo=None):
        self._id = id
        self._nombre = nombre
        self._tipo = tipo

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, value):
        self._tipo = value

#Definicion de un DTO (data transfer object) para Planeta
class PlanetaDTO(GalaxiaDTO):
    def __init__(self, id=None, nombre=None, tipo=None, masa=None, distancia_al_sol=None, galaxia_id=None):
        self._id = id
        self._nombre = nombre
        self._tipo = tipo
        self._masa = masa
        self._distancia_al_sol = distancia_al_sol
        self._galaxia_id = galaxia_id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, value):
        self._tipo = value

    @property
    def masa(self):
        return self._masa

    @masa.setter
    def masa(self, value):
        self._masa = value

    @property
    def distancia_al_sol(self):
        return self._distancia_al_sol

    @distancia_al_sol.setter
    def distancia_al_sol(self, value):
        self._distancia_al_sol = value

    @property
    def galaxia_id(self):
        return self._galaxia_id

    @galaxia_id.setter
    def galaxia_id(self, value):
        self._galaxia_id = value
