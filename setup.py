from distutils.core import setup

meta = dict(
    name          = "clusterui",
    version       = "0.1",
    license       = "MIT",
    description   = "Run interactive/UI jobs in a Condor cluster",
    author        = "Will Maier",
    author_email  = "wcmaier@hep.wisc.edu",
    url           = "http://hg.hep.wisc.edu/cmsops/clusterui",
    scripts       = ["cui"],
)

setup(**meta)
