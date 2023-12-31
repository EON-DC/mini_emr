# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_chat_room.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChatRoom(object):
    def setupUi(self, ChatRoom):
        ChatRoom.setObjectName("ChatRoom")
        ChatRoom.resize(380, 511)
        ChatRoom.setMinimumSize(QtCore.QSize(300, 500))
        self.centralwidget = QtWidgets.QWidget(ChatRoom)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget_3)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_employee_name = QtWidgets.QLabel(self.widget_3)
        self.label_employee_name.setObjectName("label_employee_name")
        self.horizontalLayout.addWidget(self.label_employee_name)
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_employee_department = QtWidgets.QLabel(self.widget_3)
        self.label_employee_department.setObjectName("label_employee_department")
        self.horizontalLayout.addWidget(self.label_employee_department)
        self.verticalLayout.addWidget(self.widget_3)
        self.plainTextEdit_chat = QtWidgets.QPlainTextEdit(self.widget)
        self.plainTextEdit_chat.setReadOnly(True)
        self.plainTextEdit_chat.setObjectName("plainTextEdit_chat")
        self.verticalLayout.addWidget(self.plainTextEdit_chat)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 90))
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_to_send = QtWidgets.QLineEdit(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_to_send.sizePolicy().hasHeightForWidth())
        self.lineEdit_to_send.setSizePolicy(sizePolicy)
        self.lineEdit_to_send.setMinimumSize(QtCore.QSize(250, 77))
        self.lineEdit_to_send.setMaximumSize(QtCore.QSize(16777215, 77))
        self.lineEdit_to_send.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lineEdit_to_send.setObjectName("lineEdit_to_send")
        self.horizontalLayout_2.addWidget(self.lineEdit_to_send)
        self.btn_to_send = QtWidgets.QPushButton(self.widget_4)
        self.btn_to_send.setMinimumSize(QtCore.QSize(75, 80))
        self.btn_to_send.setMaximumSize(QtCore.QSize(75, 80))
        self.btn_to_send.setObjectName("btn_to_send")
        self.horizontalLayout_2.addWidget(self.btn_to_send)
        self.verticalLayout.addWidget(self.widget_4)
        self.verticalLayout_2.addWidget(self.widget)
        ChatRoom.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ChatRoom)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 380, 21))
        self.menubar.setObjectName("menubar")
        ChatRoom.setMenuBar(self.menubar)

        self.retranslateUi(ChatRoom)
        QtCore.QMetaObject.connectSlotsByName(ChatRoom)

    def retranslateUi(self, ChatRoom):
        _translate = QtCore.QCoreApplication.translate
        ChatRoom.setWindowTitle(_translate("ChatRoom", "실시간 대화방"))
        self.label.setText(_translate("ChatRoom", "대화상대"))
        self.label_employee_name.setText(_translate("ChatRoom", "김연아"))
        self.label_3.setText(_translate("ChatRoom", "소속"))
        self.label_employee_department.setText(_translate("ChatRoom", "내과"))
        self.plainTextEdit_chat.setPlainText(_translate("ChatRoom", ">박광현 (나) : IC-1번 김철수님 NRS 6점 chest pain이요.\n"
">김연아 (상대) : 처방낼게요."))
        self.btn_to_send.setText(_translate("ChatRoom", "전송"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ChatRoom = QtWidgets.QMainWindow()
    ui = Ui_ChatRoom()
    ui.setupUi(ChatRoom)
    ChatRoom.show()
    sys.exit(app.exec_())
