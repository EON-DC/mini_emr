import time

from PyQt5 import QtWidgets

from Client.ui.compiled_ui_chat_room import Ui_ChatRoom
from Domain.chat_room import ChatRoom


class WidgetChatRoom(QtWidgets.QMainWindow, Ui_ChatRoom):
    def __init__(self, ui_controller):
        super().__init__()
        self.setupUi(self)
        self.controller = ui_controller
        self.setUp()

    def reset(self):
        pass

    def setUp(self):
        self.lineEdit_to_send.returnPressed.connect(lambda :self.send_message())
        self.btn_to_send.clicked.connect(lambda state: self.send_message())
    def send_message(self):
        msg_str = self.lineEdit_to_send.text()
        self.lineEdit_to_send.clear()
        self.controller.send_message_to_connect(msg_str)
    def close(self):
        super().close()

    def show(self):
        self.refresh_plain_text()
        super().show()

    def refresh_plain_text(self):
        time.sleep(0.2)
        selected_employee = self.controller.connector.selected_employee
        e_index = self.controller.connector.all_employee_list.index(selected_employee)
        if selected_employee is not None:
            self.label_employee_name.setText(selected_employee.name)
            self.label_employee_department.setText(self.controller.connector.all_employee_department[e_index])
        chat_room = self.controller.connector.selected_chat_room
        chat_room:ChatRoom
        if chat_room.chat_room_id is not None:
            self.plainTextEdit_chat.clear()
            lines = self.controller.connector.get_messages_as_string(chat_room.chat_room_id)
            if len(lines) != 0:
                self.plainTextEdit_chat.appendPlainText("\n".join(lines))

