from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtSql import *
from DataBase_Finals.pyqt_t.with_qtable_mode.clas_ss import dbController
import sys

# from dbController import dbController

app=QApplication(sys.argv)
window=QWidget()
vbox=QHBoxLayout()
tv=QTableView()
vbox.addWidget(tv)
window.setLayout(vbox)

dbc=dbController()
db = QSqlDatabase.addDatabase('QSQLITE')
db.setDatabaseName('sports.db')
model = QSqlTableModel()

dbc.initializeModel2(model,"sportsmen",tv,[])
dbc.createView("sd")
window.show()
app.exec_()