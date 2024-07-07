# Music Ranking API

Esta es una API para gestionar un ranking de éxitos musicales. Permite listar, añadir, modificar, eliminar y "tocar" canciones en el ranking.

## Requisitos

- Python 3
- Flask
- Uvicorn

## Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd tu-repositorio
2.	Crear un entorno virtual y actívalo:
   
python3 -m venv venv
source venv/bin/activate  # En macOS/Linux
venv\Scripts\activate  # En Windows

	3.	Instala las dependencias:
 pip install -r requirements.txt

## Uso

1.	Ejecutar la aplicación:
 uvicorn main:app --reload

2.	Abrir en el navegador: http://127.0.0.1:8000/docs para ver la documentación interactiva de la API.

## Endpoints

	•	GET /ranking - Obtener el ranking de canciones.
	•	POST /song - Añadir una nueva canción.
	•	GET /song/{id} - Obtener la información completa de una canción específica.
	•	PUT /song/{id} - Modificar una canción específica.
	•	DELETE /song/{id} - Eliminar una canción específica.
	•	GET /song/touch/{id} - Realizar un “touch” a una canción.
