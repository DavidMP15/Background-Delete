import os
from datetime import datetime
from rembg import remove


class QuitarFondo:
    def __init__(self, input_folder, output_folder):
        self.input_folder = input_folder
        self.output_folder = output_folder

    def procesar_imagen(self):
        carpeta_procesada = os.path.join(self.output_folder, datetime.now().strftime('%Y-%m-%d %H-%M-%S'))
        os.makedirs(carpeta_procesada, exist_ok=True)

        for nombre_archivo in os.listdir(self.input_folder):
            if nombre_archivo.lower().endswith(('.png', '.jpg', '.jpeg')):
                input_path = os.path.join(self.input_folder, nombre_archivo)
                output_path = os.path.join(carpeta_procesada, nombre_archivo)
                self._quitar_fondo(input_path, output_path)
                self._mover_imagen_original(input_path, carpeta_procesada)

    def _quitar_fondo(self, input_path, output_path):
        with open(input_path, 'rb') as inp, open(output_path, 'wb') as out:
            fondo_salida = remove(inp.read())
            out.write(fondo_salida)

    def _mover_imagen_original(self, input_path, dest_path):
        carpeta_originales = os.path.join(dest_path, 'originales')
        os.makedirs(carpeta_originales, exist_ok=True)

        nombre_archivo = os.path.basename(input_path)
        new_path = os.path.join(carpeta_originales, nombre_archivo)
        os.rename(input_path, new_path)


if __name__ == '__main__':
    input_folder = "Inicial"
    output_folder = "Resultado"

    quitar_fondo = QuitarFondo(input_folder, output_folder)
    quitar_fondo.procesar_imagen()
