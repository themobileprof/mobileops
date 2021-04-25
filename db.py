#!/usr/bin/env python3
# Python 3
#
# Author: Samuel Anyaele - TheMobileprof.com
# scripts/help/db.py
#
# The DB Script is a MobileOps menu-driven script
# that simplifies database management on the Linux
# commandline. It supports local and remote databases, 
# including SQLite, MySQL, PostgreSQL, MSSQL and Oracle

from modules import misc
from modules import db

# Connection to database
print("
        This MobileOps DB utility supports SQLite, MySQL, PostgreSQL, MSSQL and Oracle")




# Get database Name
database = input("What is your database name? ")





# Get DB location
get_host = input("Is your databases on this device? Yes/No ")
if not get_host.lower() in ("y","yes"):
    print("Please ensure that your database has enabled remote access, if not the connection will fail \n")
    input ("Press <Enter> to continue")
    db_remote = input("What is your database IP address? Example:123.255.255.2:5432 (Note: The part ater ':' is the database port) ")
    host = db_remote[:20]
else:
    host = "localhost"




# Get database type
misc.breaker()
db_type = input("What type of database do you want to connect to?
        1. SQLite
        2. MySQL
        3. PostgreSQL
        4. MSSQL
        5. Oracle
        Select from [1-5]: ")

# Get database name
db_num = input("What is the name of your database? ")

# if database is sqlite, skip request for username, paasword and host
if (db_num == '5'):
    db_type = "oracle+cx_oracle"
elif (db_num == '4'):
    db_type = "mssql+pymssql"
elif (db_num == '3'):
    db_type = "postgresql"
elif (db_num == '2'):
    db_type = "mysql"
elif (db_num == '1'):
    db_type = "sqlite"
else:
    db_type = "None"





# Get username
username = input("What is your database username? ")





# Get password
password = input("What is your database password? ")





mydb = db.db(db_name,db_type,username,password,host)
# Connect db
dbcnx = mydb.connect_db






# Store details locally
store_json = input("Would you like to store these details locally, to make it easier to connect next time? Yes/No: ")
if store_json.lower() in ('y','yes'):
    details = {}

    details[db_name + "_" + db_type + "_" + host] = {
      "db_type": db_type,
      "db_name": db_name,
      "username": username,
      "password": password,
      "host": host,
    }
    
    # Get content from file

    # convert content to array

    # append details array to file array

    # Convert amended areay to json

    # Save json file




dbcnx.close()
