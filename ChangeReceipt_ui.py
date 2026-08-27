# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ChangeReceipt.ui'
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
    QLabel, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import resource_rc

class Ui_ChangeReceipt(object):
    def setupUi(self, ChangeReceipt):
        if not ChangeReceipt.objectName():
            ChangeReceipt.setObjectName(u"ChangeReceipt")
        ChangeReceipt.resize(1448, 740)
        self.verticalLayout = QVBoxLayout(ChangeReceipt)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.retButton = QPushButton(ChangeReceipt)
        self.retButton.setObjectName(u"retButton")
        icon = QIcon()
        icon.addFile(u":/return.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.retButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.retButton)

        self.relButton = QPushButton(ChangeReceipt)
        self.relButton.setObjectName(u"relButton")
        icon1 = QIcon()
        icon1.addFile(u":/arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.relButton.setIcon(icon1)

        self.horizontalLayout.addWidget(self.relButton)

        self.label = QLabel(ChangeReceipt)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalLayout.setStretch(2, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(ChangeReceipt)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(ChangeReceipt)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(ChangeReceipt)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.fromdateEdit = QDateEdit(ChangeReceipt)
        self.fromdateEdit.setObjectName(u"fromdateEdit")
        self.fromdateEdit.setCalendarPopup(True)

        self.horizontalLayout_2.addWidget(self.fromdateEdit)

        self.label_4 = QLabel(ChangeReceipt)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.todateEdit = QDateEdit(ChangeReceipt)
        self.todateEdit.setObjectName(u"todateEdit")
        self.todateEdit.setCalendarPopup(True)

        self.horizontalLayout_2.addWidget(self.todateEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.tableWidget = QTableWidget(ChangeReceipt)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)


        self.retranslateUi(ChangeReceipt)

        QMetaObject.connectSlotsByName(ChangeReceipt)
    # setupUi

    def retranslateUi(self, ChangeReceipt):
        ChangeReceipt.setWindowTitle(QCoreApplication.translate("ChangeReceipt", u"Form", None))
        self.retButton.setText("")
        self.relButton.setText("")
        self.label.setText(QCoreApplication.translate("ChangeReceipt", u"Editing receipts", None))
        self.label_5.setText(QCoreApplication.translate("ChangeReceipt", u"Notice that you can only edit description", None))
        self.label_2.setText(QCoreApplication.translate("ChangeReceipt", u"Filtering", None))
        self.label_3.setText(QCoreApplication.translate("ChangeReceipt", u"From:", None))
        self.fromdateEdit.setDisplayFormat(QCoreApplication.translate("ChangeReceipt", u"yyyy/MM/dd", None))
        self.label_4.setText(QCoreApplication.translate("ChangeReceipt", u"To:", None))
        self.todateEdit.setDisplayFormat(QCoreApplication.translate("ChangeReceipt", u"yyyy/MM/dd", None))
    # retranslateUi

