from Detail_ui import Ui_Detail
from PySide6.QtWidgets import QWidget,QHeaderView,QAbstractItemView
from PySide6.QtSql import QSqlQuery,QSqlDatabase,QSqlQueryModel
from PySide6.QtCore import Qt

class Detail(QWidget,Ui_Detail):
    def __init__(self,id,receiver,sender,typ,date,desc,total):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Detail Factor")
        self.retButton.clicked.connect(self.back)

        self.RecSenlabel.setText("Factor Detail:   Receiver: "+receiver+"             -Sender: "+sender)
        self.tydalabel.setText("Type of Factor: "+typ+"             -Date: "+date)
        if desc == "":
            self.Desclabel.setText("No Description!")
        else:
            self.Desclabel.setText("Description: "+desc)
        self.totallabel.setText("Total price:"+str(total))
        self.get_connection()
        self.model = QSqlQueryModel()
        query = QSqlQuery(self.db)
        query.prepare("SELECT p.barcode,p.name,p.price,g.number,g.totalprice FROM products as p INNER JOIN goodsoftransactions as g ON g.product_id = p.id WHERE g.transaction_id = ?")
        query.addBindValue(id)
        query.exec_()


        self.model.setQuery(query)
        self.model.setHeaderData(0, Qt.Horizontal, "Barcode")
        self.model.setHeaderData(1, Qt.Horizontal, "Name")
        self.model.setHeaderData(2, Qt.Horizontal, "Price")
        self.model.setHeaderData(3, Qt.Horizontal, "Amount")
        self.model.setHeaderData(4, Qt.Horizontal, "Total price")
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def back(self):
        from Movement import Movement
        self.backWin = Movement()
        self.backWin.show()
        self.close()

    def get_connection(self):
        if QSqlDatabase.contains("main_connection"):
            self.db = QSqlDatabase.database("main_connection")
            return

        self.db = QSqlDatabase.addDatabase("QSQLITE", "main_connection")
        self.db.setDatabaseName("warehouse.db")
        self.db.open()