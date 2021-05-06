# Utilities for the sciview_pyground

from scyjava import config


def setup_sciview_dependencies():
    # Setup maven repositories
    config.add_repositories({'jitpack': 'https://jitpack.io'})
    config.add_repositories(
        {'scijava.public': 'https://maven.scijava.org/content/groups/public'})

    # Import/load dependencies
    sciview_deps = [
        'sc.iview:sciview:f4dd286', 'graphics.scenery:scenery:937ba10',
        'org.jetbrains.kotlin:kotlin-stdlib-jdk8:1.4.20',
        'org.jetbrains.kotlinx:kotlinx-coroutines-core:1.3.9'
    ]

    n5_deps = ['org.janelia.saalfeldlab:n5-ij:2.0.1-SNAPSHOT']

    dependencies = [
        #        'net.imagej:imagej:2.1.0',
        'sc.fiji:bigdataviewer-vistools:1.0.0-beta-29-SNAPSHOT'
    ] + sciview_deps + n5_deps

    #    , 'sc.fiji:bigdataviewer-core:10.1.1-SNAPSHOT'

    for dep in dependencies:
        config.add_endpoints(dep)
