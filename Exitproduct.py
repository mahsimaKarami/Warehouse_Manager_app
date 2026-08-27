from Exitproduct_ui import Ui_Exitproduct
from PySide6.QtWidgets import QWidget, QCompleter,QMessageBox,QTableWidgetItem,QHeaderView,QPushButton,QAbstractItemView
from PySide6.QtPrintSupport import QPrinter,QPrintPreviewDialog
from PySide6.QtGui import QIcon,QCloseEvent,QTextDocument,QPageLayout,QHideEvent
from PySide6.QtCore import Qt,QMarginsF
import sqlite3

class Exitproduct(QWidget,Ui_Exitproduct):
    def __init__(self,mainWindow):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Add products to the receipt of Issue")
        self.mainWindow = mainWindow

        conn = sqlite3.connect("warehouse.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id,name FROM products")
        rows = cursor.fetchall()
        conn.close()

        for id_, name in rows:
            self.comboBox.addItem(name, id_)
        names = [i[1] for i in rows]
        completer = QCompleter(names)
        completer.setFilterMode(Qt.MatchContains) 
        completer.setCompletionMode(QCompleter.PopupCompletion)
        self.comboBox.setCompleter(completer)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.selected_id = self.comboBox.currentData()

        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(["Barcode","Name","Price","Available","Amount","Total price","Delete"])
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.tableWidget.itemChanged.connect(self.itemChange)


        self.AddButton.clicked.connect(self.add)
        self.retButton.clicked.connect(self.back)
        self.relButton.clicked.connect(self.rel)
        self.submitButton.clicked.connect(self.addtodb)
        self.homeButton.clicked.connect(self.home)

    def self_maker(self,rec,send,date,desc):
        self.rec = rec
        self.send = send
        self.date = date
        self.desc = desc

    def add(self):
        data = self.comboBox.currentText()
        if self.duplicateInTable(data):
            QMessageBox.critical(self,"Error!!","This item exists in table. If you want to change stock,you have to double click on stock of it in tablee")
        else:
            selected_id = self.comboBox.currentData()
            conn = sqlite3.connect("warehouse.db")
            cursor = conn.cursor()
            cursor.execute("SELECT barcode,name,price,stock,min_stock FROM products WHERE id = ?",(int(selected_id),))
            data = cursor.fetchall()
            conn.close()
            if data[0][3] == 0:
                QMessageBox.critical(self,"Error!!","This item's stock is zero. You can't add this item because there is no item left in warehouse")
            else:
                row = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row)
                barcode_item = QTableWidgetItem(data[0][0])
                name_item = QTableWidgetItem(data[0][1])
                price_item = QTableWidgetItem(str(data[0][2]))
                available_item = QTableWidgetItem(str(data[0][3]))
                stock_item = QTableWidgetItem("1")
                total_item = QTableWidgetItem(str(data[0][2]))


                barcode_item.setFlags(barcode_item.flags() & ~Qt.ItemIsEditable)
                name_item.setFlags(name_item.flags() & ~Qt.ItemIsEditable)
                price_item.setFlags(price_item.flags() & ~Qt.ItemIsEditable)
                total_item.setFlags(total_item.flags() & ~Qt.ItemIsEditable)
                available_item.setFlags(available_item.flags() & ~Qt.ItemIsEditable)

                self.tableWidget.blockSignals(True)
                self.tableWidget.setItem(row, 0, barcode_item)
                self.tableWidget.setItem(row, 1, name_item)
                self.tableWidget.setItem(row, 2, price_item)
                self.tableWidget.setItem(row, 3, available_item)
                self.tableWidget.setItem(row,4,stock_item)
                self.tableWidget.setItem(row,5,total_item)
                btn = QPushButton()
                btn.setIcon(QIcon("bin.png"))
                btn.clicked.connect(self.delete_row)
                self.tableWidget.setCellWidget(row, 6, btn)
                self.tableWidget.blockSignals(False)
                
                self.calculate_total()


    def back(self):
        self.mainWindow.show()
        self.hide()
        
    def rel(self):
        self.tableWidget.setRowCount(0)
        self.label_3.setText("Total price: 0")

    def home(self):
        from Dashboard import Dashboard
        self.homeWin = Dashboard()
        self.homeWin.show()
        self.close()

    def calculate_total(self):
        total = 0
        for row in range(self.tableWidget.rowCount()):
            total  += float(self.tableWidget.item(row,5).text().strip())
        self.label_3.setText("Total price: "+str(total))
        self.total = total
 
    def itemChange(self,item):
        if item.column() == 4:
            stock = item.text().strip()
            price = float(self.tableWidget.item(item.row(),2).text().strip())
            barcode = self.tableWidget.item(item.row(),0).text().strip()
            if not stock.isdigit():
                QMessageBox.critical(self, "Error!!", "You have to enter a number for stock. Type the number into the box.")
                self.tableWidget.blockSignals(True)
                item.setText("1")
                newTotal_item = QTableWidgetItem(str(price))
                newTotal_item.setFlags(newTotal_item.flags() & ~Qt.ItemIsEditable)
                self.tableWidget.setItem(item.row(),5,newTotal_item)
                self.tableWidget.blockSignals(False)
                self.calculate_total()
            elif int(stock) > int(self.tableWidget.item(item.row(),3).text().strip()):
                QMessageBox.critical(self, "Error!!", "You can't enter larger number from available amount because you don't have enough product in warehouse.")
                self.tableWidget.blockSignals(True)
                item.setText("1")
                newTotal_item = QTableWidgetItem(str(price))
                newTotal_item.setFlags(newTotal_item.flags() & ~Qt.ItemIsEditable)
                self.tableWidget.setItem(item.row(),5,newTotal_item)
                self.tableWidget.blockSignals(False)
                self.calculate_total()
            else:
                conn = sqlite3.connect("warehouse.db")
                cursor = conn.cursor()
                cursor.execute("SELECT stock,min_stock FROM products WHERE barcode = ?",(barcode,))
                data = cursor.fetchall()
                conn.close()
                if (data[0][0] - int(stock)) <= data[0][1]:
                    ret = QMessageBox.warning(self, "Warning!!", "If you choose this stock, the warehouse will run out of this product.The minimum stock is "+str(data[0][1])+" .If you have to remove this amount of products, press ok otherwise we change the stock to 1",QMessageBox.Ok | QMessageBox.Cancel)
                    if ret == QMessageBox.Ok:
                        newTotal = price * int(stock)
                        newTotal_item = QTableWidgetItem(str(newTotal))
                        newTotal_item.setFlags(newTotal_item.flags() & ~Qt.ItemIsEditable)
                        self.tableWidget.blockSignals(True)
                        self.tableWidget.setItem(item.row(),5,newTotal_item)
                        self.tableWidget.blockSignals(False)
                        self.calculate_total()
                    else:
                        self.tableWidget.blockSignals(True)
                        item.setText("1")
                        newTotal_item = QTableWidgetItem(str(price))
                        newTotal_item.setFlags(newTotal_item.flags() & ~Qt.ItemIsEditable)
                        self.tableWidget.setItem(item.row(),5,newTotal_item)
                        self.tableWidget.blockSignals(False)
                        self.calculate_total()
                else:
                    newTotal = price * int(stock)
                    newTotal_item = QTableWidgetItem(str(newTotal))
                    newTotal_item.setFlags(newTotal_item.flags() & ~Qt.ItemIsEditable)
                    self.tableWidget.blockSignals(True)
                    self.tableWidget.setItem(item.row(),5,newTotal_item)
                    self.tableWidget.blockSignals(False)
                    self.calculate_total()

    def addtodb(self):
        conn = sqlite3.connect("warehouse.db")
        cursor = conn.cursor()
        if self.tableWidget.rowCount() == 0:
            QMessageBox.critical(self,"Error!!","If the table is empty, you can't press submit. You have to enter at least one product in table. Use combo box for choosing a product. \n If you don't have nothing to remove, just turn back to dashboard by home button top of the page")
        else:
            cursor.execute("INSERT INTO transactions (receiver,sender,type,date,description,totalprice) VALUES (?,?,?,?,?,?)",(self.rec,self.send,"exit",self.date,self.desc,self.total))
            conn.commit()
            new_id = cursor.lastrowid
            for row in range(self.tableWidget.rowCount()):
                barcode = self.tableWidget.item(row,0).text().strip()
                total = float(self.tableWidget.item(row,5).text().strip())
                stock = int(self.tableWidget.item(row,4).text().strip())
                cursor.execute("SELECT id,stock FROM products WHERE barcode = ?",(barcode,))
                data = cursor.fetchall()
                totalStock = data[0][1] - stock
                cursor.execute("INSERT INTO goodsoftransactions (transaction_id,product_id,number,totalprice) VALUES (?,?,?,?)",(new_id,data[0][0],stock,total))
                cursor.execute("UPDATE products SET stock = ? WHERE id = ?",(totalStock,data[0][0]))
                conn.commit()
            conn.commit()
            conn.close()
            ret = QMessageBox.information(self,"Congratulations!!!","You made receipt successfully! if you want to print the list of products,press ok otherwise you are guided to Dashboard",QMessageBox.Ok | QMessageBox.Cancel)
            if ret == QMessageBox.Ok:
                self.print_preview()
                from Dashboard import Dashboard
                self.backwindow = Dashboard()
                self.backwindow.show()
                self.close()
            else:
                from Dashboard import Dashboard
                self.backwindow = Dashboard()
                self.backwindow.show()
                self.close()

    def duplicateInTable(self,data):
        for row in range(self.tableWidget.rowCount()):
            if self.tableWidget.item(row,1).text() == data:
                return True
        return False
    
    def delete_row(self):
        button = self.sender()
        index = self.tableWidget.indexAt(button.pos())
        row = index.row()
        self.tableWidget.removeRow(row)
        self.calculate_total()

    def printing(self,printer):
        printer.setPageMargins(QMarginsF(10, 10, 10, 10), QPageLayout.Millimeter)
        html = """
        <style>
            table { border-collapse: collapse; width: 100%; font-family: Tahoma, Arial; }
            th { background-color: #f2f2f2; border: 1px solid black; padding: 8px; text-align: center; font-weight: bold; }
            td { border: 1px solid black; padding: 6px; text-align: right; direction: rtl; }
        </style>
        <table dir="rtl">
            <thead>
                <tr>
        """
        col_count = self.tableWidget.columnCount() - 1
        for col in range(col_count):
            if col != 3:
                header_text = self.tableWidget.horizontalHeaderItem(col).text()
                html += f"<th>{header_text}</th>"
        html += "</tr></thead><tbody>"
        for row in range(self.tableWidget.rowCount()):
            html += "<tr>"
            for col in range(col_count):
                if col != 3:
                    item = self.tableWidget.item(row, col)
                    text = item.text() if item else ""
                    html += f"<td>{text}</td>"
            html += "</tr>"
        html += "</tbody></table>"
        doc = QTextDocument()
        doc.setHtml(html)
        doc.print_(printer)

    def print_preview(self):
        printer = QPrinter(QPrinter.HighResolution)
        preview = QPrintPreviewDialog(printer, self)
        preview.paintRequested.connect(self.printing)
        preview.exec()