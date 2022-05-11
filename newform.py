# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'myFirsTryRSHYcH.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QGridLayout, QCheckBox, QLabel, QDateEdit, QToolBox, QRadioButton, QFormLayout, \
    QTableWidget, QHBoxLayout, QTableView
from PyQt5.QtCore import QRect, Qt, QMetaObject, QCoreApplication


# from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
#     QMetaObject, QObject, QPoint, QRect,
#     QSize, QTime, QUrl, Qt)
# from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
#     QFont, QFontDatabase, QGradient, QIcon,
#     QImage, QKeySequence, QLinearGradient, QPainter,
#     QPalette, QPixmap, QRadialGradient, QTransform)
# from PySide6.QtWidgets import (QApplication, QCheckBox, QDateEdit, QFormLayout,
#     QFrame, QGridLayout, QHBoxLayout, QHeaderView,
#     QLabel, QRadioButton, QSizePolicy, QTableView,
#     QTableWidget, QTableWidgetItem, QToolBox, QWidget)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(480, 670)
        self.gridLayoutWidget = QWidget(Frame)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(59, 29, 369, 281))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.checkBox = QCheckBox(self.gridLayoutWidget)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout.addWidget(self.checkBox, 1, 1, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setTextFormat(Qt.AutoText)
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label.setMargin(5)
        self.label.setIndent(5)
        self.label.setOpenExternalLinks(False)
        self.label.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout.addWidget(self.label, 1, 2, 1, 1)

        self.dateEdit = QDateEdit(self.gridLayoutWidget)
        self.dateEdit.setObjectName(u"dateEdit")

        self.gridLayout.addWidget(self.dateEdit, 0, 2, 1, 1)

        self.toolBox = QToolBox(self.gridLayoutWidget)
        self.toolBox.setObjectName(u"toolBox")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 69, 166))
        self.toolBox.addItem(self.page, u"Page 1")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 69, 166))
        self.toolBox.addItem(self.page_2, u"Page 2")

        self.gridLayout.addWidget(self.toolBox, 1, 0, 1, 1)

        self.radioButton = QRadioButton(self.gridLayoutWidget)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout.addWidget(self.radioButton, 2, 1, 1, 1)

        self.formLayoutWidget = QWidget(Frame)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(79, 359, 291, 171))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.formLayoutWidget)
        self.tableWidget.setObjectName(u"tableWidget")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.tableWidget)

        self.horizontalLayoutWidget = QWidget(Frame)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(39, 570, 391, 80))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.tableView = QTableView(self.horizontalLayoutWidget)
        self.tableView.setObjectName(u"tableView")

        self.horizontalLayout.addWidget(self.tableView)


        self.retranslateUi(Frame)

        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.checkBox.setText(QCoreApplication.translate("Frame", u"CheckBox", None))
        self.label.setText(QCoreApplication.translate("Frame", u"Conspiracy theories, Russia and us", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("Frame", u"Page 1", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("Frame", u"Page 2", None))
        self.radioButton.setText(QCoreApplication.translate("Frame", u"RadioButton", None))
    # retranslateUi

