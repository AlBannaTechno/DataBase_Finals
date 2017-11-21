import odbc
"""
import odbc

def get_pg_ver(db_alias):
    connection = odbc.odbc(db_alias)
    try:
    	cursor = connection.cursor()
    	cursor.execute('SELECT version()')
    	for row in cursor.fetchall():
    		print row[0]
    finally:
    	connection.close()

get_pg_ver('odbc_name/user/passwd')
"""
def get_pg_ver(db_alias):
    connection=odbc.odbc(db_alias)
    try:
        cursor=connection.cursor()
        cursor.execute('SELECT version()')
        for row in cursor.fetchall():
            print(row)
    finally:
        connection.close()
get_pg_ver('Database1.accdb/admin/')
