import requests
import gzip
import shutil
import os

# URL del archivo CSV (comprimido)
url = "http://data.phishtank.com/data/online-valid.csv.gz"

try:
    # Descargar el archivo comprimido
    response = requests.get(url)
    response.raise_for_status()

    # Guardar el archivo comprimido localmente
    with open("phishing_urls.csv.gz", "wb") as file:
        file.write(response.content)

    print("Archivo CSV comprimido descargado correctamente.")

    # Descomprimir el archivo CSV
    with gzip.open("phishing_urls.csv.gz", "rb") as f_in:
        with open("phishing_urls.csv", "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)

    print("Archivo CSV descomprimido correctamente.")

    # Leer el archivo CSV y extraer las URLs
    phishing_urls = []
    with open("phishing_urls.csv", "r", encoding='utf-8') as csv_file:
        # Leer la primera línea para saltar los encabezados
        next(csv_file)

        # Leer líneas y extraer URLs (suponiendo que la URL está en la segunda columna)
        for line in csv_file:
            columns = line.split(",")  # Divide la línea en columnas
            if len(columns) > 1:  # Asegurarse de que hay suficientes columnas
                phishing_urls.append(columns[1].strip())  # Añadir la URL (segunda columna)

    # Guardar las URLs de phishing en un archivo de texto
    with open("phishing_urls.txt", "w") as txt_file:
        for url in phishing_urls:
            txt_file.write(url + "\n")

    print(f"Se han guardado {len(phishing_urls)} URLs de phishing en 'phishing_urls.txt'.")

    # Limpiar archivos temporales
    os.remove("phishing_urls.csv.gz")
    os.remove("phishing_urls.csv")

except requests.RequestException as e:
    print(f"Error al descargar el archivo: {e}")
except Exception as e:
    print(f"Error: {e}")
