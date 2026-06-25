# Changelog

Todos los cambios notables y modificaciones del entorno de desarrollo para el proyecto SciVis Contest 2026 se registrarán en este archivo.

---

## [25/06/2026] - Inicialización del proyecto (Jose Miguel Molina)

### Añadido
* Clonación del repositorio oficial de la asignatura desde la dirección remota `https://github.com/sci-visus/sciviscontest2026.git`.
* Creación de un Fork del proyecto en la cuenta personal de GitHub para gestionar el desarrollo del equipo.
* Configuración de permisos de colaboración en el Fork para permitir el acceso y la integración de commits por parte de los miembros del grupo.
* Inicialización del entorno virtual local (`.venv`) en la raíz del proyecto mediante el comando `uv init`.
* Instalación y traducción de las dependencias base especificadas en el archivo `environment.yml` del equipo docente usando comandos nativos de `uv`: `jupyterlab`, `matplotlib`, `xarray`, `netcdf4`, `xmltodict`, `colorcet`, `boto3`, `basemap`, `bokeh`, `panel` e `intake`.
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