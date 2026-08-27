from Overview_ui import Ui_Overview
from PySide6.QtWidgets import QWidget,QHeaderView,QAbstractItemView
from PySide6.QtSql import QSqlTableModel, QSqlQuery,QSqlDatabase
from PySide6.QtCore import Qt

class Overview(QWidget,Ui_Overview):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Inventory overview")

        self.retButton.clicked.connect(self.back)
        
        self.settingtable()

    def settingtable(self):
        self.get_connection()
        self.model = QSqlTableModel(db = self.db)
        self.model.setQuery(QSqlQuery("SELECT barcode,name,price,stock,min_stock FROM products",self.db))
        self.model.setHeaderData(0, Qt.Horizontal, "Barcode")
        self.model.setHeaderData(1, Qt.Horizontal, "Name")
        self.model.setHeaderData(2, Qt.Horizontal, "Price")
        self.model.setHeaderData(3, Qt.Horizontal, "Stock")
        self.model.setHeaderData(4, Qt.Horizontal, "Minimum stock")

        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def get_connection(self):
        if QSqlDatabase.contains("main_connection"):
            self.db = QSqlDatabase.database("main_connection")
            return
        self.db = QSqlDatabase.addDatabase("QSQLITE", "main_connection")
        self.db.setDatabaseName("warehouse.db")
        self.db.open()
    
    def back(self):
        from Dashboard import Dashboard
        self.backwindow = Dashboard()
        self.backwindow.show()
        self.close()