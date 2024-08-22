Propósito del Código

Este script tiene como propósito gestionar un sistema de información para galaxias y planetas utilizando una base de datos MySQL. El sistema permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre galaxias y planetas, proporcionando una interfaz de usuario basada en texto para interactuar con la base de datos. Además, el código incluye un servicio de registro de logs (LogService) que graba en un archivo log.txt todas las acciones realizadas en el sistema, como la creación, búsqueda, actualización y eliminación de galaxias y planetas. Configuración y Ejecución

    Requisitos Previos

    Python 3.7 o superior: Asegúrate de tener Python instalado en tu sistema.

    Instalar dependencias: Asegúrate de tener los siguientes paquetes instalados: SQLAlchemy: para manejar la conexión y las operaciones de la base de datos. mysql-connector-python: para conectar con la base de datos MySQL.

    Puedes instalarlos usando pip:

    bash

pip install sqlalchemy mysql-connector-python

Base de Datos MySQL: Configura una base de datos MySQL con las siguientes credenciales:

Usuario: root
Contraseña: admin
Puerto: 3307
Nombre de la base de datos: sistema_solar

Si no existe, créala ejecutando el siguiente comando en tu terminal MySQL:

CREATE DATABASE sistema_solar;

    Configuración del Proyecto

    Estructura de Carpetas

    ├── accessData │ ├── conexionORM.py │ └── entities │ └── planetaModel.py ├── dominio │ └── entities │ └── modelsOrm │ └── planetaDTO.py ├── servicio │ ├── logService.py │ └── planetaServicio.py └── main.py

    Archivo de Configuración de Conexión: En accessData/conexionORM.py, define la clase Database que maneje la conexión a la base de datos.

    Modelos de Datos: Define los modelos ORM en accessData/entities/planetaModel.py y los DTOs en dominio/entities/modelsOrm/planetaDTO.py.

    Servicios: Implementa las funciones de creación, actualización, eliminación y búsqueda de galaxias y planetas en servicio/planetaServicio.py.

    Registro de Logs: Asegúrate de que el archivo logService.py esté configurado para guardar los logs en la carpeta servicio.

    Ejecución del Código

    Inicia el programa: Ejecuta el script principal desde la terminal: python main.py

    Interacción: El sistema mostrará un menú principal donde puedes seleccionar la opción de gestionar galaxias o planetas.

Ejemplos de Uso y Salidas Esperadas Gestión de Galaxias

Crear Galaxia:
    Entrada: nombre = "Vía Láctea", tipo = "espirales"
    Salida: Galaxia creada exitosamente.
    Log: 2024-08-07 12:00:00 - entro a la opcion crear galaxia Vía Láctea

Mostrar Galaxias:
    Entrada: Opción 2 en el menú de galaxias.
    Salida: ID: 1, Nombre: Vía Láctea, Tipo: espirales
    Log: 2024-08-07 12:01:00 - entro a la opcion mostrar galaxia

Gestión de Planetas

Crear Planeta:
    Entrada: nombre = "Tierra", tipo = "rocoso", masa = 5972, distancia_al_sol = 149600000, galaxia_id = 1
    Salida: Planeta creado exitosamente.
    Log: 2024-08-07 12:05:00 - entro a la opcion crear planeta: Tierra

Mostrar Planetas:
    Entrada: Opción 2 en el menú de planetas.
    Salida:

    Galaxia ID: 1, Nombre: Vía Láctea, Tipo: espirales
    Planeta ID: 1, Nombre: Tierra, Tipo: rocoso, Masa: 5972, Distancia al Sol: 149600000
    Log: 2024-08-07 12:06:00 - entro a la opcion mostrar todos los planetas
