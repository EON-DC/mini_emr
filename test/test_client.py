import sys

from PyQt5.QtWidgets import QApplication

from Client.client_connector import Connector
from Client.client_controller import WidgetController
from Common.class_common import Common

if __name__ == '__main__':
    common = Common()
    app = QApplication(sys.argv)
    client_connector = Connector()
    client_controller = WidgetController(client_connector)
    client_controller.run()
    sys.excepthook = lambda exctype, value, traceback: common.show_error_message(str(value), traceback)
    sys.exit(app.exec_())
