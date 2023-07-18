import datetime
import time

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QPoint, Qt, pyqtSignal

from Client.class_widget_admin import WidgetAdmin
from Client.class_widget_chat_room import WidgetChatRoom
from Client.class_widget_dashboard import WidgetDashBoard
from Client.class_widget_employee_finder import WidgetEmployeeFinder
from Client.class_widget_login import WidgetLogin
from Client.class_widget_medical import WidgetMedical
from Client.client_connector import Connector


class WidgetController(QtWidgets.QWidget):
    # signal 클래스 변수
    assert_same_id_signal = pyqtSignal(bool)

    def __init__(self, connector=Connector):
        assert isinstance(connector, Connector)
        super().__init__()
        self.connector = connector  # db연결 인스턴스
        self.connector.set_widget(self)
        self.widget_admin = None
        self.widget_chat_room = None
        self.widget_dashboard = None
        self.widget_e_finder = None
        self.widget_login = None
        self.widget_medical = None

        self.setUp()

    def run(self):
        self.show()

    def reset(self):
        pass

    def setUp(self):
        self.set_up_widgets()

    def close(self):
        pass

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

    @staticmethod
    def clear_widget(widget):
        if widget.layout() is not None:
            while widget.layout().count() > 0:
                item = widget.layout().takeAt(0)
                if item.widget():
                    item.widget().deleteLater()
