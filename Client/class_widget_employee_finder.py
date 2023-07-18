from PyQt5 import QtWidgets

from Client.ui.compiled_ui_employee_finder import Ui_EmployeeFinder


class WidgetEmployeeFinder(QtWidgets.QWidget,Ui_EmployeeFinder ):
    def __init__(self,ui_controller):
        super().__init__()
        self.setupUi(self)
        self.controller = ui_controller
