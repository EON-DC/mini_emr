from PyQt5 import QtWidgets

from Client.ui.compiled_ui_login_widget import Ui_LoginWidget


class WidgetLogin(QtWidgets.QWidget, Ui_LoginWidget):
    def __init__(self, ui_controller):
        super().__init__()
        self.setupUi(self)
        self.setUp()
        self.controller = ui_controller

    def reset(self):
        pass

    def setUp(self):
        self.le_login.setFocus()
        self.set_up_widgets_and_labels()
        self.set_up_triggers()

    def close(self):
        self.le_login.clear()
        self.le_pw.clear()
        super().close()

    def show(self):
        super().show()

    def set_up_widgets_and_labels(self):
        pass

    def set_up_triggers(self):
        self.btn_login.clicked.connect(lambda state: self.btn_login_clicked())
        self.le_login.returnPressed.connect(lambda: self.le_pw.setFocus())
        self.le_pw.returnPressed.connect(lambda: self.btn_login_clicked())

    def btn_login_clicked(self):
        username = self.le_login.text()
        pw = self.le_pw.text()
        self.controller.login_access(username, pw)
