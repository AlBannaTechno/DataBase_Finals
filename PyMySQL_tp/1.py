"""
OK
------------
https://www.tutorialspoint.com/python3/python_database_access.htm
"""
"""
db = PyMySQL.connect("host","user name","pass word","data base name" )
if we haven't password just but it =""

lock at  next site to know how to set password and other options
http://superuser.com/questions/603026/mysql-how-to-fix-access-denied-for-user-rootlocalhost

-----------------------------
we can connect to data base with mysql.exe -u username data_base_name
for example
>>>mysql.exe -u root employee

also we can use pass word if exist
>>>mysql.exe -u root -p employee
password:write pass here
but if we didn't set any password it's will produce
ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: YES).


"""


import pymysql as PyMySQL

# Open database connection

db = PyMySQL.connect("localhost","root","","TESTDB" )
# db = PyMySQL.connect("","root","","TESTDB" ) :default host is localhost=127.0.0.1

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print ("Database version : %s " % data)

# disconnect from server
db.close()