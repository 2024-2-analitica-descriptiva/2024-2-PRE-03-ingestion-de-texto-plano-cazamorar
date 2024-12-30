"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

import pandas as pd
import re

def pregunta_01():
    
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    file_path = 'files/input/clusters_report.txt'

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Inicializar lista para almacenar los datos procesados
    data = []
    current_cluster = None

    # Procesar las líneas para extraer los datos
    for line in lines[4:]:  # Saltar las primeras líneas del encabezado
        if re.match(r'^\s*\d+\s+\d+\s+\d+,\d+\s%', line):
            # Si ya hay un cluster actual, agregarlo antes de procesar el nuevo
            if current_cluster:
                current_cluster[3] = re.sub(r',\s+', ', ', current_cluster[3])  # Ajustar comas y espacios
                current_cluster[3] = re.sub(r'\s+', ' ', current_cluster[3]).strip()  # Ajustar espacios
                data.append(current_cluster)

            # Dividir línea en las primeras columnas
            parts = re.split(r'\s{2,}', line.strip(), maxsplit=3)
            cluster = int(parts[0])
            cantidad = int(parts[1])
            porcentaje = float(parts[2].replace(',', '.').replace('%', ''))
            palabras_clave = parts[3] if len(parts) > 3 else ""
            current_cluster = [cluster, cantidad, porcentaje, palabras_clave]
        else:
            # Continuación de palabras clave
            if current_cluster:
                current_cluster[3] += ' ' + line.strip().replace('.', '')

    # Agregar el último cluster procesado
    if current_cluster:
        current_cluster[3] = re.sub(r',\s+', ', ', current_cluster[3])  # Ajustar comas y espacios
        current_cluster[3] = re.sub(r'\s+', ' ', current_cluster[3]).strip()  # Ajustar espacios
        data.append(current_cluster)

    # Crear el DataFrame
    df = pd.DataFrame(data, columns=['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave'])

    # Ajustar nombres de columnas
    df.columns = [col.lower().replace(' ', '_') for col in df.columns]

    return df


#df = pregunta_01()
#print(df)
