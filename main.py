from accessData.conexionORM import Database  # Importar la clase Database
from servicio.logService import LogService
from accessData.entities.planetaModel import BaseDeDatos, Galaxia, Planeta
from dominio.entities.modelsOrm.planetaDTO import GalaxiaDTO, PlanetaDTO
from servicio.planetaServicio import GalaxiaService
from servicio.genericService import GenericRepository

DATABASE_URL = "mysql+mysqlconnector://root:admin@localhost:3307/instituto"

def main():
    
    galaxia_service = GalaxiaService(db)
    planeta_service = GalaxiaService(db)
    serviceGeneric = GenericRepository[Galaxia](Galaxia, db)
    log_service = LogService()

    while True:
        menuPrincipal="""
[(1)Gestión de galaxias]      
[(2)Gestión de planetas]
[(3)salir]
"""
        print(menuPrincipal)

        opcion = input("Seleccione una opción: ")

        if opcion == "1":   
            while True:
                menu = """
                            --- Menu Galaxia ---
[(1)Crear Galaxia]      [(3)Buscar Galaxia]     [(5) Eliminar Galaxia]
[(2) Mostrar Galaxias]  [(4)Actualizar Galaxia] [(6) Volver al menu Principal]
        """
                print(menu)

                opcion = input("Seleccione una opción: ")

                if opcion == "1":#crear galaxia
                    
                    nombre = input("Ingrese el nombre: ")
                    tipo = input("Ingrese el tipo de galaxia: (espirales, elipticas, irregular) ")
                    

                    galaxiaDTO = GalaxiaDTO(None, nombre, tipo)

                    #galaxia_service.crear_galaxia(galaxiaDTO)
                    galaxiaDTO = serviceGeneric.create(nombre=galaxiaDTO.nombre, tipo=galaxiaDTO.tipo)
                    #print(vars(galaxiaDTO))
                    print(f"nombre: {nombre} tipo: {tipo}")
                    log_service.logger("entro a la opcion crear galaxia " + str(galaxiaDTO.nombre))

                elif opcion == "2":#mostrar galaxia
                    
                    #galaxias = galaxia_service.mostrar_galaxias()
                    galaxias = serviceGeneric.getAll()
                    
                    for galaxia in galaxias:
                        print(f"ID: {galaxia.id}, Nombre: {galaxia.nombre}, tipo: {galaxia.tipo} ")

                    log_service.logger("entro a la opcion mostrar galaxia ")

                elif opcion == "3":#buscar galaxia
                    
                    id = int(input("Ingrese el ID de la galaxia: "))
                    #galaxias = galaxia_service.buscar_galaxia(id)
                    galaxias = serviceGeneric.get(id)
                    
                    if galaxias:
                        print(f"ID: {galaxias.id}, Nombre: {galaxias.nombre}, Apellido: {galaxias.tipo}")
                    else:
                        print("Galaxia no encontrada")
                    
                    log_service.logger("entro a la opcion buscar galaxia ")
                
                elif opcion == "4":#actualizar galaxia
                    
                    id = int(input("Ingrese el ID de la galaxia que desea actualizar: "))
                
                    nombre = input("Ingrese el nuevo nombre: ")
                    tipo = input("Ingrese el nuevo tipo: ")
                
                    galaxia = GalaxiaDTO(id, nombre, tipo)
                    #galaxia_service.actualizar_galaxia(galaxia)
                    serviceGeneric.update(id, galaxia)
                    print("Glaxia actualizada")
                    log_service.logger("entro a la opcion actualizar y se actualizó el id: " +str(id))

                elif opcion == "5":#eliminar galaxia

                    galaxia_id = int(input("Ingrese el ID del planeta que desea eliminar: "))
                    #galaxia_service.borrar_galaxia(galaxia_id)
                    serviceGeneric.delete(galaxia_id)
                    print("Galaxia eliminada")
                    log_service.logger("entro a la opcion eliminar y se borro el id: " +str(galaxia_id))
                
                elif opcion == "6":#volver al menu
                    galaxia_service.cerrarConexion()
                    break
                
                else:
                    print("Opción inválida. Por favor, seleccione una opción válida.")
        
        elif opcion == "2":
            while True:
                menu = """
                            --- Menu Planeta ---
[(1)Crear Planeta]      [(3)Buscar Planeta]     [(5) Eliminar Planeta]
[(2) Mostrar Planetas]  [(4)Actualizar Planeta] [(6) Volver al menu Principal]
        """
                print(menu)

                opcion = input("Seleccione una opción: ")

                if opcion == "1":#Crear Planeta
                    
                    #galaxias = galaxia_service.mostrar_galaxias()
                    galaxias = serviceGeneric.getAll()

                    if not galaxias:
                        print("No hay galaxias disponibles para seleccionar.")
                    else:
                        print("Ecoja en que galaxia desea crear un planeta:")
                        for galaxia in galaxias:
                            print(f"ID: {galaxia.id}, Nombre: {galaxia.nombre} Tipo: {galaxia.tipo}")

                    galaxia_id = int(input("Ingrese el ID de la galaxia seleccionada: "))
                    nombre_planeta = input("Ingrese el nombre del planeta: ")
                    tipo_planeta = input("Ingrese el tipo del planeta: ")
                    masa_planeta = int(input("Ingrese la masa del planeta: "))
                    distancia_al_sol = int(input("Ingrese la distancia al sol del planeta: "))

                    planetaDTO = PlanetaDTO(
                    id=None,  # Esto será generado automáticamente por la base de datos
                    nombre=nombre_planeta,
                    tipo=tipo_planeta,
                    masa=masa_planeta,
                    distancia_al_sol=distancia_al_sol,
                    galaxia_id=galaxia_id
                    )

                    planeta_service.crear_planeta(planetaDTO)
                    print("Planeta creado exitosamente.")
                    log_service.logger("entro a la opcion crear planeta: " +str(nombre_planeta))
                

                elif opcion == "2":# Mostrar todas las Galaxias con sus Planetas
                    
                    galaxias_y_planetas = galaxia_service.mostrar_galaxias_y_planetas()
                    for galaxia in galaxias_y_planetas:
                        galaxia_str = (f"Galaxia ID: {galaxia.id}, "
                                    f"Nombre: {galaxia.nombre}, "
                                    f"Tipo: {galaxia.tipo}")

                    planetas_str = "\n".join(
                        [f"Planeta ID: {planeta.id}, "
                        f"Nombre: {planeta.nombre}, "
                        f"Tipo: {planeta.tipo}, "
                        f"Masa: {planeta.masa}, "
                        f"Distancia al Sol: {planeta.distancia_al_sol}"
                        for planeta in galaxia.planetas]
                    )

                    print(f"{galaxia_str}\n{planetas_str}\n")
                    log_service.logger("entro a la opcion mostrar todos los planetas")


                elif opcion == "3":#buscar planeta
                    galaxia_id = int(input("Ingrese el ID de la galaxia: "))
                    planeta_id = int(input("Ingrese el ID del planeta: "))
                    planeta = galaxia_service.buscar_planeta_en_galaxia(galaxia_id, planeta_id)
                    if planeta:
                        print(f"Planeta encontrado: ID: {planeta.id}, Nombre: {planeta.nombre}, Tipo: {planeta.tipo}, Masa: {planeta.masa}, Distancia al Sol: {planeta.distancia_al_sol}")
                    else:
                        print("No se encontró el planeta en la galaxia especificada.")
                    log_service.logger("entro a la opcion buscar planeta: " +str(id))


                elif opcion == "4":#actualizar planeta

                    galaxia_id = int(input("Ingrese el ID de la galaxia: "))
                    planeta_id = int(input("Ingrese el ID del planeta: "))
                    planeta = galaxia_service.buscar_planeta_en_galaxia(galaxia_id, planeta_id)
                    if planeta:
                        print(f"Planeta encontrado: ID: {planeta.id}, Nombre: {planeta.nombre}, Tipo: {planeta.tipo}, Masa: {planeta.masa}, Distancia al Sol: {planeta.distancia_al_sol}")
                        nombre = input("Nuevo nombre del planeta: ")
                        tipo = input("Nuevo tipo del planeta: ")
                        masa = input("Nueva masa del planeta: ")
                        distancia_al_sol = input("Nueva distancia al sol del planeta: ")

                        planeta_dto = PlanetaDTO(
                            id=galaxia_id, 
                            nombre=nombre, 
                            tipo=tipo, 
                            masa=masa, 
                            distancia_al_sol=distancia_al_sol, 
                            galaxia_id=galaxia_id
                        )

                        actualizado = planeta_service.actualizar_planeta(planeta_dto)

                        if actualizado:
                            print("Planeta actualizado con éxito:")
                            print(f"ID: {actualizado.id}, Nombre: {actualizado.nombre}, Tipo: {actualizado.tipo}, Masa: {actualizado.masa}, Distancia al Sol: {actualizado.distancia_al_sol}")
                        else:
                            print("No se pudo actualizar el planeta.")

                    else:
                        print("No se encontró el planeta en la galaxia especificada.")
                    log_service.logger("entro a la opcion actualizar planeta y se actualizó el id: " +str(id))

                      

                elif opcion == "5":#eliminar planeta
                    galaxia_id = int(input("Ingrese el ID de la galaxia: "))
                    planeta_id = int(input("Ingrese el ID del planeta: "))
                    planeta = galaxia_service.buscar_planeta_en_galaxia(galaxia_id, planeta_id)
                    if planeta:
                        print(f"Planeta encontrado: ID: {planeta.id}, Nombre: {planeta.nombre}, Tipo: {planeta.tipo}, Masa: {planeta.masa}, Distancia al Sol: {planeta.distancia_al_sol}")
                        respuesta = input("¿esta seguro que quiere eliminar el planeta? [S/n]")

                        if respuesta == "S" or "s":
                            galaxia_service.borrar_planeta(galaxia_id)
                            print("Planeta eliminado")
                            log_service.logger("entro a la opcion eliminar y se borro el id: " +str(galaxia_id))
                        else:
                            print("Planeta no eliminado")
                            log_service.logger("entro a la opcion eliminar y no se borro ningun planeta")
                    
                    else:
                        print("Planeta no encontrado")
                    log_service.logger("entro a la opcion eliminar y no encontro ningun planeta")


                elif opcion == "6":#volver al menu principal
                    planeta_service.cerrarConexion()
                    break

        elif opcion == "3":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
        

    

if __name__ == "__main__":
    db = Database(DATABASE_URL)
    engine = db.engine
    BaseDeDatos.metadata.create_all(bind=engine)
    main()