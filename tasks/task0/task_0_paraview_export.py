import task0_data as tk_0
import numpy as np
import vtk
from vtk.util import numpy_support

target_variable = "tas"
target_date = "1950-01-10"
spacing = 0.25

# 1. Obtener el ndarray 2D
data =  tk_0.get_data_by_date(target_variable, target_date)        # shape (600, 1440)

ny, nx = data.shape            # ny = 600, nx = 1440

# 2. Crear un vtkImageData con esas dimensiones
image = vtk.vtkImageData()
image.SetDimensions(nx, ny, 1) # (x, y, z)
image.SetOrigin(0.0, 0.0, 0.0) # opcional: coordenadas físicas
image.SetSpacing(spacing, spacing, spacing)# ajusta a tu resolución espacial

# 3. Convertir el ndarray a vtkDataArray
flat = data.reshape(nx * ny, 1)  # vector 1D de escalares
vtk_array = numpy_support.numpy_to_vtk(
    flat, deep=True
)
vtk_array.SetName("near surface air temperature")    # nombre del campo

# 4. Asignar los escalares al vtkImageData
image.GetPointData().SetScalars(vtk_array)

# 5. Escribir a disco como .vti (XML ImageData)
writer = vtk.vtkXMLImageDataWriter()
writer.SetFileName("campo.vti")
writer.SetInputData(image)
writer.Write()