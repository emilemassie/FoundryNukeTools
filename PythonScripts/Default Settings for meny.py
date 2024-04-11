import nuke

# set default copy node setting to A BBox 
nuke.knobDefault('Copy.bbox', "A")

# set default motion blur to be centered on most nodes
nuke.knobDefault('Tracker4.shutteroffset', "centered")
nuke.knobDefault('TimeBlur.shutteroffset', "centered")
nuke.knobDefault('Transform.shutteroffset', "centered")
nuke.knobDefault('CornerPin2D.shutteroffset', "centered")
nuke.knobDefault('MotionBlur2D.shutteroffset', "centered")
nuke.knobDefault('MotionBlur3D.shutteroffset', "centered")

# Set default roto to b-spline
nuke.knobDefault('Roto.toolbox','createBSpline')
# Set default paint node settings
nuke.knobDefault('RotoPaint.toolbox','createBSpline')
nuke.knobDefault('RotoPaint.toolbox','smear')