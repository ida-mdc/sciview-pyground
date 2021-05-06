from scyjava import jimport
from sciview_pyground import setup_sciview_dependencies

setup_sciview_dependencies()

# Setup classes
HashMap = jimport('java.util.HashMap')
SciView = jimport('sc.iview.SciView')
ImageJ = jimport('net.imagej.ImageJ')

# Launch sciview
sv = SciView.create()

# Add a sphere to the scene
sv.addSphere()
