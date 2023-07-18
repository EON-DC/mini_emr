from PyQt5 import QtWidgets

from Client.ui.compiled_ui_chat_room import Ui_ChatRoom


class WidgetChatRoom(QtWidgets.QMainWindow, Ui_ChatRoom):
    def __init__(self, ui_controller):
        super().__init__()
        self.setupUi(self)
        self.controller = ui_controller
