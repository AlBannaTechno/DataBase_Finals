"""
warn :
    if we haven't a permessions to modify file in this folder
    any change on the table will refuse
    so we need to use admin or start it via python *.py from command(Admin) on windows
    or sudo in linux
    but if folder is ordinary folder our program will work correctly
    without any need to upper permessions


"""

import sys
from PyQt4 import QtCore, QtGui, QtSql


"""
warn :
    sports.db database  created from:
        create_simple_sqllite_db.py

"""


def initializeModel(model):

    model.setTable('sportsmen')
    print(model.tableName())
    model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
    model.select()
    model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
    model.setHeaderData(1, QtCore.Qt.Horizontal, "First name")
    model.setHeaderData(2, QtCore.Qt.Horizontal, "Last name")
    return model


def createView(title, model):
    view = QtGui.QTableView()
    # model.setFilter("ID = 104")
    # model.database().transaction()

    model.select()
    view.setModel(model)
    view.setSpan(0, 0, 1, model.columnCount())
    view.setWindowTitle(title)
    return view


def addrow():
    print(model.rowCount())
    ret = model.insertRows(model.rowCount(), 1)
    print(ret)


def findrow(i):
    delrow = i.row()
def full_exe():
    query=QtSql.QSqlQuery()
    # current_command="select * from  sportsmen"

    current_command="PRAGMA table_info(sportsmen)"
    query.exec_(current_command)
    final_result = ""
    tables_name=[]
    while query.next():
        temp_res = ""
        try:
            for a in range(0, 100):
                if query.value(a) != None:
                    temp_res += (str(query.value(a)) + ",")
            final_result += temp_res + "\n"
        except:
            continue
    print(final_result)
def get_cols():
    query=QtSql.QSqlQuery()
    current_command="PRAGMA table_info(sportsmen)"
    query.exec_(current_command)
    col_n=[]
    while query.next():
        try:
            for a in range(0, query.size()):
                if a==1:
                    if query.value(a) != None:
                        col_n.append(query.value(a))
                    break
        except:
            continue
    return col_n
def filtring(model,view,ser):
    # full_exe()
    if len(ser)==0:
        model.setTable("sportsmen")
        model.select()
    else:
        model.setTable("sportsmen")
        # model.setFilter("id > 103")
        ser=ser.lower()
        # model.setFilter("firstname like '%s' or lastname='%s' or id='%s'"%(ser,ser,ser))
        col_ns=get_cols()
        qu=""
        for a in col_ns:
            qu+="or {} like '%{}%'".format(a,ser)
        qu=qu[2:]
        model.setFilter(qu)

        # model.setFilter("firstname like '%{}%' or lastname like '%{}%' or id like '%{}%'".format(ser,ser,ser))
        # model.setFilter("all like '%{}%'".format(ser,ser,ser))

        # model.setFilter("firstname = {} or lastname={} or id={}".format(ser,ser,ser))
        model.select()
        view.update()
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    dlg = QtGui.QDialog()
    # db = QtSql.QSqlDatabase.addDatabase('QSQLITE',connectionName="zz")
    db = QtSql.QSqlDatabase.addDatabase('QSQLITE',"force")
    # db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('sports.db')
    model = QtSql.QSqlTableModel(dlg,db)

    delrow = -1
    model=initializeModel(model)

    view1 = createView("Table Model(View 1)", model)
    view1.clicked.connect(findrow)


    layout = QtGui.QVBoxLayout()
    layout.addWidget(view1)

    button = QtGui.QPushButton("Add a row")
    button.clicked.connect(addrow)
    layout.addWidget(button)

    btn1 = QtGui.QPushButton("del a row")
    btn1.clicked.connect(lambda: model.removeRow(view1.currentIndex().row()))
    layout.addWidget(btn1)

    dlg.setLayout(layout)
    dlg.setWindowTitle("Database Demo")
    # model.setFilter(("firstname like %{}%").format("o"))
    search=QtGui.QLineEdit()
    layout.addWidget(search)
    search.textChanged.connect(lambda :
                               filtring(model,view1,search.text())
                               )
    # filtring(model,view1)
    dlg.resize(600,400)
    # dlg.setLayoutDirection(QtCore.Qt.RightToLeft)
    dlg.show()
    sys.exit(app.exec_())