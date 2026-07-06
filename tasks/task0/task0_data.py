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


def select_ssp(date_str, ssp):
    """
    Selecciona el escenario "historical" si la fecha es menor al 2012, en caso contrario selecciona el escenario especificado.
    
    Args:
        date_str (str): Fecha objetivo en formato 'AAAA-MM-DD'.
        ssp (str): Escenario climático seleccionado.
        
    Returns:
        str: 'historical' si la fecha es igual o anterior al 31 de diciembre de 2011, 
             de lo contrario devuelve el escenario 'ssp' especificado.

    """

    target_date = datetime.strptime(date_str, '%Y-%m-%d')
    limit_date = datetime(2011, 12, 31)
    
    if target_date <= limit_date:
        return "historical"
    else:
        return ssp


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
            
    timestep_index = (date_obj.year * 365) + day_of_year
    
    return int(timestep_index)


def get_date_by_timestep(timestep):
    """
    Convierte un timestep absoluto de OpenVisus a una fecha estándar.
    
    Args:
        timestep (int): El índice absoluto de la base de datos de OpenVisus.
        
    Returns:
        str: La fecha calculada en formato 'AAAA-MM-DD'.
    """    
    
    for year in range(1950, 2101):
        day_of_year = timestep - (year * 365)
        
        if 0 <= day_of_year < 365:
            start_of_year = datetime(year, 1, 1)
            target_date = start_of_year + timedelta(days=365)
            return target_date.strftime('%Y-%m-%d')
            
    return "fuera de rango"

# ----- Data -----

def get_data_by_date(variable, date_str, ssp):
    """
    Descarga una matriz 2D de datos climáticos desde el servidor usando una fecha específica.
    
    Args:
        variable (str): Variable climática a consultar (ej. 'tas' para temperatura, 'pr' para precipitación).
        date_str (str): Fecha objetivo en formato 'AAAA-MM-DD' (Válido: 1950-01-01 a 2011-12-31).
        ssp (str): Escenario seleccionado.
            * historical
            * ssp126
            * ssp245
            * ssp370
            * ssp585
        
    Returns:
        numpy.ndarray: La matriz 2D que contiene los datos climáticos solicitados.
    """     

    scenario = select_ssp(date_str, ssp)
    timestep = get_timestep(date_str)
    print(timestep)
    field_name = f"{variable}_day_{model}_{scenario}_r1i1p1f1_gn"
    data = db.read(time=timestep, quality=0, field=field_name)
    
    return data

def get_data_by_timestep(variable, timestep, ssp):
    """
    Descarga una matriz 2D de datos climáticos usando un índice de timestep lineal.
    Ideal para controles deslizantes (sliders) de interfaz de usuario o bucles de iteración.
    
    Args:
        variable (str): Variable climática a consultar (ej. 'tas', 'pr').
        timestep (int): Índice lineal entre 0 y 22644.
        ssp (str): Escenario seleccionado.
            * historical
            * ssp126
            * ssp245
            * ssp370
            * ssp585
        
    Returns:
        numpy.ndarray: La matriz 2D que contiene los datos climáticos solicitados.
    """
        
    date = get_date_by_timestep(timestep)
    print(date)
    scenario = select_ssp(date, ssp)
    field_name = f"{variable}_day_{model}_{scenario}_r1i1p1f1_gn"
    data = db.read(time=timestep, quality=0, field=field_name)
    
    return data