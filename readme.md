##### Python-db
##### This repository will explain many different method to connect to data base with python

# Current Libs : 
## pymysql :
    (on linux : PyMySQL)->support mysql server database
#### can
    only connect to database on sql live server
## peewee :
#### support:
        MySQLDatabase
        SqliteDatabase
        PostgresqlDatabase
#### Notes :
    use object models instead of direct querys
    very important and easy and safety library
#### can :
        only create sqllite database without password
        connect to sqlite ,mysql and postgrees databases
## sqlite3:
    use with sqlite database only
#### can :
    create and connect to sqllite database
    
## Microsoft Access DataBase
    (*.mdb(access 2000),*.accdb(recently))
#### 1- pypyodbc:
    type to connect : mdb
##### can :
        create and connect to mdb database

#### 2- pyodbc:
    type : mdb , accdb but i can'r connect to accdb although it's support it
##### can:
        connect only to database
#### 3- odbc :
    can only connect to database mdb
##### Notes :    
    if we can correct pyodbc to connect to accdb we then can modify odbc
    to connect to this data base
    this is very bad library to use

#
## Pyqt-database-handler
            Driver Type             Description
            QDB2                    IBM DB2
            QIBASE                  Borland InterBase Driver
            QMYSQL                  MySQL Driver
            QOCI                    Oracle Call Interface Driver
            QODBC                   ODBC Driver (includes Microsoft SQL Server)
            QPSQL                   PostgreSQL Driver
            QSQLITE                 SQLite version 3 or above
            QSQLITE2                SQLite version 2
#### Notes :
Support AutoComplete [for all ids ]/without need to do a dynamic resolve
#### can :
        connect to all previous databases -not work with microsoft access database-
        -but work with microsoft sql server-
        
        Create sqlLite DataBase
        
        has very important technique :
            specify Connection name it's allow us to use many databases with many queries
            at the same time without make any conflict

##### GoodLuck
##### Al Banna Techno