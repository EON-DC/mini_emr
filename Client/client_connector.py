import socket
import traceback
from threading import Thread

from Common.class_common import Common
from Common.class_json_converter import ObjEncoder, ObjDecoder
from Domain.dto.dto_class import DTOMaker
from Domain.people._employee import Employee


class Connector:
    def __init__(self):
        self.common = None
        self.client_socket = None
        self.receive_thread = None
        self.controller = None

        self.dto_maker = None
        self.login_employee = None
        self.selected_patient = None
        self.selected_patient_medical_order = None
        self.selected_patient_emergency_nurse_record = None
        self.selected_patient_ktas = None
        self.patient_table_widget_list = None
        self.bed_id_list = None
        self.bed_name_list = None
        self.selected_chat_room = None
        self.is_keep_on_thread = True
        self.all_employee_list = list()

        self.encoder = ObjEncoder()
        self.decoder = ObjDecoder()

        self.setUp_attr()

    def setUp_attr(self):
        self.common = Common()
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.common.HOST, self.common.PORT))
        self.client_socket.settimeout(5)
        self.client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.receive_thread = Thread(target=self.receive_message)
        self.receive_thread.daemon = True
        self.receive_thread.start()
        self.dto_maker = DTOMaker()

    def get_login_employee(self):
        return self.login_employee

    def get_selected_patient(self):
        return self.selected_patient

    def get_selected_chat_room(self):
        return self.selected_chat_room

    def set_selected_chat_room_by_employee_id(self, employee_id):
        pass

    def set_widget_controller(self, controller):
        # 위젯 연동
        self.controller = controller

    def send_login_dto(self, username, pw):
        dto = self.dto_maker.make_login_dto(username, pw)
        header = self.common.LOGIN_ACCESS_REQ
        data = self.encoder.toJSON_an_object(dto)
        self.send_message(header, data)

    def disconnect(self):
        self.client_socket: socket.socket
        self.client_socket.close()
        print('close 시도됨')
        self.is_keep_on_thread = False

    def receive_message(self):
        while True:
            if self.is_keep_on_thread is False:
                break

            try:
                print("Client_listening")
                recv_encoded_message = self.client_socket.recv(self.common.BUFFER)
                temp = recv_encoded_message.decode(self.common.FORMAT).strip()
                if len(temp) < 3:
                    continue
                response_header, response_data = self.header_data_distributor(temp)
                print(f"CLIENT RECEIVED{type(response_data)}: ({response_header},{response_data})")
            except OSError:
                continue
            except Exception:
                traceback.print_exc()
                continue

            # 로그인 응답 받음
            if response_header == self.common.LOGIN_ACCESS_RES:
                if response_data != self.common.FALSE:
                    self.login_employee = response_data  # employee obj
                self.controller.command_signal.emit(self.common.LOGIN_ACCESS_RES, response_data)
            # 환자 리스트 받음
            elif response_header == self.common.PATIENT_NAMELIST_RES:
                self.patient_table_widget_list = response_data
                # self.patient_list = [['IC-1'], "김철수(M/55)", "김순재/조운", "접수중"]
                self.controller.command_signal.emit(self.common.PATIENT_NAMELIST_RES, response_data)

            # 환자 정보 받음
            elif response_header == self.common.PATIENT_RES:
                self.selected_patient = response_data
                self.controller.command_signal.emit(self.common.PATIENT_RES, response_data)

            # 응급간호기록 받음
            elif response_header == self.common.EMERGENCY_NURSE_RECORD_RES:
                self.selected_patient_emergency_nurse_record = response_data
                self.controller.command_signal.emit(self.common.EMERGENCY_NURSE_RECORD_RES, response_data)

            # 직원 전체 기록 받음
            elif response_header == self.common.ALL_EMPLOYEE_LIST_RES:
                assert isinstance(response_data, list) and isinstance(response_data[0], Employee)
                self.all_employee_list.clear()
                self.all_employee_list.extend(response_data)

    def send_message(self, header, data):
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

        message_to_send = f"{self.common.START_OF_TEXT}".join([header_to_sending, data_to_sending]) \
            .encode(self.common.FORMAT)

        if len(message_to_send) >= self.common.BUFFER:
            raise "부족한 버퍼 용량"
        print(f"CLIENT SENDED: (HEADER: {header} | DATA: {data})")
        self.client_socket.send(message_to_send)

    def header_data_distributor(self, decoded_message):
        # decoded_message = recv_encoded_message.decode(self.common.FORMAT).strip()
        header, data_decoded_str, = decoded_message.split(self.common.START_OF_TEXT)
        data = self.decoder.binary_to_obj(data_decoded_str)
        return header, data

    def send_chat_room_request_with_employee(self, employee: Employee):
        data = f"{(self.login_employee.employee_id, employee.employee_id)}"
        self.send_message(self.common.CHAT_ROOM_REQ, f"{data}" )
