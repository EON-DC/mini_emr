class ChatRoom:
    def __init__(self, chat_room_id, created_time):
        self.chat_room_id = chat_room_id
        self.created_time = created_time

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"{self.__dict__}"
