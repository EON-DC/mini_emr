from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from Client.ui.compiled_ui_employee_finder import Ui_EmployeeFinder
from Domain.people._employee import Employee


class WidgetEmployeeFinder(QtWidgets.QWidget,Ui_EmployeeFinder ):
    def __init__(self,ui_controller):
        super().__init__()
        self.setupUi(self)
        self.controller = ui_controller
        self.setUp()

    def reset(self):
        pass

    def setUp(self):
        self.set_trigger()

    def close(self):
        super().close()
    def show(self):
        self.refresh_employee_list_table()
        super().show()

    def set_trigger(self):
        self.table_widget_employee_list.cellDoubleClicked.connect(
            lambda row, col: self.open_chat_room(row))

    def open_chat_room(self, row):
        selected_employee = self.controller.get_all_employee()[row]
        self.controller.open_chat_room_with_employee(selected_employee)

    def refresh_employee_list_table(self):
        employee_list = self.controller.get_all_employee()
        table = self.table_widget_employee_list
        while table.rowCount():
            table.removeRow(0)
        table.setRowCount(len(employee_list))
        for row, data in enumerate(employee_list):
            data:Employee
            table.setItem(row, 0, QTableWidgetItem(f"{data.name}"))
            table.setItem(row, 1, QTableWidgetItem(f"{data.get_job()}"))
            table.setItem(row, 2, QTableWidgetItem(f"{data.mobile_phone_num_1}"))
