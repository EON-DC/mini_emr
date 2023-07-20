import random
import re
import sqlite3

from Back.db_connector import DBConnector
from Domain.chat_room import ChatRoom
from Domain.ktas import KTAS
from Domain.message import Message
from Domain.people._employee import Employee
from Common.fake_data_maker import FakeDataMaker


def insert_KTAS_data(conn):
    second_category_name_set = set()
    third_category_name_set = set()
    fourth_category_name_set = set()

    whole_data = None

    with open("../data/emergency_grade.txt", 'r', encoding='utf-8') as file:
        whole_data = file.read()

    if whole_data is None:
        raise '파일 못읽음'

    lines = whole_data.split('\n')

    result_list = list()
    for row in lines:
        word_list = row.split(' ')
        temp_list = list()

        slice_index = -1
        for i, w in enumerate(word_list):
            if len(w) == 1:
                slice_index = i
                break
        for w in word_list[:slice_index]:
            temp_list.append(word_list.pop(0))

        if slice_index == -1:
            raise '못자르고 있음'

        second_category_name = ','.join(temp_list)
        second_category_name_set.add(second_category_name)  ## 세트 추가
        second_category_code = word_list.pop(0)
        temp_list.clear()

        while not re.match(r"[A-Z]", word_list[0]):
            temp_list.append(word_list.pop(0))
        third_category_name = ' '.join(temp_list)
        third_category_name_set.add(third_category_name)  ## 세트 추가
        third_category_code = word_list.pop(0)
        temp_list.clear()

        while not re.match(r"[A-Z]{2}", word_list[0]):
            temp_list.append(word_list.pop(0))

        fourth_category_name = ' '.join(temp_list)
        fourth_category_name_set.add(fourth_category_name)  ## 세트 추가
        fourth_category_code = word_list.pop(0)
        temp_list.clear()

        final_grade = int(word_list.pop())
        ktas_code = ''.join(['A', second_category_code, third_category_code, fourth_category_code])
        result_list.append(
            KTAS('성인', 'A', second_category_name, second_category_code, third_category_name, third_category_code,
                 fourth_category_name, fourth_category_code, final_grade, ktas_code))

    with open("../data/child_grade.txt", 'r', encoding='utf-8') as file:
        whole_data = file.read()

    if whole_data is None:
        raise '파일 못읽음'

    lines = whole_data.split('\n')

    for row in lines:
        word_list = row.split(' ')
        temp_list = list()

        slice_index = -1
        for i, w in enumerate(word_list):
            if len(w) == 1:
                slice_index = i
                break
        for w in word_list[:slice_index]:
            temp_list.append(word_list.pop(0))

        if slice_index == -1:
            raise '못자르고 있음'

        second_category_name = ','.join(temp_list)
        second_category_name_set.add(second_category_name)  ## 세트 추가
        second_category_code = word_list.pop(0)
        temp_list.clear()

        while not re.match(r"[A-Z]", word_list[0]):
            temp_list.append(word_list.pop(0))
        third_category_name = ' '.join(temp_list)
        third_category_name_set.add(third_category_name)  ## 세트 추가
        third_category_code = word_list.pop(0)
        temp_list.clear()

        while not re.match(r"[A-Z]{2}", word_list[0]):
            temp_list.append(word_list.pop(0))

        fourth_category_name = ' '.join(temp_list)
        fourth_category_name_set.add(fourth_category_name)  ## 세트 추가
        fourth_category_code = word_list.pop(0)
        temp_list.clear()

        final_grade = int(word_list.pop())
        ktas_code = ''.join(['B', second_category_code, third_category_code, fourth_category_code])

        result_list.append(
            KTAS('소아', 'B', second_category_name, second_category_code, third_category_name, third_category_code,
                 fourth_category_name, fourth_category_code, final_grade, ktas_code))

    c = conn.start_conn()
    # first_category_name
    # first_category_code
    # second_category_name
    # second_category_code
    # third_category_name
    # third_category_code
    # fourth_category_name
    # fourth_category_code
    # final_grade
    for i in result_list:
        c.execute('''INSERT INTO tb_ktas (first_category_name, first_category_code, second_category_name,
         second_category_code, third_category_name, third_category_code,
         fourth_category_name, fourth_category_code, final_grade, ktas_code)
         VALUES (
         :first_category_name, 
         :first_category_code, 
         :second_category_name,
         :second_category_code,
         :third_category_name, 
         :third_category_code, 
         :fourth_category_name,
         :fourth_category_code,
         :final_grade,
         :ktas_code);''', i.__dict__)
    conn.commit_db()
    conn.end_conn()


