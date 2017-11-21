import sys
from PyQt4 import QtCore, QtGui, QtSql

app=QtGui.QApplication(sys.argv)
class dbController():
    def __init__(self,model=QtSql.QSqlTableModel(), tablename="", tableviewn=QtGui.QTableView(),headersinfo=[]):
        self.model=model
        self.tablename=tablename
        self.headersinfo=headersinfo
        self.view =tableviewn

        self.title=""
        self.initializeModel()
    def initializeModel2(self,model, tablename,tableview, headersinfo=[]):
        self.model=model
        self.model.setTable(tablename)

        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.model.select()
        self.view = tableview
        couunter = 0
        for a in headersinfo:
            self.model.setHeaderData(couunter, QtCore.Qt.Horizontal, a)
            couunter+=1

    def initializeModel(self):
        self.model.setTable(self.tablename)
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.model.select()
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "First name")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Last name")

    def createView(self,title):
        self.view.setModel(self.model)
        self.view.setWindowTitle(title)
        self.view.clicked.connect(self.findrow)
        self.title=title
    def addrow(self):
        # print(self.model.rowCount())
        ret = self.model.insertRows(self.model.rowCount(), 1)
        # print(ret)

    def addrow_lambda(sefl,Mmodel):
        # print(Mmodel.rowCount())
        ret = Mmodel.insertRows(Mmodel.rowCount(), 1)
        # print(ret)

    def findrow(i):
        return
        delrow = i.row()


if __name__=="__main__":
    windows=dbController()
    mwin=QtGui.QWidget()
    mly=QtGui.QHBoxLayout()
    mly.addWidget(windows.view)
    mwin.setLayout(mly)
    mwin.show()
    app.exec_()