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
        self.is_confirmed = is_confirmed

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
        assert isinstance(is_confirmed, bool)

    def __eq__(self, other):
        if isinstance(other, self.__class__) and self.message_id == other.message_id:
            return True
        return False
