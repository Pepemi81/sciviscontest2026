import task0_data as tk_0
import numpy as np
import vtk
from vtk.util import numpy_support

target_variable = "tas"
target_date = "1950-01-10"
ssp = "ssp126"
spacing = 0.25


# 1. Obtener el ndarray 2D


def write_vti_from_array(data, filename, spacing=(spacing, spacing, spacing)):
    ny, nx = data.shape  # (600, 1440)
    image = vtk.vtkImageData()
    image.SetDimensions(nx, ny, 1)
    image.SetOrigin(0.0, 0.0, 0.0)
    image.SetSpacing(*spacing)

    flat = data.reshape(nx * ny, 1)
    vtk_array = numpy_support.numpy_to_vtk(flat, deep=True)
    vtk_array.SetName("tas")  # nombre del campo, ajusta según variable

    image.GetPointData().SetScalars(vtk_array)

    writer = vtk.vtkXMLImageDataWriter()
    writer.SetFileName(filename)
    writer.SetInputData(image)
    writer.Write()

# ejemplo: un campo por año usando el 1 de julio
for year in range(2097, 2100):
    date_str = f"{year}-08-01"
    data =  tk_0.get_data_by_date(target_variable, date_str, ssp)        # shape (600, 1440)
    filename = f"./vtis/{target_variable}_{year}.vti"
    write_vti_from_array(data, filename)

years = list(range(2097, 2100))

with open(f"{target_variable}_years.pvd", "w", encoding="utf-8") as f:
    f.write('<VTKFile type="Collection" version="0.1" byte_order="LittleEndian">\n')
    f.write('  <Collection>\n')
    for year in years:
        fname = f"./vtis/{target_variable}_{year}.vti"
        # timestep puede ser el año, o un float (1950.0, 1951.0, ...)
        f.write(f'    <DataSet timestep="{year}" group="" part="0" file="{fname}"/>\n')
    f.write('  </Collection>\n')
    f.write('</VTKFile>\n')