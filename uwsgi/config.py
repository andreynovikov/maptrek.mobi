DB_CONNECTION_DSN = 'postgresql:///maptrek'  # set correct DSN

try:
    from local_config import *
except ImportError:
    # no local config found
    pass
