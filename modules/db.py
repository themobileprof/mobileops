# Python 3
# Author: Samuel Anyaele
# scripts/help/modules/db.py
# TheMobileProf MobileOps module database management.
# Supports: SQLite, MySQL, Postgresql, MSSQL, Oracle

import subprocess
import sqlalchemy
from . import misc

class db:
    def __init__(self,db,dbtype="sqlite",username="",password="",host="localhost"):
        # Get current directory
        self.pwd = misc.current_dir()

        # Build DB string
        self.db_string = dbtype + "//"
        # Get user details
        if username != "":
            self.db_string += username + ':' + password + '@' + host
        self.db_string += '/' + db

    def connect_db(self):
        if self.engine = create_engine(self.db_string):
            return True
        else:
            return False

