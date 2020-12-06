import sys
path = "/usr/local/lib/python3.8/dist-packages"
sys.path.insert(0, path)

import pymysql
pymysql.version_info = (1, 3, 13, "final", 0)
pymysql.install_as_MySQLdb()
