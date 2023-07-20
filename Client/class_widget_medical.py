from PyQt5 import QtWidgets

from Client.ui.compiled_ui_medical_widget import Ui_MedicalWindow


class WidgetMedical(QtWidgets.QMainWindow, Ui_MedicalWindow):
    def __init__(self, ui_controller):
        super().__init__()
        self.setupUi(self)
        self.controller = ui_controller

    def reset(self):
        pass

    def setUp(self):
        self.set_up_widgets_and_labels()

    def close(self):
        pass

    def show(self):
        self.setUp()
        super().show()

    def set_up_widgets_and_labels(self):
        pass