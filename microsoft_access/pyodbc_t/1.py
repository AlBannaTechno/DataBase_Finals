import pyodbc
db_file = r'''../Database1.accdb'''
user = 'admin'
password = ''

# odbc_conn_str = 'DRIVER={Microsoft Access Driver (*.mdb)};DBQ=%s;UID=%s;PWD=%s' %\
#                 (db_file, user, password)
# Or, for newer versions of the Access drivers:
odbc_conn_str = 'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=%s;UID=%s;PWD=%s' %\
                (db_file, user, password)

conn = pyodbc.connect(odbc_conn_str)