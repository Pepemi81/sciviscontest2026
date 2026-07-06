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

## [28/06/2026] - Funcionalidad inicial del task 0 (Jose Miguel Molina y Rodrigo Jiménez Vielba)

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

## [04/07/2026] - Reorganización de archivos (Jose Miguel Molina)

### Cambios
* Agrupados los scripts: `task0_data.py`, `visualize_by_date.py` y `visualize_by_timestep.py` en la carpeta `tasks\task0`.

---

## [05/07/2026] - Funcionalidad inicial del task 1 (Hilario Javier del Valle Escolar, Rodrigo Jiménez Vielba y Jose Miguel Molina)

### Añadido
* Creación del script `task1_data.py` para gestionar la conexión con los datos del experimento DYAMOND GEOS mediante OpenVisus.
* Implementada la función `get_data_by_timestep` para descargar volúmenes 3D de las variables atmosféricas (`u`, `v`, etc.) indicando la face del cubed-sphere, el timestep y el intervalo vertical (`z`).
* Implementada la función `get_date_by_timestep` para convertir un timestep del experimento en su fecha y hora correspondientes.
* Creación del script `visualize_by_timestep.py` como ejemplo de descarga y visualización de una sección del volumen mediante Matplotlib.

### Cambios
* Definidos los límites válidos del experimento (`MAX_TIMESTEP`, `MAX_FACES` y niveles `z`) para facilitar la validación de parámetros.
* Añadidas comprobaciones de rango para los parámetros `timestep`, `face` e intervalo `z`, mostrando mensajes de advertencia cuando los valores introducidos no son válidos.
* Automatizada la construcción de la URL del dataset a partir de la variable y la face solicitadas, evitando mantener rutas independientes para cada conjunto de datos.

### Tests
* Verificada la descarga correcta de datos tridimensionales desde distintas faces del modelo GEOS utilizando OpenVisus.
* Comprobada la conversión de timesteps a fecha y hora mediante la función `get_date_by_timestep`.
* Validado el script de ejemplo mostrando correctamente un corte del volumen descargado mediante `imshow`.

## [06/07/2026]
# Resumen de Cambios: Tarea 0 (Iago Otero y Alberto Garcia)

Este documento detalla las modificaciones y mejoras finales realizadas sobre los tres scripts principales que conforman la Tarea 0 para la descarga y visualización de datos climáticos desde OpenVisus.

## 1. `task0_data.py` (Módulo Principal de Datos)
Este archivo sufrió la mayor reestructuración para hacer la descarga de datos más robusta, modular y fácil de utilizar.

* **Creación de la función `select_ssp(date_str, ssp)`:** * Se extrajo la lógica condicional del escenario a esta nueva función.
    * Fuerza el escenario `"historical"` automáticamente si la fecha solicitada es igual o anterior al **31 de diciembre de 2011**. 
    * Si la fecha es posterior, respeta el escenario especificado por el usuario.
* **Actualización de `get_date_by_timestep(ov_timestep)`:** * Se reescribió completamente la lógica. En lugar de tratar el `timestep` como un índice lineal de días desde 1950, ahora acepta el **índice absoluto de OpenVisus** 
    * Utiliza un algoritmo de ingeniería inversa iterando sobre los años y los días del año (no se contemplan años bisiestos debido a la estructura de datos de OpenVisus) para deducir a qué fecha exacta corresponde un índice de OpenVisus.
* **Refactorización de `get_data_by_timestep(variable, timestep, ssp)`:** * Se usa la función `get_date_by_timestep` para obtener la fecha correspondiente y poder usarla en la función `select_ssp`. Y utiliza el `timestep` para leer los datos directamente.

## 2. `visualize_by_date.py` (Ejemplo por Fecha)
Las modificaciones en este script de ejemplo fueron ajustes menores de compatibilidad con el nuevo módulo de datos:

* Se ha creado variable de tipo *string* `target_scenario` para alimentar correctamente a `task0_data.get_data_by_date`.
* El código mantiene su estructura limpia, llamando a la función por fecha y mostrando el mapa de calor con `matplotlib`.

## 3. `visualize_by_timestep.py` (Visualización por Timestep)
Este script se ajustó para reflejar la nueva lógica de los timesteps absolutos requeridos por el servidor.

* **Uso de Timesteps Absolutos:** La variable `target_timestep` ahora se configura con índices reales de OpenVisus, en lugar de utilizar un rango lineal.
* **Ajuste de Escenario:** Al igual que en el script de fechas, se ha creado `target_scenario`.
* **Mejora en el Título del Gráfico:** Aprovecha la nueva capacidad de la función `get_date_by_timestep` para mostrar tanto el índice numérico (`target_timestep`) como la fecha real deducida (`real_date`) en el título del gráfico, permitiendo al usuario saber exactamente qué día está observando.
