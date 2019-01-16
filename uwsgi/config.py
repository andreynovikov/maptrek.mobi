DB_CONNECTION_DSN = 'postgresql:///maptrek'
DB_GIS_CONNECTION_DSN = 'postgresql:///gis'

try:
    from local_config import *
except ImportError:
    # no local config found
    pass
