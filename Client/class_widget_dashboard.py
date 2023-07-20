from PyQt5 import QtWidgets

from Client.ui.compiled_ui_dashboard import Ui_DashBoard


class WidgetDashBoard(QtWidgets.QMainWindow, Ui_DashBoard):
    def __init__(self,ui_controller):
        super().__init__()
        self.setupUi(self)
        self.controller = ui_controller

    def reset(self):
        pass

    def setUp(self):
        self.set_up_widgets()

    def close(self):
        pass

    def show(self):
        self.setUp()
        super().show()

    def set_up_widgets_and_labels(self):
        pass