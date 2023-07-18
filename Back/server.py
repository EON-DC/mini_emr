from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

import select

from Back.db_connector import DBConnector
from Common.class_common import Common
from Common.class_json_converter import ObjDecoder, ObjEncoder


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

    def send_message(self, client_socket: socket, result):
        print(f"Server SENDED: ({result})")
        client_socket.send(result)

    def receive_message(self, client_socket: socket):
        try:
            recv_message = client_socket.recv(self.common.BUFFER)
            request_header = recv_message[:self.common.HEADER_LENGTH].strip().decode(self.common.FORMAT)
            request_data = recv_message[self.common.HEADER_LENGTH:].strip().decode(self.common.FORMAT)
            print(f"Server RECEIVED: ({request_header},{request_data})")
        except Exception:
            return False
