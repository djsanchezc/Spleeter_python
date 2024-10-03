import os
from flask import Blueprint, request, jsonify
from spleeter.separator import Separator

routes = Blueprint('routes', __name__)

@routes.route('/separar', methods=['POST'])
def separar_audio():
    # Obtener archivo de audio y opción desde el frontend
    file = request.files['file']
    opcion = request.form['opcion']

    # Guardar archivo temporalmente
    input_audio = os.path.join("temp", file.filename)
    file.save(input_audio)

    # Crear la carpeta de salida
    output_path = os.path.join("temp", "output")
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Usar Spleeter para separar
    separator = Separator('spleeter:2stems')
    separator.separate_to_file(input_audio, output_path)

    # Seleccionar la pista dependiendo de la opción
    if opcion == 'voces':
        output_file = os.path.join(output_path, 'vocals.wav')
    elif opcion == 'instrumental':
        output_file = os.path.join(output_path, 'accompaniment.wav')
    else:
        return jsonify({'error': 'Opción no válida'}), 400

    # Devolver la ruta del archivo de salida
    return jsonify({'output_file': output_file})
