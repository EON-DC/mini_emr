from datetime import datetime

from PyQt5 import QtWidgets


class Common:
    _instance = None

    START_OF_HEADER = chr(1)
    START_OF_TEXT = chr(2)
    END_OF_TEXT = chr(3)

    HOST = '127.0.0.1'
    PORT = 9999
    BUFFER = 50000
    FORMAT = "utf-8"
    HEADER_LENGTH = 30

    def __new__(cls):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        pass

    @staticmethod
    def show_error_message(message, traceback):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setIcon(QtWidgets.QMessageBox.Critical)
        msg_box.setWindowTitle("Error")
        msg_box.setText(message)
        msg_box.exec_()
        traceback.print_exc()

    @staticmethod
    def get_subtract_time(str_start_timestamp):
        try:
            parsed_datetime = datetime.strptime(str_start_timestamp, "%Y-%m-%d %H:%M:%S")
        except:
            return '알수 없는 시간'
        now_time = datetime.now()
        result_time_delta = now_time - parsed_datetime
        return f"{result_time_delta.min}"
    @staticmethod
    def get_now_time_str():
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
