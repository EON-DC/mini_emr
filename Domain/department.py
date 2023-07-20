class Department:
    def __init__(self, department_id, name):
        self.department_id = department_id
        self.name = name

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"{self.__dict__}"
