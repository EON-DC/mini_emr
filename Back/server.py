from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

import select

from Back.db_connector import DBConnector
from Common.class_common import Common
from Common.class_json_converter import ObjDecoder, ObjEncoder
from Domain.dto.dto_class import DTOMaker


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
        self.server_socket = socket(AF_INET, SOCK_STREAM)  # AF_INET(ipv4를 의미)
        self.server_socket.bind((self.common.HOST, self.common.PORT))  # 바인딩
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
                    user = self.receive_message(client_socket)
                    if user is False:
                        continue
                    self.sockets_list.append(client_socket)
                    self.clients[client_socket] = user

                else:
                    message = self.receive_message(notified_socket)

                    if message is False:
                        self.sockets_list.remove(notified_socket)
                        del self.clients[notified_socket]
                        continue

            for notified_socket in exception_sockets:
                self.sockets_list.remove(notified_socket)
                del self.clients[notified_socket]

    def send_message(self, client_socket:socket, header, data):
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
        print(f"SERVER SENDED: (HEADER: {header} | DATA: {data})")
        client_socket.send(message_to_send)

    def header_data_distributor(self, recv_encoded_message):
        decoded_message = recv_encoded_message.decode(self.common.FORMAT).strip()
        header, data_decoded_str, = decoded_message.split(self.common.START_OF_TEXT)
        data = self.decoder.binary_to_obj(data_decoded_str)
        return header, data

    def receive_message(self, client_socket: socket):
        while True:
            try:
                recv_encoded_message = client_socket.recv(self.common.BUFFER)
                request_header, request_data = self.header_data_distributor(recv_encoded_message)
                print(f"SERVER RECEIVED: ({request_header},{request_data})")
            except Exception:
                return False

            if request_header == self.common.LOGIN_ACCESS_REQ:
                username = request_data['login_username']
                password = request_data['password']
                login_employee = self.db_conn.assert_login_username_and_password(username, password)
                if login_employee is None:
                    self.send_message(client_socket, self.common.LOGIN_ACCESS_RES,self.common.FALSE)
                else:
                    # 로그인 성공 로직
                    # 회원 정보 보내기
                    data_str = self.encoder.toJSON_an_object(login_employee)
                    self.send_message(client_socket, self.common.LOGIN_ACCESS_RES, data_str)
                    # patient_list 보내기
                    # patient_list = self.dto_maker.
                    # self.send_message(client_socket, self.common.PATIENT_NAMELIST_RES, data_str)
