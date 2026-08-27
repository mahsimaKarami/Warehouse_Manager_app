# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Exitproduct.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import resource_rc

class Ui_Exitproduct(object):
    def setupUi(self, Exitproduct):
        if not Exitproduct.objectName():
            Exitproduct.setObjectName(u"Exitproduct")
        Exitproduct.resize(1383, 751)
        self.verticalLayout_5 = QVBoxLayout(Exitproduct)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.homeButton = QPushButton(Exitproduct)
        self.homeButton.setObjectName(u"homeButton")
        icon = QIcon()
        icon.addFile(u":/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.homeButton.setIcon(icon)

        self.horizontalLayout_10.addWidget(self.homeButton)

        self.retButton = QPushButton(Exitproduct)
        self.retButton.setObjectName(u"retButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.retButton.sizePolicy().hasHeightForWidth())
        self.retButton.setSizePolicy(sizePolicy)
        icon1 = QIcon()
        icon1.addFile(u":/return.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.retButton.setIcon(icon1)

        self.horizontalLayout_10.addWidget(self.retButton)

        self.relButton = QPushButton(Exitproduct)
        self.relButton.setObjectName(u"relButton")
        sizePolicy.setHeightForWidth(self.relButton.sizePolicy().hasHeightForWidth())
        self.relButton.setSizePolicy(sizePolicy)
        icon2 = QIcon()
        icon2.addFile(u":/arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.relButton.setIcon(icon2)

        self.horizontalLayout_10.addWidget(self.relButton)

        self.label_2 = QLabel(Exitproduct)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_2)

        self.horizontalLayout_10.setStretch(3, 1)

        self.verticalLayout_5.addLayout(self.horizontalLayout_10)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableWidget = QTableWidget(Exitproduct)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)

        self.label_3 = QLabel(Exitproduct)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)


        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.comboBox = QComboBox(Exitproduct)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEditable(True)

        self.verticalLayout_4.addWidget(self.comboBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.horizontalLayout_5.addLayout(self.verticalLayout_4)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.submitButton = QPushButton(Exitproduct)
        self.submitButton.setObjectName(u"submitButton")
        sizePolicy.setHeightForWidth(self.submitButton.sizePolicy().hasHeightForWidth())
        self.submitButton.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.submitButton)

        self.AddButton = QPushButton(Exitproduct)
        self.AddButton.setObjectName(u"AddButton")
        sizePolicy.setHeightForWidth(self.AddButton.sizePolicy().hasHeightForWidth())
        self.AddButton.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.AddButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.verticalLayout_3.setStretch(0, 1)

        self.verticalLayout_5.addLayout(self.verticalLayout_3)


        self.retranslateUi(Exitproduct)

        QMetaObject.connectSlotsByName(Exitproduct)
    # setupUi

    def retranslateUi(self, Exitproduct):
        Exitproduct.setWindowTitle(QCoreApplication.translate("Exitproduct", u"Form", None))
        self.homeButton.setText("")
        self.retButton.setText("")
        self.relButton.setText("")
        self.label_2.setText(QCoreApplication.translate("Exitproduct", u"Issuing the products from the warehouse", None))
        self.label_3.setText(QCoreApplication.translate("Exitproduct", u"Total price: ", None))
        self.submitButton.setText(QCoreApplication.translate("Exitproduct", u"submit", None))
        self.AddButton.setText(QCoreApplication.translate("Exitproduct", u"Add to table", None))
    # retranslateUi

