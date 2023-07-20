import sqlite3

import numpy as np
import pandas as pd

from Domain.chat_room import ChatRoom
from Domain.message import Message
from Domain.people._employee import Employee


class DBConnector:
    # ===================== BASIC ============================ #
    _instance = None
    SQL_PATH = r"../Back/table_creation.sql"

    def __new__(cls, test_option=False):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, test_option=False):
        self.conn = None
        self.test_option = test_option

    def start_conn(self):
        if self.test_option is False:
            self.conn = sqlite3.connect('../test/main_storage.db')
        else:
            self.conn = sqlite3.connect('../test/test_storage.db')
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
        if hasattr(object_, 'to_dict_for_insert'):
            key_words = object_.to_dict_for_insert().keys()
            keys = ','.join(key_words)
            values = object_.to_dict_for_insert()
        else:
            key_words = object_.__dict__.keys()
            keys = ','.join(object_.__dict__.keys())
            values = object_.__dict__

        colon_keys = ','.join([f':{x}' for x in key_words])
        # print('#key_words#',key_words)
        # print('#keys#',keys)
        # print('#values#',values)
        # print('#colon_keys#',colon_keys)
        pstmt = f'insert into {table_name} ({keys}) values ({colon_keys})'

        return pstmt, values

    def find_obj_by_id_and_table_name(self, obj_id, table_name, class_name):
        assert isinstance(obj_id, int) and isinstance(table_name, str)
        c = self.start_conn()
        fetched_row = c.execute(f'select * from {table_name} where {class_name}_id = {obj_id}').fetchone()
        self.end_conn()
        return fetched_row

    def find_all_by_table_name(self, table_name):
        assert isinstance(table_name, str)
        c = self.start_conn()
        fetched_row_list = c.execute(f'select * from {table_name}').fetchall()
        self.end_conn()
        return fetched_row_list

    # ================ CREATE TABLE ============================ #
    def create_tables(self):
        c = self.start_conn()
        pstmt = None
        with open(self.SQL_PATH, 'r', encoding='utf-8') as file:
            pstmt = file.read()
        if pstmt is None:
            raise 'sql문 못불러옴'
        c.executescript(pstmt)
        self.commit_db()
        self.end_conn()
        print('created_tables')

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
            return
        self.commit_db()
        row = c.execute('select * from tb_employee order by employee_id desc limit 1').fetchone()
        result = Employee(*row)
        self.end_conn()
        return result

    def find_employee_by_id(self, employee_id):
        fetched_row = self.find_obj_by_id_and_table_name(employee_id, "tb_employee", "employee")
        return Employee(*fetched_row)

    def find_all_employee(self):
        fetched_rows = self.find_all_by_table_name("tb_employee")
        result_list = list()
        for row in fetched_rows:
            result_list.append(Employee(*row))
        return result_list

    def assert_login_username_and_password(self, username, password):
        c = self.start_conn()
        fetched_row = c.execute(f'select * from tb_employee where login_username=? and login_password=?',
                                (f'{username}', f'{password}',)).fetchone()

        if fetched_row is None:
            return None
        return Employee(*fetched_row)
    # ================ DOCTOR / NURSE / ADMIN ============================ #
    def insert_doctor_job(self, employee, assigned_department_id):
        c = self.start_conn()
        c.execute(f'''insert into tb_doctor(employee_id, assigned_department_id)
            values (?, ?)''', (employee.employee_id, assigned_department_id,))
        self.commit_db()
        self.end_conn()

    def insert_nurse_job(self, employee, assigned_ward_id):
        c = self.start_conn()
        c.execute(f'''insert into tb_nurse(employee_id, assigned_ward_id)
                    values (?, ?)''', (employee.employee_id, assigned_ward_id,))
        self.commit_db()
        self.end_conn()

    def insert_admin_job(self, employee, assigned_part_id):
        c = self.start_conn()
        c.execute(f'''insert into tb_administration(employee_id, assigned_part_id)
                    values (?, ?)''', (employee.employee_id, assigned_part_id,))
        self.commit_db()
        self.end_conn()

    # ================ CHAT ROOM ============================ #
    def insert_chat_room(self, chat_room: ChatRoom):
        assert isinstance(chat_room, ChatRoom)
        c = self.start_conn()
        if chat_room.chat_room_id is None:
            # insert
            pstmt, values, = self.make_prepared_statement(chat_room, 'tb_chat_room')
            c.execute(pstmt, values)
        else:
            # todo: update 로직 필요하면 작성
            pass
        self.commit_db()
        row = c.execute('select * from tb_chat_room order by chat_room_id desc limit 1').fetchone()
        result = ChatRoom(*row)
        self.end_conn()
        return result

    def find_chat_room_by_id(self, chat_room_id):
        assert isinstance(chat_room_id, int)
        fetched_row = self.find_obj_by_id_and_table_name(chat_room_id, "tb_chat_room", "chat_room")
        # 관련 톡방 사용자(2명) list 가져오기
        employee_list = self.find_employees_by_chat_room_id(chat_room_id)
        # message_list 가져오기
        message_list = self.find_messages_by_chat_room_id(chat_room_id)

        return ChatRoom(*fetched_row, employee_list=employee_list, message_list=message_list)

    def find_employees_by_chat_room_id(self, chat_room_id):
        c = self.start_conn()
        fetched_rows = c.execute(f"""
            select * from tb_employee where employee_id in 
            (select employee_id from tb_employee_chat_room where chat_room_id = {chat_room_id})
        """).fetchall()
        result_list = list()
        for row in fetched_rows:
            result_list.append(Employee(*row))
        self.end_conn()
        return result_list

    # ================ EMPLOYEE CHAT ROOM ============================ #
    def insert_employee_chat_room(self, employee_id, chat_room_id):
        assert isinstance(employee_id, int) and isinstance(chat_room_id, int)
        c = self.start_conn()
        c.execute('insert into tb_employee_chat_room(employee_id, chat_room_id) values (?, ?)',
                  (employee_id, chat_room_id))
        self.commit_db()
        self.end_conn()

    # ================ MESSAGE ============================ #
    def insert_message(self, message: Message):
        assert isinstance(message, Message)
        c = self.start_conn()
        if message.message_id is None:
            # insert
            pstmt, values, = self.make_prepared_statement(message, 'tb_message')
            c.execute(pstmt, values)
        else:
            # todo: update 로직 필요하면 작성
            pass
        self.commit_db()
        row = c.execute('select * from tb_message order by message_id desc limit 1').fetchone()
        result = Message(*row)
        self.end_conn()
        return result

    def find_messages_by_message_id(self, message_id):
        c = self.start_conn()
        fetched_row = c.execute(f"""
            select * from tb_message where message_id = {message_id})
        """).fetchone()
        result = Message(*fetched_row)
        self.end_conn()
        return result

    def find_messages_by_chat_room_id(self, chat_room_id):
        c = self.start_conn()
        fetched_rows = c.execute(f"""
            select * from tb_message where message_id in 
            (select employee_id from tb_employee_chat_room where chat_room_id = {chat_room_id})
        """).fetchall()
        result_list = list()
        for row in fetched_rows:
            result_list.append(Message(*row))
        self.end_conn()
        return result_list

    def checked_message_by_chat_room_id(self, chat_room_id):
        c = self.start_conn()
        fetched_rows = c.execute(f"""
            update tb_message set "is_confirmed"=1 where message_id in 
            (select employee_id from tb_employee_chat_room where chat_room_id = {chat_room_id})
        """).fetchall()
        result_list = list()
        for row in fetched_rows:
            result_list.append(Message(*row))
        self.end_conn()
        return result_list


if __name__ == '__main__':
    conn = DBConnector(test_option=True)
    conn.create_tables()

    from data.insert_data_to_tables import *

    insert_KTAS_data(conn)
    insert_dummy_employee_data(conn, 30)
    insert_dummy_chat_room(conn, 30)
    insert_dummy_employee_chat_room_data(conn, 100, (1, 30), (1, 30))

    print(conn.find_employee_by_id(10))
    print(conn.find_messages_by_chat_room_id(10))
