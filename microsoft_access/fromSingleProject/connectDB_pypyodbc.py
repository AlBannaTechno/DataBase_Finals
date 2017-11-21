"""
https://code.google.com/archive/p/pypyodbc/wikis/pypyodbc_for_access_mdb_file.wiki
"""""
import pypyodbc

# mymdb=pypyodbc.win_create_mdb( "database4.mdb" )
conn = pypyodbc.win_connect_mdb("database4.mdb")
pypyodbc.win_create_mdb("cof_d.mdb")

cur = conn.cursor()
cur.execute(u"""
SELECT * FROM TAB1;
""")

vv=cur.fetchall()
print (vv)
cur.close()
conn.commit()
conn.close()

# to connect to existing
