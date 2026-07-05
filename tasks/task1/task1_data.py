import OpenVisus as ov
from datetime import datetime, timedelta

# ----- Config -----
MAX_TIMESTEP = 10268
MAX_FACES = 5

START_DATE = "2020-01-20"
HOURS_PER_TIMESTEP = 1  # cada timestep = 1 hora

# ----- Date -----

def get_date_by_timestep(timestep):
    """
    Convierte un timestep del experimento a una fecha completa con
    año, mes, día, hora, minuto y segundo.

    Args:
        timestep (int): índice de timestep (0, 1, 2, ...)

    Returns:
        str: Fecha y hora en formato 'AAAA-MM-DD HH:MM:SS'
    """
    base_date = datetime.strptime(START_DATE, "%Y-%m-%d")
    delta = timedelta(hours=timestep * HOURS_PER_TIMESTEP)
    target_date = base_date + delta
    return target_date.strftime("%Y-%m-%d %H:%M:%S")


# ----- Data -----

def get_data_by_timestep(variable, face, timestep, z):
    """
    Descarga un bloque 3D de datos climáticos para una variable, una face del cubed‑sphere y un rango vertical Z en una fecha específica.
    
    Args:
        variable (str): Variable climática a consultar (ej. 'u' (eastward wind), 'v' (northward wind)).
        face (str): región de la Tierra a consultar (Válido:'0', '1', '2', '3', '4', '5').
            GEOS utiliza una malla cubed‑sphere, donde la superficie terrestre se divide en 6 regiones llamadas faces. 
            Cada face corresponde a la proyección de una cara del cubo sobre la esfera. 
            GEOS sigue la convención estándar de NASA: 
                -Face 0: Pacífico central
                -Face 1: América y el Atlántico
                -Face 2: África‑Europa
                -Face 3: Asia
                -Face 4: Índico 
                -Face 5: la región polar
        date_str (str): Fecha objetivo en formato 'AAAA-MM-DD' (Válido: 1950-01-01 a 2011-12-31).
        z (list): Lista de índices de diferentes niveles de profundidad (z) a consultar en formato [inicio,fin] (Válido: [0, 51])(Ej: [3,4], [30,35], [45,51]).
                  A más grande el intervalo más tiempo de procesamiento.
    Returns:
        numpy.ndarray: Volumen 3D (latitud × longitud × depth (z)) con los datos climáticos solicitados.
    """    
    if timestep < 0 or timestep > MAX_TIMESTEP:
        print(f"\n[WARNING] Timestep {timestep} is out of bounds.")
        print(f"[WARNING] Valid range: 0 to {MAX_TIMESTEP}")
    if face < 0 or face > MAX_FACES:
        print(f"\n[WARNING] Face {face} is out of bounds.")
        print(f"[WARNING] Valid range: 0 to {MAX_FACES}")
    if not isinstance(z, (list, tuple)) or len(z) != 2:
        print("\n[WARNING] z must be a list of two integers: [start, end]")
    else:
        z_start, z_end = z

        if z_start < 0 or z_start > 51:
            print(f"\n[WARNING] z start {z_start} is out of bounds.")
            print("[WARNING] Valid range: 0 to 51")

        if z_end < 0 or z_end > 51:
            print(f"\n[WARNING] z end {z_end} is out of bounds.")
            print("[WARNING] Valid range: 0 to 51")

        if z_start >= z_end:
            print(f"\n[WARNING] Invalid z interval: [{z_start}, {z_end}]")
            print("[WARNING] z_inicio tiene que ser menor a z_final")

    geos_face_loc=f"https://nsdf-climate3-origin.nationalresearchplatform.org:50098/nasa/nsdf/climate3/dyamond/GEOS/GEOS_{variable.upper()}/{variable.lower()}_face_{face}_depth_52_time_0_10269.idx"
    db=ov.LoadDataset(geos_face_loc)
    data = db.read(time=timestep, quality=0, z=z)
    
    return data