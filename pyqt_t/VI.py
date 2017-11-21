"""
https://www.tutorialspoint.com/pyqt/pyqt_database_handling.htm

-----------------------------------------------------------------------------------------

PyQt API contains an elaborate class system to communicate with many SQL based databases.
Its QSqlDatabase provides access through a Connection object. Following is the list of currently
available SQL drivers:
Driver Type Description
QDB2                    IBM DB2
QIBASE                  Borland InterBase Driver
QMYSQL                  MySQL Driver
QOCI                    Oracle Call Interface Driver
QODBC                   ODBC Driver (includes Microsoft SQL Server)
QPSQL                   PostgreSQL Driver
QSQLITE                 SQLite version 3 or above
QSQLITE2                SQLite version 2

-------------------------------How to Use--------------------

A connection with a SQLite database is established using the static method −

db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
db.setDatabaseName('sports.db')


        --------------------------------------
Other methods of QSqlDatabase class are as follows −

                    Methods & Description
1
setDatabaseName()

Sets the name of the database with which connection is sought

2
setHostName()

Sets the name of the host on which the database is installed

3
setUserName()

Specifies the user name for connection

4
setPassword()

Sets the connection object’s password if any

5
commit()

Commits the transactions and returns true if successful

6
rollback()

Rolls back the database transaction

7
close()

Closes the connection


-----------------------------------------------------------------

query = QtSql.QSqlQuery()
query.exec_("create table sportsmen(id int primary key,
   " "firstname varchar(20), lastname varchar(20))")

---
we also can use
db = QtSql.QSqlDatabase.addDatabase('dataBaseType',connectionname="anything")
db.setDatabaseName('sports.db')
query = QtSql.QSqlQuery(db)


"""