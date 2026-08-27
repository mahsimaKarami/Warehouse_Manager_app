from PySide6.QtWidgets import QWidget,QMessageBox
from NewWindow_ui import Ui_NewWindow
import sqlite3
from spellchecker import SpellChecker

class NewWindow(QWidget,Ui_NewWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Add new product")
        self.submitButton.clicked.connect(self.submit)
        self.relButton.clicked.connect(self.rel)
        self.retButton.clicked.connect(self.back)

    def submit(self):
        name = self.nameLine.text().strip()
        barcode = self.codeLine.text().strip()
        price = self.priceLine.text().strip()
        minstock = self.stockLine.text().strip()
        if len(name) == 0:
            QMessageBox.critical(self,"Error!!","You have to enter a name for product. Type a name in the box of name.")
        elif len(barcode) == 0:
            QMessageBox.critical(self,"Error!!","You have to enter a barcode for product. Type a barcode in the box of barcode.")
        elif not(minstock.isdigit()) and len(minstock) != 0:
            QMessageBox.critical(self,"Error!!","You have to enter true number for minimum stock.It should be integer and positive. Type a true number in the box of minimum stock.")
        elif len(price) == 0:
            QMessageBox.critical(self,"Error!!","You have to enter a price for product. Type a true price(It should be float and positive) in the box of price.")
        else:
            try:
                price = float(price)
                if price < 0:
                    QMessageBox.critical(self,"Error!!","You have to enter true price for product.Price can't be negative. Change it.")
                    return
            except ValueError:
                QMessageBox.critical(self,"Error!!","You have to enter true price for product.Price should be float. Change it.")
                return
            conn = sqlite3.connect("warehouse.db")
            cursor = conn.cursor()
            punctuations = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
            name2 = name
            for ch in punctuations:
                name2 = name.replace(ch, " ")
            words = name2.split()
            spell = SpellChecker(language='en')
            wrongs = spell.unknown(words)
            if len(wrongs) != 0:
                result = []
                for word in wrongs:
                    correct = spell.correction(word)
                    result.append("word '"+word+"' seems wrong. Suggested: '"+correct+"'")
                result.append("If you want to correct these words for you, press ok otherwise nothing changes")
                text = "\n".join(result)
                ret = QMessageBox.information(self,"wrong dictation!!",text,QMessageBox.Ok | QMessageBox.Cancel)
                if ret == QMessageBox.Ok:
                    new_words = []
                    for word in words:
                        if word in wrongs:
                            new_words.append(spell.correction(word))
                        else:
                            new_words.append(word)
                    name = " ".join(new_words)
                    self.nameLine.setText(name)
                    return
                
            if len(minstock) == 0:
                try:
                    cursor.execute("SELECT name from products")
                    data = cursor.fetchall()
                    lst = []
                    for i in data:
                        lst.append(i[0])
                    if name.capitalize() in lst:
                        QMessageBox.critical(self,"Error!!","This name is taken by another product. You have to change it.")
                        conn.close()
                        return
                    else:
                        cursor.execute("INSERT INTO products (barcode,name,price) VALUES (?,?,?)",(barcode,name.capitalize(),price))
                except sqlite3.IntegrityError:
                    QMessageBox.critical(self,"Error!!","This barcode is taken by another product.  you have to change it")
                    conn.close()
                    return
            else:
                try:
                    cursor.execute("SELECT name from products")
                    data = cursor.fetchall()
                    lst = []
                    for i in data:
                        lst.append(i[0])
                    if name.capitalize() in lst:
                        QMessageBox.critical(self,"Error!!","This name is taken by another product. Ypu have to change it.")
                        conn.close()
                        return
                    else:
                        cursor.execute("INSERT INTO products (barcode,name,price,min_stock) VALUES (?,?,?,?)",(barcode,name.capitalize(),price,int(minstock)))
                except sqlite3.IntegrityError:
                    QMessageBox.critical(self,"Error!!","This barcode is taken by another product. You have to change it.")
                    conn.close()
                    return
            conn.commit()
            conn.close()
            self.rel()
            QMessageBox.information(self,"Congratulations!!!","You entered product successfully!")
    
    def rel(self):
        self.nameLine.setText("")
        self.codeLine.setText("")
        self.priceLine.setText("")
        self.stockLine.setText("")

    def back(self):
        from Dashboard import Dashboard
        self.backwindow = Dashboard()
        self.backwindow.show()
        self.close()
        
        
    