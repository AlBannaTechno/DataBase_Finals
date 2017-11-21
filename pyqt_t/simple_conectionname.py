from PyQt4 import QtSql, QtGui


def createDB():
    """
    we should specify connection name to avoid using default connection
    which case many problems
    so we need to specify connection name in
         db = QtSql.QSqlDatabase.addDatabase('QSQLITE',connectionName="mytestconnection")
    then pass db to QSqlQuery
        query = QtSql.QSqlQuery(db)
    to use this connection
note:
    we can pass query = QtSql.QSqlQuery(db) without specifying connection name
    but this step will make query use default connection

    :return:
    """
    db = QtSql.QSqlDatabase.addDatabase('QSQLITE',connectionName="mytestconnection")
    db.setDatabaseName('sports.db')

    if not db.open():# we must do this
        QtGui.QMessageBox.critical(None, QtGui.qApp.tr("Cannot open database"),
                                   QtGui.qApp.tr("Unable to establish a database connection.\n"
                                                 "This example needs SQLite support. Please read "
                                                 "the Qt SQL driver documentation for information "
                                                 "how to build it.\n\n" "Click Cancel to exit."),
                                   QtGui.QMessageBox.Cancel)

        return False

    query = QtSql.QSqlQuery(db)

    query.exec_("create table sportsmen(id int primary key, "
                "firstname varchar(20), lastname varchar(20))")

    query.exec_("insert into sportsmen values(101, 'Roger', 'Federer')")
    query.exec_("insert into sportsmen values(102, 'Christiano', 'Ronaldo')")
    query.exec_("insert into sportsmen values(103, 'Ussain', 'Bolt')")
    query.exec_("insert into sportsmen values(104, 'Sachin', 'Tendulkar')")
    query.exec_("insert into sportsmen values(105, 'Saina', 'Nehwal')")
    return True


if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    createDB()