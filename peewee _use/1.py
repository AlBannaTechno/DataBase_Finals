"""

http://stackoverflow.com/questions/372885/how-do-i-connect-to-a-mysql-database-in-python


"""

#!/usr/bin/python
import pymysql as MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="",  # your password
                     db="TESTDB")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM MyGuests")

# print all the first cell of all the rows
for row in cur.fetchall():
    print (row)

db.close()