import socket
from threading import Thread

from Common.class_common import Common
from Common.class_json_converter import ObjEncoder, ObjDecoder
from Domain.dto.dto_class import DTOMaker


class Connector:
    def __init__(self):
        self.common = None
        self.client_socket = None
        self.receive_thread = None
        self.controller = None

        self.dto_maker = None
        self.login_employee = None
        self.selected_patient = None
        self.patient_list = None
        self.selected_chat_room = None

        self.encoder = ObjEncoder()
        self.decoder = ObjDecoder()

        self.setUp_attr()

    def setUp_attr(self):
        self.common = Common()
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.common.HOST, self.common.PORT))
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

    def receive_message(self):
        while True:
            try:
                print("Client_listening")
                recv_encoded_message = self.client_socket.recv(self.common.BUFFER)
                response_header, response_data = self.header_data_distributor(recv_encoded_message)
                print(f"CLIENT RECEIVED: ({response_header},{response_data})")
            except Exception:
                return False

            # 아이디 중복 확인 결과
            if response_header == self.common.LOGIN_ACCESS_RES:
                if response_data != self.common.FALSE:
                    self.login_employee = response_data  # employee obj
                self.controller.command_signal.emit(self.common.LOGIN_ACCESS_RES, response_data)
            # 정보 보내기
            elif response_header == self.common.PATIENT_NAMELIST_RES:
                self.patient_list = response_data
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

    def header_data_distributor(self, recv_encoded_message):
        decoded_message = recv_encoded_message.decode(self.common.FORMAT).strip()
        header, data_decoded_str, = decoded_message.split(self.common.START_OF_TEXT)
        data = self.decoder.binary_to_obj(data_decoded_str)
        return header, data
