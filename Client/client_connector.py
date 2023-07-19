from Common.class_common import Common


class Connector:
    def __init__(self):
        self.common = Common()
        self.controller = None
        self.login_employee = None



    def set_widget_controller(self, controller):
        self.controller = controller

