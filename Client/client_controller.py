import datetime
import time

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QPoint, Qt, pyqtSignal
from PyQt5.QtWidgets import QMessageBox

from Client.class_widget_admin import WidgetAdmin
from Client.class_widget_chat_room import WidgetChatRoom
from Client.class_widget_dashboard import WidgetDashBoard
from Client.class_widget_employee_finder import WidgetEmployeeFinder
from Client.class_widget_login import WidgetLogin
from Client.class_widget_medical import WidgetMedical
from Client.client_connector import Connector
from Common.class_common import Common
from Domain.people._employee import Employee


class WidgetController(QtWidgets.QWidget):
    command_signal = pyqtSignal(str, object)

    def __init__(self, connector=Connector):
        assert isinstance(connector, Connector)
        super().__init__()
        self.connector = connector  # client 연결
        self.connector.set_widget_controller(self)
        self.widget_admin = None
        self.widget_chat_room = None
        self.widget_dashboard = None
        self.widget_e_finder = None
        self.widget_login = None
        self.widget_medical = None
        self.common = None
        self.setUp()

    def login_access(self, username, pw):
        self.connector.send_login_dto(username, pw)

    def run(self):
        self.show()


    def reset(self):
        pass

    def setUp(self):
        self.common = Common()
        self.set_up_widgets()
        self.set_up_triggers()

    def disconnect_server(self):
        self.connector.disconnect()

    def show(self):
        # self.widget_admin.show()
        # self.widget_chat_room.show()
        # self.widget_dashboard.show()
        # self.widget_e_finder.show()
        self.widget_login.show()
        # self.widget_medical.show()

    def set_up_widgets(self):
        self.widget_admin = WidgetAdmin(self)
        self.widget_chat_room = WidgetChatRoom(self)
        self.widget_dashboard = WidgetDashBoard(self)
        self.widget_e_finder = WidgetEmployeeFinder(self)
        self.widget_login = WidgetLogin(self)
        self.widget_medical = WidgetMedical(self)

    def set_up_triggers(self):
        self.command_signal.connect(self.signal_handler)

    def get_all_employee(self):
        return self.connector.all_employee_list
    def get_patient_list(self):
        return self.connector.patient_table_widget_list

    def signal_handler(self, command_str, return_data_obj):
        if command_str == self.common.LOGIN_ACCESS_RES:
            if return_data_obj != self.common.FALSE:
                self.show_success_login()
            else:
                return QMessageBox.about(self.widget_login, "로그인 실패", "로그인 정보를 다시 확인해주세요.")
        elif command_str == self.common.PATIENT_NAMELIST_RES:
            self.widget_medical.refresh_patient_list_table_view(return_data_obj)
        elif command_str == self.common.PATIENT_RES:
            self.widget_medical.refresh_patient_info(return_data_obj)
        elif command_str == self.common.EMERGENCY_NURSE_RECORD_RES:
            self.widget_medical.refresh_emergency_nurse_record_info(return_data_obj)

    def open_chat_room_with_employee(self, employee:Employee):
        self.widget_chat_room:WidgetChatRoom
        self.connector.send_chat_room_request_with_employee(employee)


    def show_success_login(self):
        # login 창 닫기
        self.widget_login.close()
        # 윈도우 타이틀 설정
        employee = self.connector.get_login_employee()
        self.widget_medical: WidgetMedical
        if employee.type_job == 1:
            title = self.widget_medical.windowTitle() + " --- " + employee.name + '의사 의료통합정보 체계 로그인'
            self.widget_medical.setWindowTitle(title)
            self.widget_medical.show()
        elif employee.type_job == 2:
            title = self.widget_medical.windowTitle() + " --- " + employee.name + '간호사 의료통합정보 체계 로그인'
            self.widget_medical.setWindowTitle(title)
            self.widget_medical.show()
        else:
            title = self.widget_admin.windowTitle() + " --- " + employee.name + '의료통합정보 체계 로그인'
            self.widget_admin.setWindowTitle(title)
            self.widget_admin.show()

    @staticmethod
    def clear_widget(widget):
        if widget.layout() is not None:
            while widget.layout().count() > 0:
                item = widget.layout().takeAt(0)
                if item.widget():
                    item.widget().deleteLater()


    def show_employee_finder_widget(self):
        self.widget_e_finder.show()

    def show_chat_room_widget(self):
        self.widget_chat_room.show()