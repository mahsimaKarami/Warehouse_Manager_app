# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Detail.ui'
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

class Ui_Detail(object):
    def setupUi(self, Detail):
        if not Detail.objectName():
            Detail.setObjectName(u"Detail")
        Detail.resize(971, 782)
        self.verticalLayout = QVBoxLayout(Detail)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.retButton = QPushButton(Detail)
        self.retButton.setObjectName(u"retButton")
        icon = QIcon()
        icon.addFile(u":/return.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.retButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.retButton)

        self.mainlabel = QLabel(Detail)
        self.mainlabel.setObjectName(u"mainlabel")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.mainlabel.setFont(font)
        self.mainlabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.mainlabel)

        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.RecSenlabel = QLabel(Detail)
        self.RecSenlabel.setObjectName(u"RecSenlabel")

        self.verticalLayout.addWidget(self.RecSenlabel)

        self.tydalabel = QLabel(Detail)
        self.tydalabel.setObjectName(u"tydalabel")

        self.verticalLayout.addWidget(self.tydalabel)

        self.Desclabel = QLabel(Detail)
        self.Desclabel.setObjectName(u"Desclabel")

        self.verticalLayout.addWidget(self.Desclabel)

        self.tableView = QTableView(Detail)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)

        self.totallabel = QLabel(Detail)
        self.totallabel.setObjectName(u"totallabel")

        self.verticalLayout.addWidget(self.totallabel)


        self.retranslateUi(Detail)

        QMetaObject.connectSlotsByName(Detail)
    # setupUi

    def retranslateUi(self, Detail):
        Detail.setWindowTitle(QCoreApplication.translate("Detail", u"Form", None))
        self.retButton.setText("")
        self.mainlabel.setText(QCoreApplication.translate("Detail", u"Factors's detail", None))
        self.RecSenlabel.setText(QCoreApplication.translate("Detail", u"TextLabel", None))
        self.tydalabel.setText(QCoreApplication.translate("Detail", u"TextLabel", None))
        self.Desclabel.setText(QCoreApplication.translate("Detail", u"TextLabel", None))
        self.totallabel.setText(QCoreApplication.translate("Detail", u"TextLabel", None))
    # retranslateUi

