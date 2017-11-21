"""

http://stackoverflow.com/questions/372885/how-do-i-connect-to-a-mysql-database-in-python
"""
"""
this tool it's very fantastic tool
because it's work with python objects
"""
import peewee
from peewee import *


"connect to database"
# db = MySQLDatabase('TESTDB', user='root',passwd='')
"there are two database type are supported"
# db=SqliteDatabase
# db=PostgresqlDatabase
db=SqliteDatabase('TESTDBm.ldb')
"now create class which model our table"
"be careful with class name because it's Table Name"
class Bookse(peewee.Model):
    ""
    "no create data and it's data type out of constructor"
    author = peewee.CharField()
    title = peewee.TextField()
    "we must define Meta Class "
    class Meta:
        ""
        "and we must put database general variable=db"
        "if we comment database = db line and put pass"
        """
            Class Meta:
                pass
        """
        "or we remove Meta Class the program will create"
        "sql lite data base with peewee.db name and no password"
        "so we always need to define database variable"
        "warn database can't be string as database='name'"
        "it's will raise error "
        database = db

"now we create the table with Bookse name"
Bookse.create_table()
"no we will insert values into Bookse table "
book = Bookse(author="me", title='Peewee is cool')
"save inserted values"
book.save()
"search into Bookse table with filter"
for book in Bookse.filter(author="me"):
    print (book.title)

# Peewee is cool