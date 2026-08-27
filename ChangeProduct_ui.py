# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ChangeProduct.ui'
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
    QLabel, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import resource_rc

class Ui_ChangeProduct(object):
    def setupUi(self, ChangeProduct):
        if not ChangeProduct.objectName():
            ChangeProduct.setObjectName(u"ChangeProduct")
        ChangeProduct.resize(937, 718)
        self.verticalLayout_2 = QVBoxLayout(ChangeProduct)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.retButton = QPushButton(ChangeProduct)
        self.retButton.setObjectName(u"retButton")
        icon = QIcon()
        icon.addFile(u":/return.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.retButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.retButton)

        self.relButton = QPushButton(ChangeProduct)
        self.relButton.setObjectName(u"relButton")
        icon1 = QIcon()
        icon1.addFile(u":/arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.relButton.setIcon(icon1)

        self.horizontalLayout.addWidget(self.relButton)

        self.label = QLabel(ChangeProduct)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalLayout.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(ChangeProduct)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(ChangeProduct)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(ChangeProduct)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.comboBox = QComboBox(ChangeProduct)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEditable(True)

        self.verticalLayout.addWidget(self.comboBox)

        self.tableWidget = QTableWidget(ChangeProduct)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(ChangeProduct)

        QMetaObject.connectSlotsByName(ChangeProduct)
    # setupUi

    def retranslateUi(self, ChangeProduct):
        ChangeProduct.setWindowTitle(QCoreApplication.translate("ChangeProduct", u"Form", None))
        self.retButton.setText("")
        self.relButton.setText("")
        self.label.setText(QCoreApplication.translate("ChangeProduct", u"Editing products", None))
        self.label_2.setText(QCoreApplication.translate("ChangeProduct", u"All product's details", None))
        self.label_3.setText(QCoreApplication.translate("ChangeProduct", u"For Editing barcode,price or minimum stock just double click on cell", None))
        self.label_4.setText(QCoreApplication.translate("ChangeProduct", u"For finding special product, Use combo box", None))
    # retranslateUi

