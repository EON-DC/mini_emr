import sqlite3

import numpy as np
import pandas as pd


class DBConnector:
    # ===================== BASIC ============================ #
    _instance = None

    def __new__(cls, test_option=False):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, test_option=False):
        self.conn = None
        self.test_option = test_option

    def start_conn(self):
        if self.test_option is False:
            self.conn = sqlite3.connect('main_storage.db')
        else:
            self.conn = sqlite3.connect('test_storage.db')
        return self.conn.cursor()

    def end_conn(self):
        if self.conn is not None:
            self.conn.close()
            self.conn = None

    def commit_db(self):
        self.conn.commit()

    @staticmethod
    def set_pandas_configure():
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        pd.set_option('display.width', 1000)

    # ===================== DOMAIN ============================ #
    # ================ CREATE TABLE ============================ #
    # ================ EMPLOYEE ============================ #
    # ================ KTAS ============================ #
    # ================ EMERGENCY_NURSE_RECORD ============================ #
    # ================ CHAT_ROOM ============================ #
    # ================ EMPLOYEE_CHAT_ROOM ============================ #
    # ================ MESSAGE ============================ #
    # ================ BED OF WARD ============================ #
    # ================ DEPARTMENT ============================ #


if __name__ == '__main__':
    conn = DBConnector(test_option=True)

