# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NewWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_NewWindow(object):
    def setupUi(self, NewWindow):
        if not NewWindow.objectName():
            NewWindow.setObjectName(u"NewWindow")
        NewWindow.resize(956, 716)
        self.verticalLayout_2 = QVBoxLayout(NewWindow)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.retButton = QPushButton(NewWindow)
        self.retButton.setObjectName(u"retButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.retButton.sizePolicy().hasHeightForWidth())
        self.retButton.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/return.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.retButton.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.retButton)

        self.relButton = QPushButton(NewWindow)
        self.relButton.setObjectName(u"relButton")
        sizePolicy.setHeightForWidth(self.relButton.sizePolicy().hasHeightForWidth())
        self.relButton.setSizePolicy(sizePolicy)
        icon1 = QIcon()
        icon1.addFile(u":/arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.relButton.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.relButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.label_5 = QLabel(NewWindow)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 5)
        self.horizontalLayout_3.setStretch(3, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label = QLabel(NewWindow)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.label)

        self.nameLine = QLineEdit(NewWindow)
        self.nameLine.setObjectName(u"nameLine")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.nameLine.sizePolicy().hasHeightForWidth())
        self.nameLine.setSizePolicy(sizePolicy3)

        self.verticalLayout.addWidget(self.nameLine)

        self.label_2 = QLabel(NewWindow)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.label_2)

        self.codeLine = QLineEdit(NewWindow)
        self.codeLine.setObjectName(u"codeLine")

        self.verticalLayout.addWidget(self.codeLine)

        self.label_3 = QLabel(NewWindow)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.label_3)

        self.priceLine = QLineEdit(NewWindow)
        self.priceLine.setObjectName(u"priceLine")
        sizePolicy3.setHeightForWidth(self.priceLine.sizePolicy().hasHeightForWidth())
        self.priceLine.setSizePolicy(sizePolicy3)

        self.verticalLayout.addWidget(self.priceLine)

        self.label_4 = QLabel(NewWindow)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.label_4)

        self.stockLine = QLineEdit(NewWindow)
        self.stockLine.setObjectName(u"stockLine")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.stockLine.sizePolicy().hasHeightForWidth())
        self.stockLine.setSizePolicy(sizePolicy4)

        self.verticalLayout.addWidget(self.stockLine)

        self.submitButton = QPushButton(NewWindow)
        self.submitButton.setObjectName(u"submitButton")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.submitButton.sizePolicy().hasHeightForWidth())
        self.submitButton.setSizePolicy(sizePolicy5)
        self.submitButton.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout.addWidget(self.submitButton, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2.setStretch(2, 1)

        self.retranslateUi(NewWindow)

        QMetaObject.connectSlotsByName(NewWindow)
    # setupUi

    def retranslateUi(self, NewWindow):
        NewWindow.setWindowTitle(QCoreApplication.translate("NewWindow", u"Form", None))
        self.retButton.setText("")
        self.relButton.setText("")
        self.label_5.setText(QCoreApplication.translate("NewWindow", u"Fill these gaps to add new product", None))
        self.label.setText(QCoreApplication.translate("NewWindow", u"Enter the name of product*", None))
        self.label_2.setText(QCoreApplication.translate("NewWindow", u"Enter the barcode of product*", None))
        self.label_3.setText(QCoreApplication.translate("NewWindow", u"Enter the price of product*", None))
        self.label_4.setText(QCoreApplication.translate("NewWindow", u"Enter the minimum stock of product", None))
        self.submitButton.setText(QCoreApplication.translate("NewWindow", u"submit", None))
    # retranslateUi

