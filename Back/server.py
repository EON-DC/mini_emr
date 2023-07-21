import time
import traceback
import socket
from threading import Thread

import select

from Back.db_connector import DBConnector
from Common.class_common import Common
from Common.class_json_converter import ObjDecoder, ObjEncoder
from Domain.dto.dto_class import DTOMaker
from Domain.people._employee import Employee


class EMRServer:
    def __init__(self, db_connector: DBConnector):
        self.db_conn = db_connector
        self.common = Common()

        self.server_socket = None
        self.sockets_list = list()
        self.clients = dict()
        self.thread_for_run = None
        self.run_signal = True

        self.decoder = ObjDecoder()
        self.encoder = ObjEncoder()

        self.dto_maker = DTOMaker()

    def start(self):
        if self.thread_for_run is not None:  # 실행중이면 종료 시키기
            return
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET(ipv4를 의미)
        self.server_socket.bind((self.common.HOST, self.common.PORT))  # 바인딩
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.listen()  # 리슨 시작
        self.sockets_list.clear()  # 소켓리스트 클리어
        self.sockets_list.append(self.server_socket)
        self.run_signal = True
        self.thread_for_run = Thread(target=self.run)
        self.thread_for_run.start()
        print('SERVER STARTED')

    def run(self):
        while True:
            if self.run_signal is False:
                break
            try:
                read_sockets, _, exception_sockets = select.select(self.sockets_list, [], self.sockets_list, 0.1)
            except Exception:
                continue
            for notified_socket in read_sockets:
                if notified_socket == self.server_socket:
                    client_socket, client_address = self.server_socket.accept()
                    print(client_address, '연결됨')
                    user = self.receive_message(client_socket)
                    if user is False:
                        continue
                    self.sockets_list.append(client_socket)
                    self.clients[client_socket] = user

                else:
                    message = self.receive_message(notified_socket)
                    print(message, '연결해제됨')
                    if message is False:
                        self.sockets_list.remove(notified_socket)
                        print(notified_socket, '연결해제됨')
                        del self.clients[notified_socket]

            for notified_socket in exception_sockets:
                self.sockets_list.remove(notified_socket)
                print(notified_socket, '오류로 연결해제됨')
                del self.clients[notified_socket]

    def send_message(self, client_socket: socket, header, data):
        assert isinstance(header, str) or isinstance(header, bytes)
        assert isinstance(data, str) or isinstance(data, bytes)
        if isinstance(header, bytes):
            header_to_sending = header.decode(self.common.FORMAT)
        else:
            header_to_sending = header
        if isinstance(data, bytes):
            data_to_sending = data.decode(self.common.FORMAT)
        else:
            data_to_sending = data

        message_to_send = f"{self.common.START_OF_TEXT}".join([header_to_sending, data_to_sending])
        if len(message_to_send) >= self.common.BUFFER:
            raise "부족한 버퍼 용량"
        message_to_send = f"{message_to_send:<{self.common.BUFFER}}"

        print(f"SERVER SENDED: (HEADER: {header} | DATA: {data})")
        client_socket.sendall(message_to_send.encode(self.common.FORMAT))

    def header_data_distributor(self, recv_encoded_message):
        decoded_message = recv_encoded_message.decode(self.common.FORMAT).strip()
        header, data_decoded_str, = decoded_message.split(self.common.START_OF_TEXT)
        data = self.decoder.binary_to_obj(data_decoded_str)
        return header, data

    def receive_message(self, client_socket: socket):
        while True:
            try:
                recv_encoded_message = client_socket.recv(self.common.BUFFER)
                if len(recv_encoded_message) < 3:
                    continue
                request_header, request_data = self.header_data_distributor(recv_encoded_message)
                print(f"SERVER RECEIVED: ({request_header},{request_data})")

            except Exception:
                traceback.print_exc()
                return False

            if request_header == self.common.LOGIN_ACCESS_REQ:
                username = request_data['login_username']
                password = request_data['password']
                login_employee = self.db_conn.assert_login_username_and_password(username, password)
                if login_employee is None:
                    self.send_message(client_socket, self.common.LOGIN_ACCESS_RES, self.common.FALSE)
                else:
                    # 로그인 성공 로직
                    # 회원 정보 보내기
                    data_str = self.encoder.toJSON_an_object(login_employee)
                    self.send_message(client_socket, self.common.LOGIN_ACCESS_RES, data_str)
                    # patient_list 보내기
                    # sample_patient_list = f"""{[("IC-1", "김철수(M/55)", "김순재/조운", "접수중"),
                    #                             ("IC-2", "관우(M/22)", "김순재/박사라", "접수중")]}"""
                    stored_patient_list = list()
                    patient_table_list = list()
                    bed_id_list, name_list, = self.db_conn.find_bed_id_and_name_list_by_employee_id(
                        login_employee.employee_id)
                    patient_list = list()
                    doctor_list = list()
                    state_list = list()

                    first_patient_index = -1
                    for idx, i in enumerate(bed_id_list):
                        temp = self.db_conn.find_patient_by_bed_id(i)
                        stored_patient_list.append(temp)
                        if temp is None:
                            patient_list.append('')
                            doctor_list.append('')
                            state_list.append('')
                        else:
                            if first_patient_index == -1:
                                first_patient_index = idx
                            patient_list.append(temp.get_name_and_age())
                            doctor_name = self.db_conn.find_doctor_name_by_doctor_id(temp.assigned_doctor_id)
                            nurse_name = self.db_conn.find_nurse_name_by_nurse_id(temp.assigned_nurse_id)
                            doctor_list.append(f"{doctor_name}/{nurse_name}")
                            state_list.append('접수중')

                    for row in zip(name_list, patient_list, doctor_list, state_list):
                        patient_table_list.append(row)
                    self.send_message(client_socket, self.common.PATIENT_NAMELIST_RES, f"{patient_table_list}")
                    print('first_patient_index:', first_patient_index)
                    # patient 보내기
                    if first_patient_index != -1:
                        self.send_message(client_socket, self.common.PATIENT_RES,
                                          f"{stored_patient_list[first_patient_index]}")
                        time.sleep(0.2)
                        # MEDICAL_ORDER_RES
                        emergency_nurse_record = self.db_conn.find_emergency_nurse_record_by_register_id(
                            stored_patient_list[first_patient_index].register_number)
                        self.send_message(client_socket, self.common.EMERGENCY_NURSE_RECORD_RES,
                                          f"{emergency_nurse_record}")
                    # patient 보내기
                    employee_list = self.db_conn.find_all_employee()
                    self.send_message(client_socket, self.common.ALL_EMPLOYEE_LIST_RES,
                                      f"{employee_list}")
            elif request_header == self.common.CHAT_ROOM_REQ:  
                assert isinstance(request_data, tuple)
                login_employee_id, request_employee_id= request_data
                chat_room_id = self.db_conn.find_chat_room_by_two_employee_id(login_employee_id, request_employee_id)
                message_list = self.db_conn.find_messages_by_chat_room_id(chat_room_id)
                self.send_message(self.common.MESSAGE_LIST_RES, self.encoder.toJSON_an_object(message_list))
                
                
            return True
