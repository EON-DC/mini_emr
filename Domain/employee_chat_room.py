class EmployeeChatRoom:
    def __init__(self):
        pass

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"{self.__dict__}"
