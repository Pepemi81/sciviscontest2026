import OpenVisus as ov
from datetime import datetime, timedelta

# ----- Config -----

MIN_DATE = "1950-01-01"
MAX_DATE = "2011-12-31"

# Dias totales reales entre 1950-01-01 y 2011-12-31
MAX_TIMESTEP = 22644

# ----- Time -----

def get_timestep(date_str):
    """
    Calcula el índice específico del servidor OpenVisus para una fecha dada.
    
    Args:
        date_str (str): Fecha objetivo en formato 'AAAA-MM-DD'.
        
    Returns:
        int: El índice absoluto de timestep requerido por la base de datos de OpenVisus.
    """
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    start_of_year = datetime(date_obj.year, 1, 1)
    
    day_of_year = (date_obj - start_of_year).days
    
    is_leap_year = False
    if date_obj.year % 4 == 0:
        if date_obj.year % 100 != 0 or date_obj.year % 400 == 0:
            is_leap_year = True
            
    if is_leap_year == True:
        total_days_in_year = 366
    else:
        total_days_in_year = 365
        
    timestep_index = (date_obj.year * total_days_in_year) + day_of_year
    
    return int(timestep_index)

def get_date_by_timestep(timestep):
    """
    Convierte un timestep lineal normalizado de vuelta a una cadena de fecha estándar.
    
    Args:
        timestep (int): Paso lineal de 0 a 22644 (días desde 1950-01-01).
        
    Returns:
        str: La fecha calculada en formato 'AAAA-MM-DD'.
    """
    base_date = datetime.strptime(MIN_DATE, "%Y-%m-%d")
    target_date = base_date + timedelta(days=int(timestep))
    return target_date.strftime("%Y-%m-%d")

# ----- Data -----

def get_data_by_date(variable, face, date_str, z):
    """
    Descarga una matriz 2D de datos climáticos desde el servidor usando una fecha específica.
    
    Args:
        variable (str): Variable climática a consultar (ej. 'U' (eastward wind), 'V' (northward wind)).
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
        z (list): Lista de índices de diferentes niveles de profundidad (z) a consultar en formato [inicio,fin] (Válido: [0,51]).
        
    Returns:
        numpy.ndarray: La matriz 2D que contiene los datos climáticos solicitados.
    """    
    geos_face_loc=f"https://nsdf-climate3-origin.nationalresearchplatform.org:50098/nasa/nsdf/climate3/dyamond/GEOS/GEOS_{variable.upper()}/{variable.lower()}_face_{face}_depth_52_time_0_10269.idx"
    db=ov.LoadDataset(geos_face_loc)
    timestep = get_timestep(date_str)
    data = db.read(time=timestep, quality=0, z=z)
    
    return data

def get_data_by_timestep(variable, timestep):
    """
    Descarga una matriz 2D de datos climáticos usando un índice de timestep lineal.
    Ideal para controles deslizantes (sliders) de interfaz de usuario o bucles de iteración.
    
    Args:
        variable (str): Variable climática a consultar (ej. 'tas', 'pr').
        timestep (int): Índice lineal entre 0 y 22644.
        
    Returns:
        numpy.ndarray: La matriz 2D que contiene los datos climáticos solicitados.
    """
    if timestep < 0 or timestep > MAX_TIMESTEP:
        print(f"\n[WARNING] Timestep {timestep} is out of bounds.")
        print(f"[WARNING] Valid range: 0 to {MAX_TIMESTEP}")
        
    date = get_date_by_timestep(timestep)
    data = get_data_by_date(variable, date)
    
    return data