from PyQt5 import QtWidgets
from Client.ui.compiled_ui_admin_widget import Ui_AdminWindow


class WidgetAdmin(QtWidgets.QMainWindow, Ui_AdminWindow):
    def __init__(self, ui_controller):
        super().__init__()
        self.setupUi(self)
        self.controller = ui_controller
