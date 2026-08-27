# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dashboard.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QPushButton, QSizePolicy,
    QSpacerItem, QTableView, QVBoxLayout, QWidget)
import resource_rc

class Ui_Dashboard(object):
    def setupUi(self, Dashboard):
        if not Dashboard.objectName():
            Dashboard.setObjectName(u"Dashboard")
        Dashboard.resize(1137, 747)
        self.verticalLayout_2 = QVBoxLayout(Dashboard)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_5 = QLabel(Dashboard)
        self.label_5.setObjectName(u"label_5")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_5)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.label = QLabel(Dashboard)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.verticalLayout_5.addWidget(self.label)

        self.newButton = QPushButton(Dashboard)
        self.newButton.setObjectName(u"newButton")
        sizePolicy1.setHeightForWidth(self.newButton.sizePolicy().hasHeightForWidth())
        self.newButton.setSizePolicy(sizePolicy1)

        self.verticalLayout_5.addWidget(self.newButton)

        self.recButton = QPushButton(Dashboard)
        self.recButton.setObjectName(u"recButton")

        self.verticalLayout_5.addWidget(self.recButton)

        self.sellButton = QPushButton(Dashboard)
        self.sellButton.setObjectName(u"sellButton")
        sizePolicy1.setHeightForWidth(self.sellButton.sizePolicy().hasHeightForWidth())
        self.sellButton.setSizePolicy(sizePolicy1)

        self.verticalLayout_5.addWidget(self.sellButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.label_2 = QLabel(Dashboard)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)

        self.verticalLayout_5.addWidget(self.label_2)

        self.overButton = QPushButton(Dashboard)
        self.overButton.setObjectName(u"overButton")
        sizePolicy1.setHeightForWidth(self.overButton.sizePolicy().hasHeightForWidth())
        self.overButton.setSizePolicy(sizePolicy1)

        self.verticalLayout_5.addWidget(self.overButton)

        self.movButton = QPushButton(Dashboard)
        self.movButton.setObjectName(u"movButton")
        sizePolicy1.setHeightForWidth(self.movButton.sizePolicy().hasHeightForWidth())
        self.movButton.setSizePolicy(sizePolicy1)

        self.verticalLayout_5.addWidget(self.movButton)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_4)

        self.label_6 = QLabel(Dashboard)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_5.addWidget(self.label_6)

        self.PchanButton = QPushButton(Dashboard)
        self.PchanButton.setObjectName(u"PchanButton")

        self.verticalLayout_5.addWidget(self.PchanButton)

        self.RchanButton = QPushButton(Dashboard)
        self.RchanButton.setObjectName(u"RchanButton")

        self.verticalLayout_5.addWidget(self.RchanButton)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)


        self.gridLayout.addLayout(self.verticalLayout_5, 0, 1, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(Dashboard)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setPixmap(QPixmap(u":/signal2.jpg"))

        self.horizontalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(Dashboard)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.lowstockTable = QTableView(Dashboard)
        self.lowstockTable.setObjectName(u"lowstockTable")

        self.verticalLayout_3.addWidget(self.lowstockTable)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 1)

        self.verticalLayout.addLayout(self.gridLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Dashboard)

        QMetaObject.connectSlotsByName(Dashboard)
    # setupUi

    def retranslateUi(self, Dashboard):
        Dashboard.setWindowTitle(QCoreApplication.translate("Dashboard", u"Form", None))
        self.label_5.setText(QCoreApplication.translate("Dashboard", u"WELCOME TO WAREHOUSE MANAGMENT", None))
        self.label.setText(QCoreApplication.translate("Dashboard", u"Goods and products", None))
        self.newButton.setText(QCoreApplication.translate("Dashboard", u"Add new product", None))
        self.recButton.setText(QCoreApplication.translate("Dashboard", u"Goods Receiving", None))
        self.sellButton.setText(QCoreApplication.translate("Dashboard", u"Goods Issue", None))
        self.label_2.setText(QCoreApplication.translate("Dashboard", u"Reporting", None))
        self.overButton.setText(QCoreApplication.translate("Dashboard", u"Inventory overview", None))
        self.movButton.setText(QCoreApplication.translate("Dashboard", u"Inventory Movement", None))
        self.label_6.setText(QCoreApplication.translate("Dashboard", u"Editing receipts or products", None))
        self.PchanButton.setText(QCoreApplication.translate("Dashboard", u"Edit product", None))
        self.RchanButton.setText(QCoreApplication.translate("Dashboard", u"Edit receipt", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("Dashboard", u"Low stock Budget", None))
    # retranslateUi

