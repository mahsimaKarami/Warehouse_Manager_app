from PySide6.QtWidgets import QWidget,QHeaderView,QAbstractItemView
from Dashboard_ui import Ui_Dashboard
from newWindow import NewWindow
from ReceiveForm import ReceiveForm
from ChangeProduct import ChangeProduct
from ChangeReceipt import ChangeReceipt
from PySide6.QtSql import QSqlTableModel, QSqlQuery,QSqlDatabase
from PySide6.QtCore import Qt



class Dashboard(QWidget,Ui_Dashboard):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Dashboard")
        self.newButton.clicked.connect(self.new)
        self.recButton.clicked.connect(self.form1)
        self.sellButton.clicked.connect(self.form2)
        self.overButton.clicked.connect(self.overview)
        self.movButton.clicked.connect(self.movement)
        self.PchanButton.clicked.connect(self.changeProduct)
        self.RchanButton.clicked.connect(self.ChangeReceipt)

        self.get_connection()
        self.model = QSqlTableModel(db=self.db)
        self.model.setQuery(QSqlQuery("SELECT barcode,name,price,stock,min_stock FROM products WHERE stock <= min_stock",self.db))
        self.model.setHeaderData(0, Qt.Horizontal, "Barcode")
        self.model.setHeaderData(1, Qt.Horizontal, "Name")
        self.model.setHeaderData(2, Qt.Horizontal, "Price")
        self.model.setHeaderData(3, Qt.Horizontal, "Stock")
        self.model.setHeaderData(4, Qt.Horizontal, "Minimum stock")

        self.lowstockTable.setModel(self.model)
        self.lowstockTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.lowstockTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
    
    def new(self):
        self.newWin = NewWindow()
        self.newWin.show()
        self.close()
    
    def form1(self):
            self.recWin = ReceiveForm(1)
            self.recWin.show()
            self.close()
    
    def form2(self):
            self.exWin = ReceiveForm(2)
            self.exWin.show()
            self.close()

    def overview(self):
        from Overview import Overview
        self.overviewWin = Overview()
        self.overviewWin.show()
        self.close()

    def movement(self):
         from Movement import Movement
         self.movWin = Movement()
         self.movWin.show()
         self.close()


    def changeProduct(self):
        self.changep = ChangeProduct()
        self.changep.show()
        self.close()
    
    def ChangeReceipt(self):
        self.changer = ChangeReceipt()
        self.changer.show()
        self.close()

    def get_connection(self):
        if QSqlDatabase.contains("main_connection"):
            self.db = QSqlDatabase.database("main_connection")
            return
        self.db = QSqlDatabase.addDatabase("QSQLITE", "main_connection")
        self.db.setDatabaseName("warehouse.db")
        self.db.open()