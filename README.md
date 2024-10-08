# Audio Separator API

Esta es una API desarrollada con Flask que permite separar las pistas de audio en voces e instrumental utilizando la librería Spleeter.

## Descripción

La API recibe un archivo de audio y una opción (voces o instrumental) desde el frontend, y devuelve la pista de audio correspondiente. Utiliza Spleeter para realizar la separación de las pistas.

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu_usuario/audio-separator-api.git
   cd audio-separator-api

2. Crea y activa un entorno virtual:
   ```bash
   python -m venv env
   source env/bin/activate  # En Windows usa `.\env\Scripts\activate`

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt

## Uso

1. Ejecuta la aplicación:
   ```bash
   python app.py

2. Envía una solicitud POST a /separar con el archivo de audio y la opción deseada (voces o instrumental).

## Dependencias

- Flask
- Flask-CORS
- Spleeter