def insert_dummy_employee_data(conn: DBConnector, size):
    # 우선 내 거 하나
    conn.insert_employee(Employee(None, "박광현", 2, "qwer11", "1234", "010-1010-0102", "010-0215-1335"))
    maker = FakeDataMaker()
    for i in range(size):
        # 가짜 생성
        name = maker.get_random_fake_name()
        type_job = maker.get_random_type_job()
        login_username = maker.get_random_login_id()
        login_pw = "1234"
        phone_1 = maker.get_random_phone_num()
        phone_2 = maker.get_random_phone_num()
        # 객체화 및 입력
        dummy_employee = Employee(None, name, type_job, login_username, login_pw, phone_1, phone_2)
        dummy_employee = conn.insert_employee(dummy_employee)
        if dummy_employee.type_job == 1:
            conn.insert_doctor_job(dummy_employee, random.randint(1, 6))
        elif dummy_employee.type_job == 2:
            conn.insert_nurse_job(dummy_employee, random.randint(7, 12))
        elif dummy_employee.type_job == 3:
            conn.insert_admin_job(dummy_employee, random.randint(13, 14))
def insert_dummy_chat_room(conn: DBConnector, size):
    maker = FakeDataMaker()
    for i in range(size):
        # 가짜 생성
        # 객체화 및 입력
        random_date = maker.get_random_date_time_str()
        dummy_chat_room = ChatRoom(None, random_date)
        conn.insert_chat_room(dummy_chat_room)


def insert_dummy_employee_chat_room_data(conn: DBConnector, size, employee_range, chat_range):
    maker = FakeDataMaker()
    min_id_employee, max_id_employee = employee_range
    min_id_chat, max_id_chat = chat_range
    for i in range(size):
        # 가짜 생성
        # 객체화 및 입력
        random_employee_id_1, random_employee_id_2 = random.sample(range(min_id_employee, max_id_employee), 2)
        random_chat_room_id = random.randint(min_id_chat, max_id_chat)
        conn.insert_employee_chat_room(random_employee_id_1, random_chat_room_id)
        conn.insert_employee_chat_room(random_employee_id_2, random_chat_room_id)
        for _ in range(random.randint(1, 10)):
            # 가짜 생성
            # 객체화 및 입력
            dummy_message_1 = Message(None, random_employee_id_1, random_chat_room_id, maker.get_random_lorem(), False)
            dummy_message_2 = Message(None, random_employee_id_2, random_chat_room_id, maker.get_random_lorem(), False)
            conn.insert_message(dummy_message_1)
            conn.insert_message(dummy_message_2)


def insert_dummy_message_data(conn: DBConnector, size, employee_range, chat_range):
    maker = FakeDataMaker()
    min_id_employee, max_id_employee = employee_range
    min_id_chat, max_id_chat = chat_range
    for i in range(size):
        # 가짜 생성
        # 객체화 및 입력
        random_employee_id = random.randint(min_id_employee, max_id_employee)
        random_chat_room_id = random.randint(min_id_chat, max_id_chat)
        dummy_message = Message(None, random_employee_id, random_chat_room_id, maker.get_random_lorem(), False)
        conn.insert_message(dummy_message)
