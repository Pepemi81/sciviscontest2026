import OpenVisus as ov
from datetime import datetime, timedelta

# ----- Config -----

main_url = "https://atlantis.sci.utah.edu/mod_visus?dataset=nex-gddp-cmip6"
backup_url = "https://us-east-1.gw.future-tech-holdings.com/nasa-t0/nex-gddp-cmip6/nex-gddp-cmip6.idx"

model = "ACCESS-CM2"
scenario = "historical"

MIN_DATE = "1950-01-01"
MAX_DATE = "2011-12-31"

# Dias totales reales entre 1950-01-01 y 2011-12-31
MAX_TIMESTEP = 22644 

try:
    db = ov.LoadDataset(main_url)
except Exception:
    db = ov.LoadDataset(backup_url)

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

def get_data_by_date(variable, date_str):
    """
    Descarga una matriz 2D de datos climáticos desde el servidor usando una fecha específica.
    
    Args:
        variable (str): Variable climática a consultar (ej. 'tas' para temperatura, 'pr' para precipitación).
        date_str (str): Fecha objetivo en formato 'AAAA-MM-DD' (Válido: 1950-01-01 a 2011-12-31).
        
    Returns:
        numpy.ndarray: La matriz 2D que contiene los datos climáticos solicitados.
    """     
    timestep = get_timestep(date_str)
    field_name = f"{variable}_day_{model}_{scenario}_r1i1p1f1_gn"
    data = db.read(time=timestep, quality=0, field=field_name)
    
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