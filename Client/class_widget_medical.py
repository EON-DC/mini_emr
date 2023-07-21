from PyQt5 import QtWidgets, QtGui

from Client.ui.compiled_ui_medical_widget import Ui_MedicalWindow
from Domain.emergency_nurse_record import EmergencyNurseRecord
from Domain.people.patient import Patient


class WidgetMedical(QtWidgets.QMainWindow, Ui_MedicalWindow):
    def __init__(self, ui_controller):
        super().__init__()
        self.setupUi(self)
        self.controller = ui_controller

    def reset(self):
        pass

    def setUp(self):
        self.set_up_widgets_and_labels()

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.controller.disconnect_server()


    def show(self):
        self.setUp()
        super().show()

    def set_up_widgets_and_labels(self):
        self.tableWidget_patient_list.setColumnWidth(0, 20)
        self.tableWidget_patient_list.setColumnWidth(1, 70)
        self.tableWidget_patient_list.setColumnWidth(2, 100)
        self.tableWidget_patient_list.setColumnWidth(3, 70)
        self.btn_chat_open.clicked.connect(lambda state:self.controller.show_employee_finder_widget())

    def refresh_emergency_nurse_record_info(self, emergency_nurse_record:EmergencyNurseRecord):
        enr = emergency_nurse_record
        self.label_cheif_complain.setText(enr.cheif_complain)
        self.plain_text_edit_memo.clear()
        self.plain_text_edit_memo.appendPlainText(enr.memo)
        self.label_register_timestamp.setText(enr.saved_time)

    def refresh_patient_info(self, patient_obj=None):
        if patient_obj is not None:
            patient = patient_obj
        else:
            patient = self.controller.selected_patient()
        assert isinstance(patient, Patient)
        self.label_patient_name.setText(f"{patient.get_name_and_age()}\n{patient.register_number}")

    def refresh_assigned_doctor_name(self, doctor_name=None):
        if doctor_name is None:
            self.label_assigned_doctor_name.setText("")
        else:
            self.label_assigned_doctor_name.setText(doctor_name)

    def refresh_memo(self, memo=None):
        if memo is None:
            self.plain_text_edit_memo.setText("")
        else:
            self.plain_text_edit_memo.setText(memo)

    def refresh_ktas_grade(self, ktas):
        self.label_ktas_code.setText(ktas.ktas_code)
        self.label_ktas_grade.setText(f"{ktas.final_grade}")

    def refresh_medical_order_info(self, medical_nurse_record):
        self.label_cheif_complain.setText(medical_nurse_record.cheif_complain)

    def refresh_patient_list_table_view(self, return_data_obj=None):
        table = self.tableWidget_patient_list
        while table.rowCount():
            table.removeRow(0)
        if return_data_obj is not None:
            patient_list = return_data_obj
        else:
            patient_list = self.controller.get_patient_list()

        row_count = len(patient_list)
        col_count = 4

        table.setRowCount(row_count)
        for row, p in enumerate(patient_list):
            for col in range(col_count):
                table.setItem(row, col, QtWidgets.QTableWidgetItem(str(p[col])))


