import datetime

from Domain.message import Message
from Domain.people._employee import Employee


class ChatRoom:
    def __init__(self, chat_room_id, created_time=None, employee_list=None, message_list=None):
        self.chat_room_id = chat_room_id
        if created_time is not None:
            self.created_time = self.date_time_converter(created_time)
        else:
            self.created_time = created_time
        if employee_list is not None: # 리스트 초기화
            self.employee_list = employee_list
        else:
            self.employee_list = list()

        if message_list is not None:
            self.message_list = message_list
        else:
            self.message_list = list()

    def append_or_extend_message(self, value):
        if isinstance(value, list):
            assert isinstance(value[0], Message)
            for m in value:
                if m not in self.message_list:
                    self.message_list.append(m)
        else:
            assert isinstance(value, Message)
            if value not in self.message_list:
                self.message_list.append(value)

    def get_messages(self):
        result_message_list = [x for x in self.message_list if x.chat_room_id == self.chat_room_id]
        return result_message_list






    def get_date_str(self, format_=None):
        if format_ is None:
            return self.created_time.strftime('%Y-%m-%d %H:%M:%S')
        else:
            return self.created_time.strftime(format_)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"{self.__dict__}"

    def to_dict_for_insert(self):
        origin_dict = self.__dict__.copy()
        origin_dict['created_time'] = self.created_time.strftime('%Y-%m-%d %H:%M:%S')
        if self.chat_room_id is None:
            del origin_dict['chat_room_id']
        del origin_dict['employee_list']
        del origin_dict['message_list']
        return origin_dict


    @staticmethod
    def date_time_converter(created_time):
        if isinstance(created_time, str):
            result = datetime.datetime.strptime(created_time, '%Y-%m-%d %H:%M:%S')
            return result
        if isinstance(created_time, datetime.datetime):
            return created_time
        else:
            raise 'datetime 확인불가'
