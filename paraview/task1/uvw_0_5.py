# trace generated using paraview version 6.1.1
#import paraview
#paraview.compatibility.major = 6
#paraview.compatibility.minor = 1

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'PVD Reader'
a0_timepvd = PVDReader(registrationName='0_time.pvd', FileName='"C:\\Master\\VIDA\\Final\\sciviscontest2026\\tasks\\task1\\0_time.pvd"')
a0_timepvd.PointArrays = ['u', 'v', 'w']

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
a0_timepvdDisplay = Show(a0_timepvd, renderView1, 'StructuredGridRepresentation')

# trace defaults for the display properties.
a0_timepvdDisplay.Set(
    Representation='Outline',
    ColorArrayName=['POINTS', ''],
    OSPRayScaleArray='u',
    ScaleFactor=65.01832580566406,
    SelectScaleArray='u',
    GlyphTableIndexArray='u',
    GaussianRadius=3.2509162902832034,
    SetScaleArray=['POINTS', 'u'],
    OpacityArray=['POINTS', 'u'],
    ScalarOpacityUnitDistance=5.0024428965705,
    SelectInputVectors=[None, ''],
)

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
a0_timepvdDisplay.ScaleTransferFunction.Points = [-58.6045036315918, 0.0, 0.5, 0.0, 90.4375, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
a0_timepvdDisplay.OpacityTransferFunction.Points = [-58.6045036315918, 0.0, 0.5, 0.0, 90.4375, 1.0, 0.5, 0.0]

# init the 'Polar Axes Representation' selected for 'PolarAxes'
a0_timepvdDisplay.PolarAxes.MaximumRadius = 650.1832580566406

# reset view to fit data
renderView1.ResetCamera(False, 0.9)

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=a0_timepvd)
calculator1.Function = ''

# Properties modified on calculator1
calculator1.Function = '(u * iHat + v * jHat + w * kHat)'

# show data in view
calculator1Display = Show(calculator1, renderView1, 'StructuredGridRepresentation')

