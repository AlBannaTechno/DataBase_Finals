from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtSql import *
from DataBase_Finals.pyqt_t.with_qtable_mode.c2_class import dbController
import sys

# from dbController import dbController
"""
when we specify connection name we should use next step
    but when we use this option with table model we must use the steps

db = QSqlDatabase.addDatabase('QSQLITE',connectionName="osp")
db.setDatabaseName('sports.db')
db.open()# we must open database manually
qu=QSqlQuery(db)
model.setQuery(qu)
model = QSqlTableModel(None,db)
    we can replace none with any another permitted value
--------------------
    we can change query vi :
        # model.setQuery(qu)
"""



app=QApplication(sys.argv)
window=QWidget()
vbox=QHBoxLayout()
tv=QTableView()
vbox.addWidget(tv)
window.setLayout(vbox)

dbc=dbController()
db = QSqlDatabase.addDatabase('QSQLITE',connectionName="osp")

db.setDatabaseName('sports.db')
print(db.open())
qu=QSqlQuery(db)
model = QSqlTableModel(None,db)
dbc.initializeModel2(model,"sportsmen",tv,[])
dbc.createView("sd")
window.show()
app.exec_()


# app=QApplication(sys.argv)
# db = QSqlDatabase.addDatabase('QSQLITE',connectionName="oop")
# db.setDatabaseName("sports.db")
# print(db.open())
# qu=QSqlQuery(db)
# qu.exec_("select * from sportsmen")
# qu.next()
# print(qu.value(1))
# app.exec_()