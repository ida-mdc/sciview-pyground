# By Kyle Harrington (2021), mdc@kyleharrington.com

from jpype import JObject
from scyjava import jimport, to_java
from sciview_pyground import setup_sciview_dependencies

setup_sciview_dependencies()

# Setup classes
HashMap = jimport('java.util.HashMap')
SciView = jimport('sc.iview.SciView')
ImageJ = jimport('net.imagej.ImageJ')
N5Importer = jimport('org.janelia.saalfeldlab.n5.ij.N5Importer')
N5Utils = jimport('org.janelia.saalfeldlab.n5.imglib2.N5Utils')
BdvFunctions = jimport('bdv.util.BdvFunctions')
RandomAccessibleInterval = jimport('net.imglib2.RandomAccessibleInterval')

#filename = "https://open.quiltdata.com/b/janelia-cosem/tree/jrc_macrophage-2/"
filename = "s3://janelia-cosem/jrc_macrophage-2/"
n5 = N5Importer().N5ViewerReaderFun().apply(to_java(filename))

em_dataset = 'jrc_macrophage-2.n5/em/fibsem-uint16/s5'
labels_dataset = 'jrc_macrophage-2.n5/labels/er_pred/s5'

em = N5Utils.open(n5, em_dataset)
em_rai = JObject(em, RandomAccessibleInterval)
BdvFunctions.show(em_rai, 'em')

# Launch sciview
#sv = SciView.create()
