# By Kyle Harrington (2021), mdc@kyleharrington.com

from jpype import JObject, JException
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
N5FSWriter = jimport('org.janelia.saalfeldlab.n5.N5FSWriter')
GzipCompression = jimport('org.janelia.saalfeldlab.n5.GzipCompression')
N5FSReader = jimport('org.janelia.saalfeldlab.n5.N5FSReader')

#filename = "https://open.quiltdata.com/b/janelia-cosem/tree/jrc_macrophage-2/"
remote_filename = "s3://janelia-cosem/jrc_macrophage-2/"
remote_n5 = N5Importer().N5ViewerReaderFun().apply(to_java(remote_filename))
local_filename = "/mnt/data/COSEM/jrc_macrophage-2/"
scale = 's3'

em_dataset = 'jrc_macrophage-2.n5/em/fibsem-uint16/%s' % scale
labels_dataset = 'jrc_macrophage-2.n5/labels/er_pred/%s' % scale

em = N5Utils.open(remote_n5, em_dataset)
em_rai = JObject(em, RandomAccessibleInterval)

block_size = [96, 96, 96]
local_n5 = N5FSWriter(local_filename)


def cache_n5(rai, local_n5, dataset):
    if (not local_n5.exists(dataset)):
        print('Caching %s' % dataset)
        N5Utils.save(rai, local_n5, dataset, block_size, GzipCompression())
        print('Done caching')
    else:
        print('Already cached')


cache_n5(em_rai, local_n5, em_dataset)
local_n5 = N5FSReader(local_filename)

em = N5Utils.open(local_n5, em_dataset)
em_rai = JObject(em, RandomAccessibleInterval)

#BdvFunctions.show(em_rai, 'em')

# Launch sciview
sv = SciView.create()

# Note that currently the voxel resolution is required or an index OOB exception will be thrown
#resolution = [4.0, 4.0, 3.36]
resolution = [el * 2**4 for el in [4.0, 4.0, 3.36]]
sv.addVolume(em_rai, "em", resolution)
