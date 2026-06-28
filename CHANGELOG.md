# Changelog

Todos los cambios notables y modificaciones del entorno de desarrollo para el proyecto SciVis Contest 2026 se registrarán en este archivo.

---

## [25/06/2026] - Inicialización del proyecto (Jose Miguel Molina)

### Añadido
* Clonación del repositorio oficial de la asignatura desde la dirección remota `https://github.com/sci-visus/sciviscontest2026.git`.
* Creación de un Fork del proyecto en la cuenta personal de GitHub para gestionar el desarrollo del equipo.
* Configuración de permisos de colaboración en el Fork para permitir el acceso y la integración de commits por parte de los miembros del grupo.
* Inicialización del entorno virtual local (`.venv`) en la raíz del proyecto mediante el comando `uv init`.
* Instalación y traducción de las dependencias base especificadas en el archivo `environment.yml` del equipo docente usando comandos nativos de `uv`: `jupyterlab`, `matplotlib`, `xarray`, `netcdf4`, `xmltodict`, `colorcet`, `boto3`, `basemap`, `bokeh`, `panel`, `intake`, `intake-nexgddp`, `requests` y `aiohttp`.
* Adición de las librerías especializadas para el streaming remoto de datos multidimensionales y cartografía: `OpenVisus`, `openvisuspy` y `cartopy`.

### Cambios
* Vinculación del cuaderno de Jupyter en Visual Studio Code al Kernel del entorno virtual local (`Python 3.13.9`), asegurando que las dependencias añadidas con `uv` se referencien de forma correcta.

### Tests
* Comprobación y arranque exitoso del servidor de JupyterLab, confirmando el acceso local a la carpeta de ejemplos de cuadernos provista por la cátedra (`notebooks_examples`).

## Próximos Pasos

* Analizar el código de carga remota mediante OpenVisus en los notebooks de ejemplo para comprender la infraestructura de datos sin descarga local.
* Desarrollar los primeros scripts de filtrado y segmentación de datos en busca de anomalías térmicas o dinámicas.
* Establecer la estructura de comunicación entre los cuadernos de análisis y los scripts de renderizado 3D en VTK.

---

## [28/06/2026] - Funcionalidad inicial del task 0 (Jose Miguel Molina y Rodrigo Jiménez)

### Añadido
* Creación del script `task0_data.py` para dejar lista la conexión con el servidor y la gestión de la temperatura y precipitación.
* Puestos comentarios (docstrings) en español en todas las funciones para que salga la ayuda con el ratón al escribir el código.
* Creación del script `visualize_by_date.py` como ejemplo para pedir y ver los datos usando una fecha.
* Creación del script `visualize_by_timestep.py` como ejemplo para pedir y ver los datos usando el número de timestep.

### Cambios
* Corregido el año de inicio del dataset al 1 de enero de 1950 tras comprobar los límites reales del servidor.
* Arreglado el problema de los años bisiestos del servidor cambiando el sistema por un contador de días limpio (de 0 a 22644).
* Añadido el uso de `timedelta` para poder sacar la fecha real a partir de un timestep y usarla en los títulos de las gráficas.
* Modificada la función `get_data_by_timestep` para que traduzca el número del slider de los de visualización al índice raro que pide el servidor.

### Tests
* Comprobado que los scripts de ejemplo funcionan bien importando el script de datos y que no hace falta usar OpenVisus en ellos.

---
