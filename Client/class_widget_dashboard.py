from PyQt5 import QtWidgets

from Client.ui.compiled_ui_dashboard import Ui_DashBoard


class WidgetDashBoard(QtWidgets.QMainWindow, Ui_DashBoard):
    def __init__(self,ui_controller):
        super().__init__()
        self.setupUi(self)
        self.controller = ui_controller