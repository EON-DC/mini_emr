# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_medical_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MedicalWindow(object):
    def setupUi(self, MedicalWindow):
        MedicalWindow.setObjectName("MedicalWindow")
        MedicalWindow.resize(1062, 860)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MedicalWindow.sizePolicy().hasHeightForWidth())
        MedicalWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MedicalWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.verticalLayout.addWidget(self.line_11)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.widget_3)
        self.widget.setMaximumSize(QtCore.QSize(300, 16777215))
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.line_12 = QtWidgets.QFrame(self.widget)
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.horizontalLayout_4.addWidget(self.line_12)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setMaximumSize(QtCore.QSize(90, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.label_22 = QtWidgets.QLabel(self.widget)
        self.label_22.setMinimumSize(QtCore.QSize(200, 0))
        self.label_22.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_4.addWidget(self.label_22)
        self.line_13 = QtWidgets.QFrame(self.widget)
        self.line_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.horizontalLayout_4.addWidget(self.line_13)
        self.horizontalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.widget_3)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.pushButton_10 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_3.addWidget(self.pushButton_10)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_3.addWidget(self.pushButton_6)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.pushButton_8 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_3.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_3.addWidget(self.pushButton_9)
        self.pushButton_7 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_3.addWidget(self.pushButton_7)
        self.horizontalLayout.addWidget(self.widget_2)
        self.line_14 = QtWidgets.QFrame(self.widget_3)
        self.line_14.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.horizontalLayout.addWidget(self.line_14)
        self.verticalLayout.addWidget(self.widget_3)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.line_3 = QtWidgets.QFrame(self.widget_4)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_2.addWidget(self.line_3)
        self.label_7 = QtWidgets.QLabel(self.widget_4)
        self.label_7.setMinimumSize(QtCore.QSize(60, 0))
        self.label_7.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.widget_4)
        self.label_8.setMinimumSize(QtCore.QSize(100, 0))
        self.label_8.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.line_5 = QtWidgets.QFrame(self.widget_4)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout_2.addWidget(self.line_5)
        self.label_9 = QtWidgets.QLabel(self.widget_4)
        self.label_9.setMinimumSize(QtCore.QSize(60, 0))
        self.label_9.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_2.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.widget_4)
        self.label_10.setMinimumSize(QtCore.QSize(150, 0))
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        self.line_6 = QtWidgets.QFrame(self.widget_4)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.horizontalLayout_2.addWidget(self.line_6)
        self.label_15 = QtWidgets.QLabel(self.widget_4)
        self.label_15.setMinimumSize(QtCore.QSize(60, 0))
        self.label_15.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_2.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(self.widget_4)
        self.label_16.setMinimumSize(QtCore.QSize(30, 0))
        self.label_16.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_2.addWidget(self.label_16)
        self.line_7 = QtWidgets.QFrame(self.widget_4)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.horizontalLayout_2.addWidget(self.line_7)
        self.label_18 = QtWidgets.QLabel(self.widget_4)
        self.label_18.setMinimumSize(QtCore.QSize(60, 0))
        self.label_18.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_2.addWidget(self.label_18)
        self.label_19 = QtWidgets.QLabel(self.widget_4)
        self.label_19.setMinimumSize(QtCore.QSize(40, 0))
        self.label_19.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_2.addWidget(self.label_19)
        self.line_8 = QtWidgets.QFrame(self.widget_4)
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.horizontalLayout_2.addWidget(self.line_8)
        self.label_3 = QtWidgets.QLabel(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.line_9 = QtWidgets.QFrame(self.widget_4)
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.horizontalLayout_2.addWidget(self.line_9)
        self.label_11 = QtWidgets.QLabel(self.widget_4)
        self.label_11.setMinimumSize(QtCore.QSize(60, 0))
        self.label_11.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_2.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.widget_4)
        self.label_12.setMinimumSize(QtCore.QSize(80, 0))
        self.label_12.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_2.addWidget(self.label_12)
        self.line_10 = QtWidgets.QFrame(self.widget_4)
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.horizontalLayout_2.addWidget(self.line_10)
        self.label_13 = QtWidgets.QLabel(self.widget_4)
        self.label_13.setMinimumSize(QtCore.QSize(60, 0))
        self.label_13.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_2.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.widget_4)
        self.label_14.setMinimumSize(QtCore.QSize(40, 0))
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_2.addWidget(self.label_14)
        self.line_4 = QtWidgets.QFrame(self.widget_4)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_2.addWidget(self.line_4)
        self.verticalLayout.addWidget(self.widget_4)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.widget_7 = QtWidgets.QWidget(self.centralwidget)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.widget_5 = QtWidgets.QWidget(self.widget_7)
        self.widget_5.setMaximumSize(QtCore.QSize(250, 16777215))
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 10)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_11 = QtWidgets.QWidget(self.widget_5)
        self.widget_11.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_11.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_11.setObjectName("widget_11")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_11)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label = QtWidgets.QLabel(self.widget_11)
        self.label.setMinimumSize(QtCore.QSize(100, 0))
        self.label.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_9.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem)
        self.btn_refresh_patient_list = QtWidgets.QPushButton(self.widget_11)
        self.btn_refresh_patient_list.setObjectName("btn_refresh_patient_list")
        self.horizontalLayout_9.addWidget(self.btn_refresh_patient_list)
        self.verticalLayout_2.addWidget(self.widget_11)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.widget_5)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 3, item)
        self.verticalLayout_2.addWidget(self.tableWidget_2)
        self.widget_12 = QtWidgets.QWidget(self.widget_5)
        self.widget_12.setMinimumSize(QtCore.QSize(0, 60))
        self.widget_12.setMaximumSize(QtCore.QSize(16777215, 60))
        self.widget_12.setObjectName("widget_12")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_12)
        self.verticalLayout_4.setContentsMargins(0, 5, 0, 5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.widget_12)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.line_15 = QtWidgets.QFrame(self.widget_12)
        self.line_15.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.verticalLayout_4.addWidget(self.line_15)
        self.label_17 = QtWidgets.QLabel(self.widget_12)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_4.addWidget(self.label_17)
        self.verticalLayout_2.addWidget(self.widget_12)
        self.plain_text_edit_memo = QtWidgets.QPlainTextEdit(self.widget_5)
        self.plain_text_edit_memo.setMinimumSize(QtCore.QSize(0, 200))
        self.plain_text_edit_memo.setMaximumSize(QtCore.QSize(16777215, 200))
        self.plain_text_edit_memo.setObjectName("plain_text_edit_memo")
        self.verticalLayout_2.addWidget(self.plain_text_edit_memo)
        self.widget_13 = QtWidgets.QWidget(self.widget_5)
        self.widget_13.setObjectName("widget_13")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.widget_13)
        self.horizontalLayout_11.setContentsMargins(0, 5, 0, 0)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem1 = QtWidgets.QSpacerItem(172, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem1)
        self.pushButton_12 = QtWidgets.QPushButton(self.widget_13)
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_11.addWidget(self.pushButton_12)
        self.verticalLayout_2.addWidget(self.widget_13)
        self.horizontalLayout_7.addWidget(self.widget_5)
        self.line_16 = QtWidgets.QFrame(self.widget_7)
        self.line_16.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.horizontalLayout_7.addWidget(self.line_16)
        self.widget_6 = QtWidgets.QWidget(self.widget_7)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_10 = QtWidgets.QWidget(self.widget_6)
        self.widget_10.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_10.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_10)
        self.horizontalLayout_8.setContentsMargins(0, 0, 5, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_5 = QtWidgets.QLabel(self.widget_10)
        self.label_5.setMinimumSize(QtCore.QSize(60, 0))
        self.label_5.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.label_21 = QtWidgets.QLabel(self.widget_10)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_8.addWidget(self.label_21)
        self.pushButton_11 = QtWidgets.QPushButton(self.widget_10)
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_8.addWidget(self.pushButton_11)
        self.verticalLayout_3.addWidget(self.widget_10)
        self.listWidget = QtWidgets.QListWidget(self.widget_6)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.verticalLayout_3.addWidget(self.listWidget)
        self.horizontalLayout_7.addWidget(self.widget_6)
        self.verticalLayout.addWidget(self.widget_7)
        self.widget_8 = QtWidgets.QWidget(self.centralwidget)
        self.widget_8.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_8.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.widget_9 = QtWidgets.QWidget(self.widget_8)
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.widget_9)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(self.widget_9)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.horizontalLayout_6.addWidget(self.widget_9)
        self.verticalLayout.addWidget(self.widget_8)
        MedicalWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MedicalWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1062, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MedicalWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MedicalWindow)
        QtCore.QMetaObject.connectSlotsByName(MedicalWindow)

    def retranslateUi(self, MedicalWindow):
        _translate = QtCore.QCoreApplication.translate
        MedicalWindow.setWindowTitle(_translate("MedicalWindow", "응급의료기록"))
        self.pushButton_2.setText(_translate("MedicalWindow", "실시간 챗"))
        self.label_22.setText(_translate("MedicalWindow", "메세지가 도착하였습니다"))
        self.pushButton_3.setText(_translate("MedicalWindow", "중증도분류"))
        self.pushButton_10.setText(_translate("MedicalWindow", "검사결과"))
        self.pushButton_6.setText(_translate("MedicalWindow", "입실기록"))
        self.pushButton_4.setText(_translate("MedicalWindow", "처치/재료"))
        self.pushButton_5.setText(_translate("MedicalWindow", "식사신청"))
        self.pushButton.setText(_translate("MedicalWindow", "간호기록"))
        self.pushButton_8.setText(_translate("MedicalWindow", "Flowsheet"))
        self.pushButton_9.setText(_translate("MedicalWindow", "간호분류"))
        self.pushButton_7.setText(_translate("MedicalWindow", "퇴실신청"))
        self.label_7.setText(_translate("MedicalWindow", "선택환자:"))
        self.label_8.setText(_translate("MedicalWindow", "김아무개(M/55)"))
        self.label_9.setText(_translate("MedicalWindow", "주호소:"))
        self.label_10.setText(_translate("MedicalWindow", "가슴이 답답해요."))
        self.label_15.setText(_translate("MedicalWindow", "중증도:"))
        self.label_16.setText(_translate("MedicalWindow", "1"))
        self.label_18.setText(_translate("MedicalWindow", "KTAS:"))
        self.label_19.setText(_translate("MedicalWindow", "ICBA"))
        self.label_11.setText(_translate("MedicalWindow", "접수시간"))
        self.label_12.setText(_translate("MedicalWindow", "07/18 15:33"))
        self.label_13.setText(_translate("MedicalWindow", "체류시간"))
        self.label_14.setText(_translate("MedicalWindow", "02:22"))
        self.label.setText(_translate("MedicalWindow", "재실환자리스트"))
        self.btn_refresh_patient_list.setText(_translate("MedicalWindow", "Refresh"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MedicalWindow", "번호"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MedicalWindow", "환자(나이)"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MedicalWindow", "담당의/간호사"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MedicalWindow", "진행상황"))
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        item = self.tableWidget_2.item(0, 0)
        item.setText(_translate("MedicalWindow", "IC-1"))
        item = self.tableWidget_2.item(0, 1)
        item.setText(_translate("MedicalWindow", "김철수(M/55)"))
        item = self.tableWidget_2.item(0, 2)
        item.setText(_translate("MedicalWindow", "김순재/조운"))
        item = self.tableWidget_2.item(0, 3)
        item.setText(_translate("MedicalWindow", "접수중"))
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)
        self.label_6.setText(_translate("MedicalWindow", "1명 입실중 "))
        self.label_17.setText(_translate("MedicalWindow", " 간호메모"))
        self.plain_text_edit_memo.setPlainText(_translate("MedicalWindow", "- 보호자 대기(-) / 연락(+)\n"
"- Chest Pain NRS 6점 -> noti(+) /처방(-)\n"
"- ECG: ST Elevation r/o ischemic HF"))
        self.pushButton_12.setText(_translate("MedicalWindow", "저장"))
        self.label_5.setText(_translate("MedicalWindow", "처방화면"))
        self.label_21.setText(_translate("MedicalWindow", "추가처방"))
        self.pushButton_11.setText(_translate("MedicalWindow", "Refresh"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MedicalWindow", "1. check v/s q 1hr"))
        item = self.listWidget.item(1)
        item.setText(_translate("MedicalWindow", "2. restrict ABR"))
        item = self.listWidget.item(2)
        item.setText(_translate("MedicalWindow", "3. Total NPO"))
        item = self.listWidget.item(3)
        item.setText(_translate("MedicalWindow", "4. f/u BST q 6hr"))
        item = self.listWidget.item(5)
        item.setText(_translate("MedicalWindow", "====== 수액 ========"))
        item = self.listWidget.item(6)
        item.setText(_translate("MedicalWindow", "1. NS 1L/bag   100ml/hr"))
        item = self.listWidget.item(8)
        item.setText(_translate("MedicalWindow", "====== PO ========"))
        item = self.listWidget.item(9)
        item.setText(_translate("MedicalWindow", "1. Clopidrogel 300mg  6Tab"))
        item = self.listWidget.item(10)
        item.setText(_translate("MedicalWindow", "2. Tigagreller 180mg 1Tab 둘 다 지금 복용해주세요"))
        item = self.listWidget.item(12)
        item.setText(_translate("MedicalWindow", "====== Text Order ========="))
        item = self.listWidget.item(13)
        item.setText(_translate("MedicalWindow", "보호자 대기 시켜주세요"))
        item = self.listWidget.item(15)
        item.setText(_translate("MedicalWindow", "===== PCI Order ==========="))
        item = self.listWidget.item(16)
        item.setText(_translate("MedicalWindow", "...."))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("MedicalWindow", "현재 시각"))
        self.label_4.setText(_translate("MedicalWindow", "2023-07-18 10:42"))
        self.menu.setTitle(_translate("MedicalWindow", "메뉴"))
        self.menu_2.setTitle(_translate("MedicalWindow", "검사"))
        self.menu_3.setTitle(_translate("MedicalWindow", "기록"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MedicalWindow = QtWidgets.QMainWindow()
    ui = Ui_MedicalWindow()
    ui.setupUi(MedicalWindow)
    MedicalWindow.show()
    sys.exit(app.exec_())