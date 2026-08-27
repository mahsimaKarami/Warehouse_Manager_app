# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Overview.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTableView, QVBoxLayout,
    QWidget)
import resource_rc

class Ui_Overview(object):
    def setupUi(self, Overview):
        if not Overview.objectName():
            Overview.setObjectName(u"Overview")
        Overview.resize(948, 791)
        self.verticalLayout_2 = QVBoxLayout(Overview)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.retButton = QPushButton(Overview)
        self.retButton.setObjectName(u"retButton")
        icon = QIcon()
        icon.addFile(u":/return.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.retButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.retButton)

        self.label = QLabel(Overview)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(Overview)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.tableView = QTableView(Overview)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Overview)

        QMetaObject.connectSlotsByName(Overview)
    # setupUi

    def retranslateUi(self, Overview):
        Overview.setWindowTitle(QCoreApplication.translate("Overview", u"Form", None))
        self.retButton.setText("")
        self.label.setText(QCoreApplication.translate("Overview", u"Inventory overview", None))
        self.label_2.setText(QCoreApplication.translate("Overview", u"All product's details", None))
    # retranslateUi

