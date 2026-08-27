# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Movement.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QTableView,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_Movement(object):
    def setupUi(self, Movement):
        if not Movement.objectName():
            Movement.setObjectName(u"Movement")
        Movement.resize(1091, 818)
        self.verticalLayout = QVBoxLayout(Movement)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.retButton = QPushButton(Movement)
        self.retButton.setObjectName(u"retButton")
        icon = QIcon()
        icon.addFile(u":/return.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.retButton.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.retButton)

        self.label_4 = QLabel(Movement)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Movement)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(Movement)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.fromdateEdit = QDateEdit(Movement)
        self.fromdateEdit.setObjectName(u"fromdateEdit")
        self.fromdateEdit.setCalendarPopup(True)

        self.horizontalLayout.addWidget(self.fromdateEdit)

        self.label_3 = QLabel(Movement)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_3)

        self.todateEdit = QDateEdit(Movement)
        self.todateEdit.setObjectName(u"todateEdit")
        self.todateEdit.setCalendarPopup(True)

        self.horizontalLayout.addWidget(self.todateEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tableView = QTableView(Movement)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)


        self.retranslateUi(Movement)

        QMetaObject.connectSlotsByName(Movement)
    # setupUi

    def retranslateUi(self, Movement):
        Movement.setWindowTitle(QCoreApplication.translate("Movement", u"Form", None))
        self.retButton.setText("")
        self.label_4.setText(QCoreApplication.translate("Movement", u"Inventory Movement", None))
        self.label.setText(QCoreApplication.translate("Movement", u"Filtering", None))
        self.label_2.setText(QCoreApplication.translate("Movement", u"From:", None))
        self.fromdateEdit.setDisplayFormat(QCoreApplication.translate("Movement", u"yyyy/MM/dd", None))
        self.label_3.setText(QCoreApplication.translate("Movement", u"To:", None))
        self.todateEdit.setDisplayFormat(QCoreApplication.translate("Movement", u"yyyy/MM/dd", None))
    # retranslateUi

