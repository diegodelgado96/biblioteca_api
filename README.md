# Proyecto Biblioteca API

Este es un proyecto para una API de biblioteca que se utiliza para gestionar libros, usuarios y más. Está desarrollado utilizando Python, FastAPI y PostgreSQL.

## Requisitos

Antes de comenzar, asegúrate de tener los siguientes requisitos instalados:

- [Python 3.8+](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/download/)

## Instalación

Sigue estos pasos para instalar y ejecutar el proyecto:

1. **Clona el repositorio**:

   Si aún no has clonado el proyecto, puedes hacerlo con el siguiente comando:

   ```bash
   git clone https://github.com/diegodelgado96/biblioteca_api.git
   cd biblioteca_api

1. **Crea un archivo .env en la raiz del proyecto**:

   Por ejemplo:

   ```bash
    DB_USER=postgres
    DB_PASSWORD=12345678A.
    DB_HOST=localhost
    DB_PORT=5432
    DB_NAME=biblioteca

1. **Crear un entorno virtual**:

   Crea un entorno virtual para evitar conflictos con otras dependencias globales:

   ```bash
    python -m venv venv

1. **Crear un entorno virtual**:

   Crea un entorno virtual para evitar conflictos con otras dependencias globales y activarlo:

   ```bash
    python -m venv venv
    source venv/bin/activate //en linux
    venv\Scripts\activate  //en windows

1. **Instalar dependencias**:

   Instala las dependencias necesarias con pip:

   ```bash
    pip install -r requirements.txt

1. **Ejecutar la API**:

   Una vez que todo esté configurado, ejecuta la API con Uvicorn:

   ```bash
    uvicorn app.main:app --reload
    
    # NOTA: Asegurate de tener una base de datos creada en postgres. El nombre de tu base de datos debe ser igual a la variable 'DB_NAME' de las variables de entorno en el archivo .env

1. **Acceder a la documentación interactiva**:

   Una vez que la API esté en funcionamiento, puedes acceder a la documentación interactiva en:

    - Swagger UI: http://127.0.0.1:8000/docs
    - ReDoc: http://127.0.0.1:8000/redoc  