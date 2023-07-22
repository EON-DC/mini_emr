import datetime
import sqlite3

import numpy as np
import pandas as pd

from Domain.chat_room import ChatRoom
from Domain.emergency_nurse_record import EmergencyNurseRecord
from Domain.message import Message
from Domain.people._employee import Employee
from Domain.people.patient import Patient


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

    def find_all_employee_department(self):
        all_employee_list = self.find_all_employee()
        c = self.start_conn()
        result_list = list()
        for e in all_employee_list:
            name = None
            if e.type_job == 1:
                name = c.execute(f"""
                    select name from tb_department where department_id = 
                        (select assigned_department_id from tb_doctor where employee_id = {e.employee_id})
                """).fetchone()
            elif e.type_job ==2:
                name = c.execute(f"""
                    select name from tb_department where department_id = 
                        (select assigned_ward_id from tb_nurse where employee_id = {e.employee_id})
                """).fetchone()
            elif e.type_job ==3:
                name = c.execute(f"""
                    select name from tb_department where department_id = 
                        (select assigned_part_id from tb_administration where employee_id = {e.employee_id})
                """).fetchone()

            if name is None:
                name = "-"
            else:
                name = name[0]
            result_list.append(name)
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

    def find_doctor_name_by_doctor_id(self, doctor_id):
        c = self.start_conn()
        fetched_row = c.execute(f"""
            select name from tb_employee where employee_id =
                (select employee_id from tb_doctor where doctor_id = ?)
        """, (doctor_id, )).fetchone()
        if fetched_row is not None:
            result = fetched_row[0]
        else:
            result = ''
        self.end_conn()
        return result

    def find_nurse_name_by_nurse_id(self, nurse_id):
        c = self.start_conn()
        fetched_row = c.execute(f"""
            select name from tb_employee where employee_id =
                (select employee_id from tb_nurse where nurse_id = ?)
        """, (nurse_id, )).fetchone()
        if fetched_row is not None:
            result = fetched_row[0]
        else:
            result = ''
        self.end_conn()
        return result

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

    def create_chat_room(self, login_employee_id, request_employee_id):
        c = self.start_conn()
        now_time_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        c.execute(f"""
            insert into tb_chat_room(created_time) values (?)
        """, (f"{now_time_str}",))
        self.commit_db()
        last_index = c.execute(f"""
            select chat_room_id from tb_chat_room order by chat_room_id desc limit 1
        """).fetchone()
        if last_index is None:
            raise 'insert 실패'
        last_index = last_index[0]

        c.executescript(f"""
            insert into tb_employee_chat_room(chat_room_id,employee_id) 
                values ({last_index}, {login_employee_id}),
                        ({last_index}, {request_employee_id});
        """)
        self.commit_db()
        self.end_conn()
        return last_index

    def find_chat_room_by_two_employee_id(self, login_employee_id, request_employee_id):
        assert isinstance(login_employee_id, int) and isinstance(request_employee_id, int)
        c = self.start_conn()
        login_employee_chat_room_list = set()
        request_employee_chat_room_list = set()

        fetched_row = c.execute(f"""
            select chat_room_id from tb_employee_chat_room where employee_id = {login_employee_id}   
        """).fetchall()
        for i in fetched_row:
            login_employee_chat_room_list.update(i)

        fetched_row = c.execute(f"""
                    select chat_room_id from tb_employee_chat_room where employee_id = {request_employee_id}   
                """).fetchall()
        for i in fetched_row:
            request_employee_chat_room_list.update(i)

        intersection_chat_room_set = login_employee_chat_room_list.intersection(request_employee_chat_room_list)
        if len(intersection_chat_room_set) == 0:
            intersection_chat_room_id = self.create_chat_room(login_employee_id, request_employee_id)
        else:
            intersection_chat_room_id= intersection_chat_room_set.pop()
        print("intersection_chat_room_id: ", intersection_chat_room_id)
        return intersection_chat_room_id


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

    # ================ EmergencyNurseRecord ============================ #
    def find_emergency_nurse_record_by_register_id(self, register_id):
        c = self.start_conn()
        fetched_row = c.execute("""
            select * from tb_emergency_nurse_record where register_id = ?
        """, (register_id,)).fetchone()
        if fetched_row is not None:
            return EmergencyNurseRecord(*fetched_row)
        return None
    # ================ patient ============================ #
    def find_all_patient(self):
        fetched_rows = self.find_all_by_table_name("tb_patient")
        result_list = list()
        for row in fetched_rows:
            result_list.append(Patient(*row))
        return result_list

    def find_patient_by_bed_id(self, bed_id):
        c = self.start_conn()
        fetched_row = c.execute("""
            select * from tb_patient where using_bed_id = ?
        """, (bed_id, )).fetchone()
        if fetched_row is not None:
            return Patient(*fetched_row)
        return None


    def find_bed_id_and_name_list_by_employee_id(self, employee_id):
        c = self.start_conn()

        job_code = self.find_employee_by_id(employee_id).type_job
        table_name = ''
        if job_code == 1:
            table_name = 'tb_doctor'
            col_name  = 'assigned_department_id'
        elif  job_code == 2:
            table_name = 'tb_nurse'
            col_name = 'assigned_ward_id'
        else:
            table_name = 'tb_admin'
            col_name = 'assigned_part_id'

        fetched_rows = c.execute(f"""
            select bed_id, viewing_bed_name from tb_bed_of_ward 
                where assigned_ward_id = 
                (select {col_name} from {table_name} where employee_id =?)
        """, (employee_id,)).fetchall()

        bed_id_list = list()
        name_list = list()

        for row in fetched_rows:
            bed_id_list.append(row[0])
            name_list.append(row[1])

        self.end_conn()
        return bed_id_list, name_list

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
            select * from tb_message where chat_room_id = ?
        """, (chat_room_id, )).fetchall()
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
    # bed_id_list, name_list, = conn.find_bed_id_and_name_list_by_employee_id(1)
    # for i in bed_id_list:
    #     print(conn.find_patient_by_bed_id(i))
    conn.create_chat_room(1, 11)

    # conn.create_tables()

    # from data.insert_data_to_tables import *
    #
    # insert_KTAS_data(conn)
    # insert_dummy_employee_data(conn, 30)
    # insert_dummy_chat_room(conn, 30)
    # insert_dummy_employee_chat_room_data(conn, 100, (1, 30), (1, 30))
    #
    # print(conn.find_employee_by_id(10))
    # print(conn.find_messages_by_chat_room_id(10))

