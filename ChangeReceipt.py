from ChangeReceipt_ui import Ui_ChangeReceipt
from PySide6.QtWidgets import QWidget,QHeaderView,QAbstractItemView,QTableWidgetItem,QMessageBox
from PySide6.QtCore import Qt,QDate
import sqlite3

class ChangeReceipt(QWidget,Ui_ChangeReceipt):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Editing receipts")
        
        self.retButton.clicked.connect(self.back)
        self.relButton.clicked.connect(self.rel)

        self.fromdateEdit.setDateRange(QDate(2020,1,1), QDate.currentDate())
        self.fromdateEdit.setDate(QDate(2020,1,1))
        self.todateEdit.setDateRange(QDate(2020,1,1), QDate.currentDate())
        self.todateEdit.setDate(QDate.currentDate())
        self.fromdateEdit.dateChanged.connect(self.DataTable)
        self.todateEdit.dateChanged.connect(self.DataTable)

        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(["ID","Receiver","Sender","Type of receipt","Date of receipt","description","Total price"])
        self.tableWidget.setColumnHidden(0,True)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QHeaderView.Stretch)
        for col in range(self.tableWidget.columnCount()):
            if col != 5:
                header.setMinimumSectionSize(80)
        self.tableWidget.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.tableWidget.itemChanged.connect(self.itemChange)
        self.DataTable()

    def DataTable(self):
        self.tableWidget.setRowCount(0)
        fro = self.fromdateEdit.date().toString("yyyy-MM-dd")
        to = self.todateEdit.date().toString("yyyy-MM-dd")
        conn = sqlite3.connect("warehouse.db")
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM transactions WHERE "date" >= ? AND "date" <= ?""",(fro,to))
        datas = cursor.fetchall()
        conn.close()
        for i in datas:
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            id_item = QTableWidgetItem(str(i[0]))
            receiver_item = QTableWidgetItem(i[1])
            sender_item = QTableWidgetItem(i[2])
            type_item = QTableWidgetItem(i[3])
            date_item = QTableWidgetItem(i[4])
            description_item = QTableWidgetItem(i[5])
            total_item = QTableWidgetItem(str(i[6]))

            receiver_item.setFlags(receiver_item.flags() & ~Qt.ItemIsEditable)
            sender_item.setFlags(sender_item.flags() & ~Qt.ItemIsEditable)
            type_item.setFlags(type_item.flags() & ~Qt.ItemIsEditable)
            date_item.setFlags(date_item.flags() & ~Qt.ItemIsEditable)
            total_item.setFlags(type_item.flags() & ~Qt.ItemIsEditable)

            self.tableWidget.blockSignals(True)
            self.tableWidget.setItem(row, 0, id_item)
            self.tableWidget.setItem(row, 1, receiver_item)
            self.tableWidget.setItem(row, 2, sender_item)
            self.tableWidget.setItem(row, 3, type_item)
            self.tableWidget.setItem(row, 4, date_item)
            self.tableWidget.setItem(row,5,description_item)
            self.tableWidget.setItem(row,6,total_item)
            self.tableWidget.blockSignals(False)
    
    def itemChange(self,item):
        ret = QMessageBox.warning(self,"Warning!!!","Are you sure you want to change? This change is going to be permanent. If you press ok, change submits otherwise the change doesn't submit",QMessageBox.Ok | QMessageBox.Cancel)
        if ret == QMessageBox.Ok:
            conn = sqlite3.connect("warehouse.db")
            cursor = conn.cursor()
            id = int(self.tableWidget.item(item.row(),0).text().strip())
            if item.column() == 5:
                    description = item.text().strip()
                    cursor.execute("UPDATE transactions SET description = ? WHERE id = ?",(description,id))
                    conn.commit()
                    conn.close()
        else:
            self.BackToNormal(item)

    def BackToNormal(self,item):
        id = int(self.tableWidget.item(item.row(),0).text().strip())
        conn = sqlite3.connect("warehouse.db")
        cursor = conn.cursor()
        cursor.execute("SELECT description FROM transactions WHERE id = ?",(id,))
        datas = cursor.fetchall()
        self.tableWidget.blockSignals(True)
        item.setText(datas[0][0])
        self.tableWidget.blockSignals(False)
        conn.close()
    
    def rel(self):
        self.fromdateEdit.setDate(QDate(2020,1,1))
        self.todateEdit.setDate(QDate.currentDate())

    def back(self):
        from Dashboard import Dashboard
        self.backWin = Dashboard()
        self.backWin.show()
        self.close()