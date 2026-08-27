from PySide6.QtWidgets import QWidget,QMessageBox,QCompleter
from PySide6.QtCore import QDate
from PySide6.QtCore import Qt
from ReceiveForm_ui import Ui_ReceiveForm
import sqlite3

class ReceiveForm(QWidget,Ui_ReceiveForm):
    def __init__(self,num):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Add detail of receipt")
        self.retButton.clicked.connect(self.back)
        self.relButton.clicked.connect(self.rel)
        self.submitButton.clicked.connect(self.submit)
        self.dateEdit.setDateRange(QDate(2020,1,1), QDate.currentDate())
        self.dateEdit.setDate(QDate.currentDate())
        self.num = num
        self.newWindow = None

        conn = sqlite3.connect("warehouse.db")
        cursor = conn.cursor()
        cursor.execute("SELECT receiver,sender FROM transactions")
        rows = cursor.fetchall()
        conn.close()

        receivers = []
        for i in rows:
            if i[0] not in receivers:
                receivers.append(i[0])
        senders = []
        for i in rows:
            if i[1] not in senders:
                senders.append(i[1])

        completerR = QCompleter(receivers)
        completerR.setFilterMode(Qt.MatchContains) 
        completerR.setCompletionMode(QCompleter.PopupCompletion)
        completerR.setCaseSensitivity(Qt.CaseInsensitive)
        self.RecEdit.setCompleter(completerR)

        completerS = QCompleter(senders)
        completerS.setFilterMode(Qt.MatchContains) 
        completerS.setCompletionMode(QCompleter.PopupCompletion)
        completerS.setCaseSensitivity(Qt.CaseInsensitive)
        self.SendEdit.setCompleter(completerS)


    def submit(self):
        receiver = self.RecEdit.text().strip()
        receiver = receiver.capitalize()
        sender = self.SendEdit.text().strip()
        sender = sender.capitalize()
        date = self.dateEdit.date().toString("yyyy-MM-dd")
        description = self.textEdit.toPlainText()

        if len(receiver) == 0:
            QMessageBox.critical(self,"Error!!","You have to enter a name for reciever. Type a name in the box of receiver.")
        elif len(sender) == 0:
            QMessageBox.critical(self,"Error!!","You have to enter a name for senderType a name in the box of sender.")
        else:
            if self.num == 1:
                from Addproduct import Addproduct
                if self.newWindow == None:
                    self.newWindow = Addproduct(self)
                    self.newWindow.self_maker(rec=receiver,send=sender,date=date,desc=description)
                    self.newWindow.show()
                    self.hide()
                else:
                    self.newWindow.show()
                    self.newWindow.self_maker(rec=receiver,send=sender,date=date,desc=description)
                    self.hide()
            else:
                from Exitproduct import Exitproduct
                if self.newWindow == None:
                    self.newWindow = Exitproduct(self)
                    self.newWindow.self_maker(rec=receiver,send=sender,date=date,desc=description)
                    self.newWindow.show()
                    self.hide()
                else:
                    self.newWindow.show()
                    self.newWindow.self_maker(rec=receiver,send=sender,date=date,desc=description)
                    self.hide()



    def rel(self):
        self.RecEdit.setText("")
        self.SendEdit.setText("")
        self.dateEdit.setDate(QDate.currentDate())
        self.textEdit.clear()

    def back(self):
        from Dashboard import Dashboard
        self.backwindow = Dashboard()
        self.backwindow.show()
        self.close()