# trace defaults for the display properties.
calculator1Display.Set(
    Representation='Outline',
    ColorArrayName=['POINTS', ''],
    OSPRayScaleArray='u',
    SelectOrientationVectors='Result',
    ScaleFactor=65.01832580566406,
    SelectScaleArray='u',
    GlyphTableIndexArray='u',
    GaussianRadius=3.2509162902832034,
    SetScaleArray=['POINTS', 'u'],
    OpacityArray=['POINTS', 'u'],
    ScalarOpacityUnitDistance=5.0024428965705,
    SelectInputVectors=['POINTS', 'Result'],
)

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
calculator1Display.ScaleTransferFunction.Points = [-58.6045036315918, 0.0, 0.5, 0.0, 90.4375, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
calculator1Display.OpacityTransferFunction.Points = [-58.6045036315918, 0.0, 0.5, 0.0, 90.4375, 1.0, 0.5, 0.0]

# init the 'Polar Axes Representation' selected for 'PolarAxes'
calculator1Display.PolarAxes.MaximumRadius = 650.1832580566406

# hide data in view
Hide(a0_timepvd, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Glyph'
glyph1 = Glyph(registrationName='Glyph1', Input=calculator1,
    GlyphType='Arrow')
glyph1.Set(
    OrientationArray=['POINTS', 'Result'],
    ScaleArray=['POINTS', 'u'],
    ScaleFactor=65.01832580566406,
)

# Properties modified on glyph1
glyph1.Set(
    ScaleArray=['POINTS', 'Result'],
    ScaleFactor=0.7189310386251728,
)

# show data in view
glyph1Display = Show(glyph1, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'u'
uLUT = GetColorTransferFunction('u')

# trace defaults for the display properties.
glyph1Display.Set(
    Representation='Surface',
    ColorArrayName=['POINTS', 'u'],
    LookupTable=uLUT,
    OSPRayScaleArray='u',
    SelectOrientationVectors='Result',
    ScaleFactor=65.63521118164063,
    SelectScaleArray='u',
    GlyphTableIndexArray='u',
    GaussianRadius=3.281760559082031,
    SetScaleArray=['POINTS', 'u'],
    OpacityArray=['POINTS', 'u'],
    SelectInputVectors=['POINTS', 'Result'],
)

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
glyph1Display.ScaleTransferFunction.Points = [-56.3857536315918, 0.0, 0.5, 0.0, 89.11425018310547, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
glyph1Display.OpacityTransferFunction.Points = [-56.3857536315918, 0.0, 0.5, 0.0, 89.11425018310547, 1.0, 0.5, 0.0]

# init the 'Polar Axes Representation' selected for 'PolarAxes'
glyph1Display.PolarAxes.MaximumRadius = 656.3521118164062

# show color bar/color legend
glyph1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get opacity transfer function/opacity map for 'u'
uPWF = GetOpacityTransferFunction('u')

# get 2D transfer function for 'u'
uTF2D = GetTransferFunction2D('u')

# set active source
SetActiveSource(calculator1)

# set active source
SetActiveSource(glyph1)

# ---------------------------------------------------------------
# FIX: color map SEPARADO para este glyph (separate=True), para
# que no comparta rango de colores con los demÃ¡s glyphs (glyph2,
# glyph3, glyph4), que tienen otro rango de valores de 'Result'.
# ---------------------------------------------------------------
ColorBy(glyph1Display, ('POINTS', 'Result', 'Magnitude'), separate=True)

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(uLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
glyph1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
glyph1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Result' PROPIO de glyph1
resultLUT1 = GetColorTransferFunction('Result', glyph1Display, separate=True)

# get opacity transfer function/opacity map for 'Result' PROPIO de glyph1
resultPWF1 = GetOpacityTransferFunction('Result', glyph1Display, separate=True)

# Apply a preset using its name.
resultLUT1.ApplyPreset('Rainbow Desaturated', True)

# hide data in view
Hide(calculator1, renderView1)

# create a new 'PVD Reader'
a1_timepvd = PVDReader(registrationName='1_time.pvd', FileName='C:\\Master\\VIDA\\Final\\sciviscontest2026\\task1\\1_time.pvd')
a1_timepvd.PointArrays = ['u', 'v', 'w']

# set active source
SetActiveSource(calculator1)

# set active source
SetActiveSource(glyph1)

# set active source
SetActiveSource(a1_timepvd)

# show data in view
a1_timepvdDisplay = Show(a1_timepvd, renderView1, 'StructuredGridRepresentation')

# trace defaults for the display properties.
a1_timepvdDisplay.Set(
    Representation='Outline',
    ColorArrayName=['POINTS', ''],
    OSPRayScaleArray='u',
    ScaleFactor=65.01832580566406,
    SelectScaleArray='u',
    GlyphTableIndexArray='u',
    GaussianRadius=3.2509162902832034,
    SetScaleArray=['POINTS', 'u'],
    OpacityArray=['POINTS', 'u'],
    ScalarOpacityUnitDistance=5.0024428965705,
    SelectInputVectors=[None, ''],
)

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
a1_timepvdDisplay.ScaleTransferFunction.Points = [-59.015625, 0.0, 0.5, 0.0, 52.78125, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
a1_timepvdDisplay.OpacityTransferFunction.Points = [-59.015625, 0.0, 0.5, 0.0, 52.78125, 1.0, 0.5, 0.0]

# init the 'Polar Axes Representation' selected for 'PolarAxes'
a1_timepvdDisplay.PolarAxes.MaximumRadius = 650.1832580566406

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Calculator'
calculator2 = Calculator(registrationName='Calculator2', Input=a1_timepvd)
calculator2.Function = '(u*iHat + v*jHat + w*kHat)'

# hide data in view
Hide(a1_timepvd, renderView1)

# create a new 'Glyph'
glyph2 = Glyph(registrationName='Glyph2', Input=calculator2,
    GlyphType='Arrow')
glyph2.Set(
    OrientationArray=['POINTS','Result'],
    ScaleArray=['POINTS','Result'],
    ScaleFactor=0.7189310386251728,
)

# show data in view
glyph2Display = Show(glyph2, renderView1, 'GeometryRepresentation')

# hide data in view
Hide(calculator2, renderView1)

# set active source
SetActiveSource(glyph1)

# set active source
SetActiveSource(glyph2)

# ---------------------------------------------------------------
# FIX: color map SEPARADO para glyph2
# ---------------------------------------------------------------
ColorBy(glyph2Display, ('POINTS', 'Result', 'Magnitude'), separate=True)

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(uLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
glyph2Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
glyph2Display.SetScalarBarVisibility(renderView1, False)

# get color transfer function/color map for 'Result' PROPIO de glyph2
resultLUT2 = GetColorTransferFunction('Result', glyph2Display, separate=True)
resultPWF2 = GetOpacityTransferFunction('Result', glyph2Display, separate=True)

# Apply a preset using its name.
resultLUT2.ApplyPreset('Rainbow Desaturated', True)

# create a new 'PVD Reader'
a2_timepvd = PVDReader(registrationName='2_time.pvd', FileName='C:\\Master\\VIDA\\Final\\sciviscontest2026\\task1\\2_time.pvd')
a2_timepvd.PointArrays = ['u', 'v', 'w']

# show data in view
a2_timepvdDisplay = Show(a2_timepvd, renderView1, 'StructuredGridRepresentation')

# trace defaults for the display properties.
a2_timepvdDisplay.Set(
    Representation='Outline',
    ColorArrayName=['POINTS', ''],
    OSPRayScaleArray='u',
    ScaleFactor=65.01832580566406,
    SelectScaleArray='u',
    GlyphTableIndexArray='u',
    GaussianRadius=3.2509162902832034,
    SetScaleArray=['POINTS', 'u'],
    OpacityArray=['POINTS', 'u'],
    ScalarOpacityUnitDistance=5.0024428965705,
    SelectInputVectors=[None, ''],
)

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
a2_timepvdDisplay.ScaleTransferFunction.Points = [-92.84375, 0.0, 0.5, 0.0, 108.40225219726562, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
a2_timepvdDisplay.OpacityTransferFunction.Points = [-92.84375, 0.0, 0.5, 0.0, 108.40225219726562, 1.0, 0.5, 0.0]

# init the 'Polar Axes Representation' selected for 'PolarAxes'
a2_timepvdDisplay.PolarAxes.MaximumRadius = 650.1832580566406

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Calculator'
calculator3 = Calculator(registrationName='Calculator3', Input=a2_timepvd)
calculator3.Function = '(u*iHat + v*jHat + w*kHat)'

# hide data in view
Hide(a2_timepvd, renderView1)

# create a new 'Glyph'
glyph3 = Glyph(registrationName='Glyph3', Input=calculator3,
    GlyphType='Arrow')
glyph3.Set(
    OrientationArray=['POINTS','Result'],
    ScaleArray=['POINTS','Result'],
    ScaleFactor=0.7189310386251728,
)

# show data in view
glyph3Display = Show(glyph3, renderView1, 'GeometryRepresentation')

# hide data in view
Hide(calculator3, renderView1)

# ---------------------------------------------------------------
# FIX: color map SEPARADO para glyph3
# ---------------------------------------------------------------
ColorBy(glyph3Display, ('POINTS', 'Result', 'Magnitude'), separate=True)

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(uLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
glyph3Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
glyph3Display.SetScalarBarVisibility(renderView1, False)

# get color transfer function/color map for 'Result' PROPIO de glyph3
resultLUT3 = GetColorTransferFunction('Result', glyph3Display, separate=True)
resultPWF3 = GetOpacityTransferFunction('Result', glyph3Display, separate=True)

# Apply a preset using its name.
resultLUT3.ApplyPreset('Rainbow Desaturated', True)

# create a new 'PVD Reader'
a3_timepvd = PVDReader(registrationName='3_time.pvd', FileName='C:\\Master\\VIDA\\Final\\sciviscontest2026\\task1\\3_time.pvd')
a3_timepvd.PointArrays = ['u', 'v', 'w']

# show data in view
a3_timepvdDisplay = Show(a3_timepvd, renderView1, 'StructuredGridRepresentation')

# trace defaults for the display properties.
a3_timepvdDisplay.Set(
    Representation='Outline',
    ColorArrayName=['POINTS', ''],
    OSPRayScaleArray='u',
    ScaleFactor=65.01832580566406,
    SelectScaleArray='u',
    GlyphTableIndexArray='u',
    GaussianRadius=3.2509162902832034,
    SetScaleArray=['POINTS', 'u'],
    OpacityArray=['POINTS', 'u'],
    ScalarOpacityUnitDistance=5.0024428965705,
    SelectInputVectors=[None, ''],
)

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
a3_timepvdDisplay.ScaleTransferFunction.Points = [-50.68760681152344, 0.0, 0.5, 0.0, 23.367185592651367, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
a3_timepvdDisplay.OpacityTransferFunction.Points = [-50.68760681152344, 0.0, 0.5, 0.0, 23.367185592651367, 1.0, 0.5, 0.0]

# init the 'Polar Axes Representation' selected for 'PolarAxes'
a3_timepvdDisplay.PolarAxes.MaximumRadius = 650.1832580566406

# update the view to ensure updated data information
renderView1.Update()

# hide data in view
Hide(a3_timepvd, renderView1)

# create a new 'Calculator'
calculator4 = Calculator(registrationName='Calculator4', Input=a3_timepvd)
calculator4.Function = '(u*iHat + v*jHat + w*kHat)'

# hide data in view
Hide(a3_timepvd, renderView1)

# create a new 'Glyph'
glyph4 = Glyph(registrationName='Glyph4', Input=calculator4,
    GlyphType='Arrow')
glyph4.Set(
    OrientationArray=['POINTS','Result'],
    ScaleArray=['POINTS','Result'],
    ScaleFactor=0.7189310386251728,
)

# show data in view
glyph4Display = Show(glyph4, renderView1, 'GeometryRepresentation')

# hide data in view
Hide(calculator4, renderView1)

# ---------------------------------------------------------------
# FIX: color map SEPARADO para glyph4
# ---------------------------------------------------------------
ColorBy(glyph4Display, ('POINTS', 'Result', 'Magnitude'), separate=True)

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(uLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
glyph4Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
glyph4Display.SetScalarBarVisibility(renderView1, False)

# get color transfer function/color map for 'Result' PROPIO de glyph4
resultLUT4 = GetColorTransferFunction('Result', glyph4Display, separate=True)
resultPWF4 = GetOpacityTransferFunction('Result', glyph4Display, separate=True)

# Apply a preset using its name.
resultLUT4.ApplyPreset('Rainbow Desaturated', True)

# set active source
SetActiveSource(a3_timepvd)

# create a new 'PVD Reader'
hurs_yearspvd = PVDReader(registrationName='hurs_years.pvd', FileName='C:\Master\\VIDA\\Final\\sciviscontest2026\\task0\\hurs_years.pvd')
hurs_yearspvd.PointArrays = ['hurs']

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

# show color bar/color legend
hurs_yearspvdDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get 2D transfer function for 'hurs'
hursTF2D = GetTransferFunction2D('hurs')

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
calculator5 = Calculator(registrationName='Calculator5', Input=extractSurface1)
calculator5.Function = ''

# Properties modified on calculator5
calculator5.Set(
    CoordinateResults=1,
    Function='380 * ( cos((coordsY-74.875)/179.875*3.141592) * cos(coordsX/179.875*3.141592) * iHat + cos((coordsY-74.875)/179.875*3.141592) * sin(coordsX/179.875*3.141592) * jHat + sin((coordsY-74.875)/179.875*3.141592) * kHat )',
)

# show data in view
calculator5Display = Show(calculator5, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
calculator5Display.Set(
    Representation='Surface',
    ColorArrayName=['POINTS', 'hurs'],
    LookupTable=hursLUT,
    OSPRayScaleArray='hurs',
    ScaleFactor=75.99977357557405,
    SelectScaleArray='hurs',
    GlyphTableIndexArray='hurs',
    GaussianRadius=3.7999886787787025,
    SetScaleArray=['POINTS', 'hurs'],
    OpacityArray=['POINTS', 'hurs'],
    SelectInputVectors=[None, ''],
)

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
calculator5Display.ScaleTransferFunction.Points = [8.924211502075195, 0.0, 0.5, 0.0, 101.4416732788086, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
calculator5Display.OpacityTransferFunction.Points = [8.924211502075195, 0.0, 0.5, 0.0, 101.4416732788086, 1.0, 0.5, 0.0]

# init the 'Polar Axes Representation' selected for 'PolarAxes'
calculator5Display.PolarAxes.MaximumRadius = 759.9977357557405

# hide data in view
Hide(extractSurface1, renderView1)

# show color bar/color legend
calculator5Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
hursLUT.ApplyPreset('Linear Green (Gr4L)', True)

# Properties modified on hursLUT
hursLUT.NanColor = [0.007843137718737125, 0.0, 0.18431372940540314]

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1032, 502)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.Set(
    CameraPosition=[-148.69854373006683, 2279.3060312603234, 109.06590898779504],
    CameraFocalPoint=[-73.59222161451159, 132.04163382015454, 43.1086312906553],
    CameraViewUp=[0.008496113285886179, -0.030404402394944723, 0.9995015699707729],
    CameraParallelScale=459.7973088095621,
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


# import ptc
# web_app = ptc.Viewer(from_state=True)
# web_app.start(open_browser=False)