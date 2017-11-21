import pyodbc
# db_file = r'''C:\x.mdb'''
db_file="E:\\ProjectsUnderWork\\TheLastBrain\\HyperPyQTProjects\\GEnSols\\DataBase_Finals\\microsoft_access\\fromSingleProject\\database4.mdb"
# user = 'admin'
user=""
password = ''

odbc_conn_str = 'DRIVER={Microsoft Access Driver (*.mdb)};DBQ=%s;UID=%s;PWD=%s' %\
                (db_file, user, password)
# Or, for newer versions of the Access drivers:

# odbc_conn_str = 'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=%s;UID=%s;PWD=%s' %\
#                 (db_file, user, password)

conn = pyodbc.connect(odbc_conn_str)

# from docs
# # cnxn = pyodbc.connect('DSN=DataSourceName;UID=user;PWD=password')
# co=pyodbc.connect("DSN=database4.mdb;UID=;PWD=")
