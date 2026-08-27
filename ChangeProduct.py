from ChangeProduct_ui import Ui_ChangeProduct
from PySide6.QtWidgets import QWidget,QCompleter,QHeaderView,QAbstractItemView,QTableWidgetItem,QMessageBox
from PySide6.QtCore import Qt
import sqlite3

class ChangeProduct(QWidget,Ui_ChangeProduct):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Editing products")
        self.retButton.clicked.connect(self.back)
        self.relButton.clicked.connect(self.rel)

        conn = sqlite3.connect("warehouse.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id,name FROM products")
        rows = cursor.fetchall()
        conn.close()

        self.comboBox.addItem("All",None)
        for ids, name in rows:
            self.comboBox.addItem(name, ids)
        names = [i[1] for i in rows]
        completer = QCompleter(names)
        completer.setFilterMode(Qt.MatchContains) 
        completer.setCompletionMode(QCompleter.PopupCompletion)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.comboBox.setCompleter(completer)
        self.comboBox.currentIndexChanged.connect(self.DataTable)

        self.tableWidget.setColumnCount(6)
        self.tableWidget.setHorizontalHeaderLabels(["ID","Barcode","Name","Price","Stock","Minimum stock"])
        self.tableWidget.setColumnHidden(0,True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.tableWidget.itemChanged.connect(self.itemChange)
        self.DataTable(0)

    def DataTable(self,index):
        self.tableWidget.setRowCount(0)
        conn = sqlite3.connect("warehouse.db")
        cursor = conn.cursor()
        if self.comboBox.itemData(index) == None:
            cursor.execute("SELECT * FROM products")
        else:
            id = self.comboBox.itemData(index)
            cursor.execute("SELECT * FROM products WHERE id = ?",(id,))
        datas = cursor.fetchall()
        conn.close()

        for i in datas:
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            id_item = QTableWidgetItem(str(i[0]))
            barcode_item = QTableWidgetItem(i[1])
            name_item = QTableWidgetItem(i[2])
            price_item = QTableWidgetItem(str(i[3]))
            stock_item = QTableWidgetItem(str(i[4]))
            min_item = QTableWidgetItem(str(i[5]))

            name_item.setFlags(name_item.flags() & ~Qt.ItemIsEditable)
            stock_item.setFlags(price_item.flags() & ~Qt.ItemIsEditable)

            self.tableWidget.blockSignals(True)
            self.tableWidget.setItem(row, 0, id_item)
            self.tableWidget.setItem(row, 1, barcode_item)
            self.tableWidget.setItem(row, 2, name_item)
            self.tableWidget.setItem(row, 3, price_item)
            self.tableWidget.setItem(row, 4, stock_item)
            self.tableWidget.setItem(row,5,min_item)
            self.tableWidget.blockSignals(False)


    def itemChange(self,item):
        ret = QMessageBox.warning(self,"Warning!!!","Are you sure you want to change? This change is going to be permanent. If you press ok, change submits otherwise the change doesn't submit",QMessageBox.Ok | QMessageBox.Cancel)
        if ret == QMessageBox.Ok:
            conn = sqlite3.connect("warehouse.db")
            cursor = conn.cursor()
            id = int(self.tableWidget.item(item.row(),0).text().strip())
            match item.column():
                case 1:
                    barcode = item.text().strip()
                    try:
                        cursor.execute("UPDATE products SET barcode = ? WHERE id = ?",(barcode,id))
                        conn.commit()
                        conn.close()
                    except sqlite3.IntegrityError:
                        QMessageBox.critical(self,"Error!!","This barcode is taken by another product. you have to change it")
                        self.BackToNormal(item)
                        conn.close()
                case 3:
                    price = item.text().strip()
                    try:
                        price = float(price)
                        if price < 0:
                            QMessageBox.critical(self,"Error!!","You have to enter true price for product.Price can't be negative. You have to change it to a correct number.")
                            conn.close()
                            self.BackToNormal(item)
                            return
                        cursor.execute("UPDATE products SET price = ? WHERE id = ?",(price,id))
                        conn.commit()
                        conn.close()
                    except ValueError:
                        QMessageBox.critical(self,"Error!!","You have to enter true price for product.Price should be float. You have to change it to a correct number.")
                        conn.close()
                        self.BackToNormal(item)
                        return
                case 5:
                    min_stock = item.text().strip()
                    try:
                        min_stock = int(min_stock)
                        if min_stock < 0:
                            QMessageBox.critical(self,"Error!!","You have to enter true minimum stock for product.It can't be negative. You have to change it to a correct number.")
                            conn.close()
                            self.BackToNormal(item)
                            return
                        cursor.execute("UPDATE products SET min_stock = ? WHERE id = ?",(min_stock,id))
                        conn.commit()
                        conn.close()
                    except ValueError:
                        QMessageBox.critical(self,"Error!!","you have to enter true Minimum stock for product.It should be int. You have to change it to a correct number.")
                        conn.close()
                        self.BackToNormal(item)
        else:
            self.BackToNormal(item)

    def BackToNormal(self,item):
        id = int(self.tableWidget.item(item.row(),0).text().strip())
        conn = sqlite3.connect("warehouse.db")
        cursor = conn.cursor()
        cursor.execute("SELECT barcode,price,min_stock FROM products WHERE id = ?",(id,))
        datas = cursor.fetchall()
        self.tableWidget.blockSignals(True)
        match item.column():
            case 1:
                item.setText(datas[0][0])
            case 3:
                item.setText(str(datas[0][1]))
            case 5:
                item.setText(str(datas[0][2]))
        self.tableWidget.blockSignals(False)
        conn.close()

    def back(self):
        from Dashboard import Dashboard
        self.backWin = Dashboard()
        self.backWin.show()
        self.close()

    def rel(self):
        self.comboBox.setCurrentIndex(0)
        self.DataTable(0)