from scyjava import jimport, config

# Instructions for setting up python env and testing:
# [assumes conda is installed, and in root of git repo]
# 1) conda env create -f environment.yml
# 2) conda activate sciview
# 3) python scripts/python_basic.py

#print(os.environ['JAVA_HOME'])

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

dependencies = [
    'net.imagej:imagej:2.1.0', 'sc.fiji:bigdataviewer-core:10.1.1-SNAPSHOT'
] + sciview_deps

for dep in dependencies:
    config.add_endpoints(dep)

# Setup classes
HashMap = jimport('java.util.HashMap')
SciView = jimport('sc.iview.SciView')
ImageJ = jimport('net.imagej.ImageJ')

# Launch sciview
sv = SciView.create()
