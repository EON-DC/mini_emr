import json


class Message:
    def __init__(self, message_id, sender_employee_id, chat_room_id, contents, is_confirmed):
        self.assert_param(message_id,
                          sender_employee_id,
                          chat_room_id,
                          contents,
                          is_confirmed)
        self.message_id = message_id
        self.sender_employee_id = sender_employee_id
        self.chat_room_id = chat_room_id
        self.contents = contents
        self.is_confirmed = self.bool_definer(is_confirmed)

    @staticmethod
    def assert_param(message_id,
                     sender_employee_id,
                     chat_room_id,
                     contents,
                     is_confirmed):
        assert isinstance(message_id, int) or message_id is None
        assert isinstance(sender_employee_id, int)
        assert isinstance(chat_room_id, int)
        assert isinstance(contents, str)
        assert isinstance(is_confirmed, bool) or isinstance(is_confirmed, int)

    @staticmethod
    def bool_definer(value_):
        if isinstance(value_, bool):
            return value_
        if value_ == 1:
            return True
        elif value_ == 0:
            return False 
        else:
            raise 'bool값 확인요망'


    def to_dict_for_insert(self):
        origin_dict = self.__dict__.copy()
        if self.is_confirmed is True:
            origin_dict['is_confirmed'] = 1
        else:
            origin_dict['is_confirmed'] = 0
        return origin_dict

    def __eq__(self, other):
        if isinstance(other, self.__class__) and self.message_id == other.message_id:
            return True
        return False

    def __lt__(self, other):
        return self.message_id < other.message_id

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"{self.__dict__}"
