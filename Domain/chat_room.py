import datetime


class ChatRoom:
    def __init__(self, chat_room_id, created_time, user_list=None, message_list=None):
        self.chat_room_id = chat_room_id
        self.created_time = self.date_time_converter(created_time)
        if user_list is not None: # 리스트 초기화
            self.user_list = user_list
        else:
            self.user_list = list()

        if message_list is not None:
            self.message_list = message_list
        else:
            self.message_list = list()


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
        del origin_dict['user_list']
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
