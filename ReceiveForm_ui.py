# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ReceiveForm.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTextEdit, QVBoxLayout, QWidget)
import resource_rc

class Ui_ReceiveForm(object):
    def setupUi(self, ReceiveForm):
        if not ReceiveForm.objectName():
            ReceiveForm.setObjectName(u"ReceiveForm")
        ReceiveForm.resize(991, 774)
        self.verticalLayout_2 = QVBoxLayout(ReceiveForm)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.retButton = QPushButton(ReceiveForm)
        self.retButton.setObjectName(u"retButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.retButton.sizePolicy().hasHeightForWidth())
        self.retButton.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/return.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.retButton.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.retButton)

        self.relButton = QPushButton(ReceiveForm)
        self.relButton.setObjectName(u"relButton")
        sizePolicy.setHeightForWidth(self.relButton.sizePolicy().hasHeightForWidth())
        self.relButton.setSizePolicy(sizePolicy)
        icon1 = QIcon()
        icon1.addFile(u":/arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.relButton.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.relButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label = QLabel(ReceiveForm)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label_3 = QLabel(ReceiveForm)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.RecEdit = QLineEdit(ReceiveForm)
        self.RecEdit.setObjectName(u"RecEdit")

        self.verticalLayout.addWidget(self.RecEdit)

        self.label_4 = QLabel(ReceiveForm)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.SendEdit = QLineEdit(ReceiveForm)
        self.SendEdit.setObjectName(u"SendEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.SendEdit.sizePolicy().hasHeightForWidth())
        self.SendEdit.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.SendEdit)

        self.label_5 = QLabel(ReceiveForm)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.dateEdit = QDateEdit(ReceiveForm)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setCalendarPopup(True)

        self.verticalLayout.addWidget(self.dateEdit)

        self.label_6 = QLabel(ReceiveForm)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.textEdit = QTextEdit(ReceiveForm)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy1.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.textEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.submitButton = QPushButton(ReceiveForm)
        self.submitButton.setObjectName(u"submitButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.submitButton.sizePolicy().hasHeightForWidth())
        self.submitButton.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.submitButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(ReceiveForm)

        QMetaObject.connectSlotsByName(ReceiveForm)
    # setupUi

    def retranslateUi(self, ReceiveForm):
        ReceiveForm.setWindowTitle(QCoreApplication.translate("ReceiveForm", u"Form", None))
        self.retButton.setText("")
        self.relButton.setText("")
        self.label.setText(QCoreApplication.translate("ReceiveForm", u"Receiving product", None))
        self.label_3.setText(QCoreApplication.translate("ReceiveForm", u"Enter the name of reciever*", None))
        self.label_4.setText(QCoreApplication.translate("ReceiveForm", u"Enter the name of sender*", None))
        self.label_5.setText(QCoreApplication.translate("ReceiveForm", u"choose the date of receiving products", None))
        self.dateEdit.setDisplayFormat(QCoreApplication.translate("ReceiveForm", u"yyyy/MM/dd", None))
        self.label_6.setText(QCoreApplication.translate("ReceiveForm", u"enter description if you want", None))
        self.submitButton.setText(QCoreApplication.translate("ReceiveForm", u"Submit", None))
    # retranslateUi

