from Movement_ui import Ui_Movement
from PySide6.QtWidgets import QWidget,QHeaderView,QAbstractItemView,QPushButton
from PySide6.QtSql import QSqlQuery,QSqlDatabase,QSqlQueryModel
from PySide6.QtCore import Qt,QDate
from PySide6.QtGui import QIcon


class Movement(QWidget,Ui_Movement):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Inventory Movement")
        self.retButton.clicked.connect(self.back)

        self.fromdateEdit.setDateRange(QDate(2020,1,1), QDate.currentDate())
        self.fromdateEdit.setDate(QDate(2020,1,1))
        self.todateEdit.setDateRange(QDate(2020,1,1), QDate.currentDate())
        self.todateEdit.setDate(QDate.currentDate())
        
        self.fromdateEdit.dateChanged.connect(self.newTable)
        self.todateEdit.dateChanged.connect(self.newTable)
        self.newTable()

    def newTable(self):
        self.get_connection()
        self.model = QSqlQueryModel()
        fro = self.fromdateEdit.date().toString("yyyy-MM-dd")
        to = self.todateEdit.date().toString("yyyy-MM-dd")
        query = QSqlQuery(self.db)
        query.prepare("""SELECT id,receiver,sender,type,date,description,totalprice,'' as action FROM transactions WHERE "date" >= ? AND "date" <= ?""")
        query.addBindValue(fro)
        query.addBindValue(to)
        query.exec_()

        self.model.setQuery(query)
        self.model.setHeaderData(1, Qt.Horizontal, "Receive")
        self.model.setHeaderData(2, Qt.Horizontal, "Sender")
        self.model.setHeaderData(3, Qt.Horizontal, "Type of receipt")
        self.model.setHeaderData(4, Qt.Horizontal, "Date")
        self.model.setHeaderData(5, Qt.Horizontal, "Description")
        self.model.setHeaderData(6, Qt.Horizontal, "Total price")
        self.model.setHeaderData(7, Qt.Horizontal, "Detail of receipt")
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView.hideColumn(0)

        for row in range(self.model.rowCount()):
            btn = QPushButton()
            btn.setIcon(QIcon("click.png"))
            btn.clicked.connect(lambda checked=False,rw=row:self.showDetail(rw))
            self.tableView.setIndexWidget(self.model.index(row, 7),btn)


    def get_connection(self):
        if QSqlDatabase.contains("main_connection"):
            self.db = QSqlDatabase.database("main_connection")
            return

        self.db = QSqlDatabase.addDatabase("QSQLITE", "main_connection")
        self.db.setDatabaseName("warehouse.db")
        self.db.open()

    def showDetail(self,rw):
        from Detail import Detail
        id = self.model.data(self.model.index(rw,0))
        rec = self.model.data(self.model.index(rw,1))
        sen = self.model.data(self.model.index(rw,2))
        typ = self.model.data(self.model.index(rw,3))
        date = self.model.data(self.model.index(rw,4))
        desc = self.model.data(self.model.index(rw,5))
        total = self.model.data(self.model.index(rw,6))
        self.nextWin = Detail(id,rec,sen,typ,date,desc,total)
        self.nextWin.show()
        self.close()

    def back(self):
        from Dashboard import Dashboard
        self.backWin = Dashboard()
        self.backWin.show()
        self.close()
