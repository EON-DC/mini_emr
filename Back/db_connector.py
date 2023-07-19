import sqlite3

import numpy as np
import pandas as pd

from Domain.people._employee import Employee


class DBConnector:
    # ===================== BASIC ============================ #
    _instance = None
    SQL_PATH = r"table_creation.sql"

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

    @staticmethod
    def make_prepared_statement(object_, table_name):
        keys = ','.join(object_.__dict__.keys())
        colon_keys = ','.join([f':{x}' for x in object_.__dict__.keys()])
        pstmt = f'insert into {table_name} ({keys}) values ({colon_keys})'
        values = object_.__dict__
        return pstmt, values

    def find_obj_by_id_and_table_name(self, obj_id, table_name, class_name):
        assert isinstance(obj_id, int) and isinstance(table_name, str)
        c = self.start_conn()
        fetched_row = c.execute(f'select * from {table_name} where {class_name}_id = {obj_id}').fetchone()
        self.end_conn()
        return fetched_row

    # ================ CREATE TABLE ============================ #
    def create_tables(self):
        c = self.start_conn()
        pstmt = None
        with open(self.SQL_PATH, 'r') as file:
            pstmt = file.read()
        if pstmt is None:
            raise 'sql문 못불러옴'
        c.executescript(pstmt)
        self.commit_db()
        self.end_conn()

    # ===================== DOMAIN ============================ #
    # ================ EMPLOYEE ============================ #
    def insert_employee(self, employee: Employee):
        assert isinstance(employee, Employee)
        c = self.start_conn()
        if employee.employee_id is None:
            # insert
            pstmt, values, = self.make_prepared_statement(employee, 'tb_employee')
            c.execute(pstmt, values)
        else:
            # todo: update 로직 필요하면 작성
            pass
        self.commit_db()
        row = c.execute('select * from tb_employee order by employee_id asc limit 1').fetchone()
        result = Employee(*row)
        self.end_conn()
        return result

    def find_employee_by_id(self, employee_id):
        fetched_row = self.find_obj_by_id_and_table_name(employee_id, "tb_employee", "employee")
        return Employee(*fetched_row)


if __name__ == '__main__':
    conn = DBConnector(test_option=True)
    conn.create_tables()

    from data.insert_data_to_tables import *

    insert_KTAS_data(conn)
    insert_employee_data(conn, 30)

