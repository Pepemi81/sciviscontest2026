import task1_data as tk_1
import numpy as np
import vtk
from vtk.util import numpy_support

from tasks.task0.task0_data import get_date_by_timestep


## VARIABLES ##

max_faces = 6
max_timesteps = 5
max_depths = 4

N = 1440           # Numero de celdas por lado del array de datos
DELTA = 90.0 / N   # 0.0625 grados por celda
R_BASE = 400.0     # radio base de la esfera en unidades de ParaView

# Centros aproximados de cada cara
FACE_CENTER = {
    0: (  0.0, -135.0),  # Pacífico central
    1: (  0.0,  -45.0),  # América + Atlántico
    2: (  0.0,   45.0),  # África‑Europa
    3: (  0.0,  135.0),  # Asia
    4: ( 45.0,    0.0),  # Índico / norte
    5: (-45.0,    0.0),  # hemisferio sur
}


## TRATAMIENTO DE DATOS ##

# Obtener los arrays u, v y w dada una cara especifica
def make_vti_u_v_w(face, timestep, z_range, filename, heightDiff = 20.0):

    ## OBTENER DATOS ##

    # Obtener los datos de las tres componentes vectoriales
    u = tk_1.get_data_by_timestep("u", face, timestep, z_range)  # shape (nx, ny, nz)
    v = tk_1.get_data_by_timestep("v", face, timestep, z_range)
    w = tk_1.get_data_by_timestep("w", face, timestep, z_range)

    nz, ny, nx = u.shape    # Al reves porque get_data_by_timestep devuelve una matriz 1 x 1440 x 1440


    ## TRANSFORMAR A PUNTOS ESFERICOS ##

    # Obtener el conjunto de latitudes y longitudes de la cara
    lat_deg, lon_deg = get_latlon_for_face(face)

    # Crear el array de puntos sobre el que aplicar las transformaciones para obtener los puntos finales
    points = vtk.vtkPoints()
    points.SetNumberOfPoints(nx * ny * nz)

    # Obtener la posición de cada punto teniendo en cuenta su altura
    idx = 0

    for k in range(nz):     # Por cada una de las alturas sobre la cara
        # Calcular el radio final del punto y obtener sus coordenadas x y z radiales
        radius = R_BASE + k * heightDiff
        x, y, z = latlon_to_xyz(lat_deg, lon_deg, radius)

        # Aplanar el array de puntos a unidimensional y añadir info de coordenadas de los puntos
        for val_x, val_y, val_z in zip(x.ravel(order="C"), y.ravel(order="C"), z.ravel(order="C")):
            points.SetPoint(idx, val_x, val_y, val_z)
            idx += 1


    ## GUARDAR EN MEMORIA ##

    # Crear los arrays de escalares de de VTK
    vtk_u = to_vtk_scalars(u, "u")
    vtk_v = to_vtk_scalars(v, "v")
    vtk_w = to_vtk_scalars(w, "w")

    # Crear una malla VTK con los puntos esfericos calculados
    grid = vtk.vtkStructuredGrid()
    grid.SetDimensions(nx, ny, nz)
    grid.SetPoints(points)      # Añadir los puntos ya transformados a la malla

    # Añadir la información del viento a los puntos esfericos
    pd = grid.GetPointData()
    pd.SetScalars(vtk_u)
    pd.AddArray(vtk_v)
    pd.AddArray(vtk_w)

    # Escribir a disco
    writer = vtk.vtkXMLStructuredGridWriter()
    writer.SetFileName(filename)
    writer.SetInputData(grid)
    writer.Write()


## AUTOMATIZACION DE DATOS FINALES ##

# Obtener archivos por cada cara y timestep
for face in range(0,max_faces):
    print(f"face: {face}")

    files = []  # Lista de todos los archivos de una cara por timestep
    for timeStep in range(0, max_timesteps):
        print(timeStep)
        date_str = f"{tk_1.get_date_by_timestep(timeStep)}"
        fileName = f"./vtss/{face}_{timeStep:05d}.vts"
        make_vti_u_v_w(face, timeStep, z_range = [0, max_depths], filename = fileName)
        files.append((timeStep, fileName))

    with open(f"{face}_time.pvd", "w", encoding="utf-8") as f:
        f.write('<VTKFile type="Collection" version="0.1" byte_order="LittleEndian">\n')
        f.write('  <Collection>\n')
        for (timeStep, fileName) in files:
            f.write(f'    <DataSet timestep="{timeStep}" group="" part="0" file="{fileName}"/>\n')
        f.write('  </Collection>\n')
        f.write('</VTKFile>\n')


## FUNCIONES AUXILIARES ##

# Parsear un array a un array de VTK
def to_vtk_scalars(arr, name):
    flat = arr.ravel(order="C")
    vtk_arr = numpy_support.numpy_to_vtk(
        num_array = flat,
        deep = True,
        array_type = vtk.VTK_FLOAT
    )
    vtk_arr.SetName(name)
    return vtk_arr

# Obtener las longitudes y latitudes de cada celda de una cara (posibles latitudes -> lat_deg ; posibles longitudes -> lon_deg)
def get_latlon_for_face(face):
    lat0, lon0 = FACE_CENTER[face]
    lat_min = lat0 - 45.0
    lon_min = lon0 - 45.0

    # i: eje X (lons), j: eje Y (lats)
    i, j = np.meshgrid(np.arange(N),np.arange(N))

    lat_deg = lat_min + j * DELTA
    lon_deg = lon_min + i * DELTA
    return lat_deg, lon_deg

def latlon_to_xyz(lat_deg, lon_deg, radius):
    lat = np.deg2rad(lat_deg)
    lon = np.deg2rad(lon_deg)

    x = radius * np.cos(lat) * np.cos(lon)
    y = radius * np.cos(lat) * np.sin(lon)
    z = radius * np.sin(lat)

    return x, y, z