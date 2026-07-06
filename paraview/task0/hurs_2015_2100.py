# trace generated using paraview version 6.1.1
#import paraview
#paraview.compatibility.major = 6
#paraview.compatibility.minor = 1

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'PVD Reader'
hurs_yearspvd = PVDReader(registrationName='hurs_years.pvd', FileName='E:\\U-TAD\\Curso_25_26\\MCRS\\VisDatos\\sciviscontest2026\\tasks\\task0\\hurs_years.pvd')
hurs_yearspvd.PointArrays = ['hurs']

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
hurs_yearspvdDisplay = Show(hurs_yearspvd, renderView1, 'UniformGridRepresentation')

# get color transfer function/color map for 'hurs'
hursLUT = GetColorTransferFunction('hurs')

# get opacity transfer function/opacity map for 'hurs'
hursPWF = GetOpacityTransferFunction('hurs')

# trace defaults for the display properties.
hurs_yearspvdDisplay.Set(
    Representation='Slice',
    ColorArrayName=['POINTS', 'hurs'],
    LookupTable=hursLUT,
    OSPRayScaleArray='hurs',
    ScaleFactor=35.975,
    SelectScaleArray='hurs',
    GlyphTableIndexArray='hurs',
    GaussianRadius=1.79875,
    SetScaleArray=['POINTS', 'hurs'],
    OpacityArray=['POINTS', 'hurs'],
    ScalarOpacityUnitDistance=4.09453468694336,
    ScalarOpacityFunction=hursPWF,
    OpacityArrayName=['POINTS', 'hurs'],
    ColorArray2Name=['POINTS', 'hurs'],
    IsosurfaceValues=[55.182942390441895],
    SelectInputVectors=[None, ''],
)

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
hurs_yearspvdDisplay.ScaleTransferFunction.Points = [8.924211502075195, 0.0, 0.5, 0.0, 101.4416732788086, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
hurs_yearspvdDisplay.OpacityTransferFunction.Points = [8.924211502075195, 0.0, 0.5, 0.0, 101.4416732788086, 1.0, 0.5, 0.0]

# init the 'Polar Axes Representation' selected for 'PolarAxes'
hurs_yearspvdDisplay.PolarAxes.MaximumRadius = 359.75

# init the 'Plane' selected for 'SliceFunction'
hurs_yearspvdDisplay.SliceFunction.Origin = [179.875, 74.875, 0.0]

# reset view to fit data
renderView1.ResetCamera(False, 0.9)

#changing interaction mode based on data extents
renderView1.Set(
    InteractionMode='2D',
    CameraPosition=[179.875, 74.875, 1205.1625000000001],
    CameraFocalPoint=[179.875, 74.875, 0.0],
)

# get the material library
materialLibrary1 = GetMaterialLibrary()

# show color bar/color legend
hurs_yearspvdDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get 2D transfer function for 'hurs'
hursTF2D = GetTransferFunction2D('hurs')

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
hursLUT.ApplyPreset('Linear Green (Gr4L)', True)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
hursLUT.ApplyPreset('Linear Green (Gr4L)', True)

# invert the transfer function
hursLUT.InvertTransferFunction()

# Properties modified on hursLUT
hursLUT.NanColor = [0.007843137718737125, 0.0, 0.18431372940540314]

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(registrationName='ExtractSurface1', Input=hurs_yearspvd)

# show data in view
extractSurface1Display = Show(extractSurface1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
extractSurface1Display.Set(
    Representation='Surface',
    ColorArrayName=['POINTS', 'hurs'],
    LookupTable=hursLUT,
    OSPRayScaleArray='hurs',
    ScaleFactor=35.975,
    SelectScaleArray='hurs',
    GlyphTableIndexArray='hurs',
    GaussianRadius=1.79875,
    SetScaleArray=['POINTS', 'hurs'],
    OpacityArray=['POINTS', 'hurs'],
    SelectInputVectors=[None, ''],
)

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
extractSurface1Display.ScaleTransferFunction.Points = [8.924211502075195, 0.0, 0.5, 0.0, 101.4416732788086, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
extractSurface1Display.OpacityTransferFunction.Points = [8.924211502075195, 0.0, 0.5, 0.0, 101.4416732788086, 1.0, 0.5, 0.0]

# init the 'Polar Axes Representation' selected for 'PolarAxes'
extractSurface1Display.PolarAxes.MaximumRadius = 359.75

# hide data in view
Hide(hurs_yearspvd, renderView1)

# show color bar/color legend
extractSurface1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=extractSurface1)
calculator1.Function = ''

# Properties modified on calculator1
calculator1.Set(
    CoordinateResults=1,
    ResultArrayName='SphericalProjection',
    Function='400 * ( cos((coordsY-74.875)/179.875*3.141592) * cos(coordsX/179.875*3.141592) * iHat + cos((coordsY-74.875)/179.875*3.141592) * sin(coordsX/179.875*3.141592) * jHat + sin((coordsY-74.875)/179.875*3.141592) * kHat )',
)

# show data in view
calculator1Display = Show(calculator1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
calculator1Display.Set(
    Representation='Surface',
    ColorArrayName=['POINTS', 'hurs'],
    LookupTable=hursLUT,
    OSPRayScaleArray='hurs',
    ScaleFactor=79.99976165849898,
    SelectScaleArray='hurs',
    GlyphTableIndexArray='hurs',
    GaussianRadius=3.9999880829249492,
    SetScaleArray=['POINTS', 'hurs'],
    OpacityArray=['POINTS', 'hurs'],
    SelectInputVectors=[None, ''],
)

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
calculator1Display.ScaleTransferFunction.Points = [8.924211502075195, 0.0, 0.5, 0.0, 101.4416732788086, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
calculator1Display.OpacityTransferFunction.Points = [8.924211502075195, 0.0, 0.5, 0.0, 101.4416732788086, 1.0, 0.5, 0.0]

# init the 'Polar Axes Representation' selected for 'PolarAxes'
calculator1Display.PolarAxes.MaximumRadius = 799.9976165849898

# hide data in view
Hide(extractSurface1, renderView1)

# show color bar/color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

#change interaction mode for render view
renderView1.InteractionMode = '3D'

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1595, 862)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.Set(
    CameraPosition=[2269.4150557116477, -216.15337170920697, 327.76588601058586],
    CameraFocalPoint=[179.87499999999997, 74.875, 1.2979281256868421e-14],
    CameraViewUp=[0.06273214426285074, 0.9105640600985692, 0.4085801886202934],
    CameraParallelScale=194.83655008750284,
)


##--------------------------------------------
## You may need to add some code at the end of this python script depending on your usage, eg:
#
## Render all views to see them appears
# RenderAllViews()
#
## Interact with the view, usefull when running from pvpython
# Interact()
#
## Save a screenshot of the active view
# SaveScreenshot("path/to/screenshot.png")
#
## Save a screenshot of a layout (multiple splitted view)
# SaveScreenshot("path/to/screenshot.png", GetLayout())
#
## Save all "Extractors" from the pipeline browser
# SaveExtracts()
#
## Save a animation of the current active view
# SaveAnimation()
#
## Please refer to the documentation of paraview.simple
## https://www.paraview.org/paraview-docs/nightly/python/
##--------------------------------------------