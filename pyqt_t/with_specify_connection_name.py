#####################################################################
# test.py                                                           #
# ! /usr/bin/env python                                             #
#  -*- coding: utf-8 -*-                                            #
#####################################################################

from PyQt4 import QtGui, QtCore, QtSql
from src.database import DBase

class Test(QtGui.QMainWindow):

    def __init__(self):
        super(Test, self).__init__()

        self.tview = QtGui.QTableView()
        self.setCentralWidget(self.tview)
        model = QtSql.QSqlTableModel(self)
        model.setTable("person")
        model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        model.select()
        model.setHeaderData(0, QtCore.Qt.Horizontal, QtCore.QObject.trUtf8(model, "№"))
        model.setHeaderData(1, QtCore.Qt.Horizontal, QtCore.QObject.trUtf8(model, "Name"))
        model.setHeaderData(2, QtCore.Qt.Horizontal, QtCore.QObject.trUtf8(model, "Lastname"))

        self.tview.setModel(model)

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    db = DBase()
    db.connection_db()
    window = Test()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec_())

#####################################################################
# database.py                                                       #
# ! /usr/bin/env python                                             #
#  -*- coding: utf-8 -*-                                            #

from PyQt4 import QtSql, QtGui

class DBase():
    def connection_db(self):
        db=QtSql.QSqlDatabase.addDatabase("QSQLITE", "Base")
        db.setDatabaseName("db.sqlite")
        if db.open():
            print ('DataBase is now opened.')
            query = QtSql.QSqlQuery()
            query.exec_("create table person(id int primary key, "
                    "firstname varchar(20), lastname varchar(20))")
            query.exec_("insert into person values(101, 'Danny', 'Young')")
            query.exec_("insert into person values(102, 'Christine', 'Holand')")
            query.exec_("insert into person values(103, 'Lars', 'Gordon')")
            query.exec_("insert into person values(104, 'Roberto', 'Robitaille')")
        return True