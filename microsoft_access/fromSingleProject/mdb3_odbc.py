import odbc
db_file="database4.mdb"
user=""
password=""
def get_pg_ver(db_alias):
    connection = odbc.odbc(db_alias)
    try:
        cursor = connection.cursor()
        print(type(cursor))
        # cursor.execute('select Version()')
        # for row in cursor.fetchall():
        #     print (row[0])
    finally:
    	connection.close()
odbc_conn_str = 'DRIVER={Microsoft Access Driver (*.mdb)};DBQ=%s;UID=%s;PWD=%s' %\
                (db_file, user, password)
get_pg_ver(odbc_conn_str)