"""
https://code.google.com/archive/p/pypyodbc/wikis/pypyodbc_for_access_mdb_file.wiki
"""""
import pypyodbc

mymdb=pypyodbc.win_create_mdb( "database4.mdb" )
conn = pypyodbc.win_connect_mdb("database4.mdb")

cur = conn.cursor()
cur.execute(u"""CREATE TABLE pypyodbc_test_tabl (ID INTEGER PRIMARY KEY,product_name TEXT)""")

cur.execute(u"""INSERT INTO pypyodbc_test_tabl VALUES (1,'PyPyODBC')""")

cur.close()
conn.commit()
conn.close()

# to connect to existing
# pypyodbc.win_compact_mdb("D:\\The path to the original to be compacted mdb file" ,"D:\\The path to put the compacted new mdb file")