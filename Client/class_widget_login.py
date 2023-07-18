from PyQt5 import QtWidgets

from Client.ui.compiled_ui_login_widget import Ui_LoginWidget


class WidgetLogin(QtWidgets.QWidget, Ui_LoginWidget):
    def __init__(self, ui_controller):
        super().__init__()
        self.setupUi(self)
        self.controller = ui_controller
