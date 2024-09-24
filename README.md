# Descargador de URLs de Phishing

Este proyecto está diseñado para descargar un archivo CSV comprimido que contiene URLs de phishing desde PhishTank, descomprimirlo, extraer las URLs y guardarlas en un archivo de texto. Este script está destinado para uso ético y profesional, ayudando a detectar y mitigar amenazas de phishing mediante la inteligencia en ciberseguridad.

## Descripción del Código

1. **Importación de Módulos**  
   Se utilizan las siguientes bibliotecas:
   - `requests`: Para realizar solicitudes HTTP y descargar archivos.
   - `gzip`: Para manejar archivos comprimidos en formato Gzip.
   - `shutil`: Para operaciones de archivo, como copiar contenido entre archivos.
   - `os`: Para manejar operaciones del sistema, como eliminar archivos.

2. **URL del Archivo CSV**  
   Se define la URL del archivo CSV comprimido:
   ```python
   url = "http://data.phishtank.com/data/online-valid.csv.gz"
   ```

3. **Descargar el Archivo Comprimido**
   
   El código utiliza `requests.get()` para descargar el archivo. Se maneja cualquier error de red utilizando `response.raise_for_status()`.

5. **Guardar y Descomprimir el Archivo**  

   Después de descargarlo, se guarda localmente como `phishing_urls.csv.gz`. Luego, se descomprime usando `gzip.open()` y se guarda como `phishing_urls.csv`.

6. **Extraer URLs de Phishing**
   
   El código lee el archivo CSV descomprimido y extrae las URLs de phishing. Se asume que la URL está en la segunda columna del archivo. Las URLs se almacenan en una lista.

8. **Guardar las URLs en un Archivo de Texto**
   
   Finalmente, se guardan todas las URLs de phishing en un archivo de texto llamado `phishing_urls.txt`. Se imprime un mensaje indicando cuántas URLs se han guardado.

10. **Limpieza**
    
   Se eliminan los archivos temporales (`phishing_urls.csv.gz` y `phishing_urls.csv`) para evitar el uso innecesario de espacio en disco.

12. **Manejo de Errores**
    
   Se implementa un manejo de errores básico para capturar excepciones relacionadas con la descarga y la manipulación de archivos.

## Requisitos

- Python 3.x
- Bibliotecas: `requests`

Puedes instalar la biblioteca `requests` usando pip:

```bash
pip install requests
```

## Uso

Simplemente ejecuta el script en tu entorno de Python. Se descargará el archivo CSV, se procesará y se generará un archivo de texto con las URLs de phishing. Recuerda usar esta herramienta de manera ética y profesional para ayudar a proteger a las personas y organizaciones de amenazas de phishing.

```bash
python Phishing_URL_Downloader.py
```

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras algún problema o deseas agregar una nueva característica, no dudes en abrir un issue o enviar un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
