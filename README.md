# Proyecto de Alineamiento de Secuencias

Este proyecto implementa un pipeline de procesamiento para alinear secuencias genéticas. Utiliza la herramienta Clustal Omega para el alineamiento y proporciona funcionalidades para filtrar y verificar la calidad de los alineamientos.

## Estructura del Proyecto

El código se organiza en varios módulos dentro de la carpeta `src`, cada uno dedicado a una parte específica del proceso:

- `procesamiento_secuencias.py`: Funciones para preprocesar las secuencias antes del alineamiento.
- `alineamiento.py`: Funciones para alinear las secuencias y comprobar la calidad de los alineamientos.

Los scripts y datos necesarios se encuentran en las carpetas `data` y `tools`.

## Requisitos

Para ejecutar este proyecto, es necesario tener Python instalado en tu sistema, así como acceso a Clustal Omega. La ruta a Clustal Omega debe ser especificada en el script principal. Asegúrate de que los directorios y rutas en el script principal coincidan con tu estructura de archivos local.

## Configuración

1. Clona este repositorio en tu máquina local.
2. Asegúrate de tener instalado Python 3.6 o superior.
3. Descarga y configura Clustal Omega en la carpeta `tools`.


## Uso

Para ejecutar el pipeline, navega al directorio del proyecto y ejecuta:
python run_pipeline.py


## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor, crea un fork del repositorio, realiza tus cambios, y envía un pull request. 

## Licencia

Este proyecto está licenciado bajo la Licencia MIT.
