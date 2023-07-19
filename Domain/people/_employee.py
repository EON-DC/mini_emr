class Employee:
    def __init__(self, employee_id, name, type_job, login_username, login_password,
                 mobile_phone_num_1, mobile_phone_num_2):
        self.employee_id = employee_id
        self.name = name
        self.type_job = type_job
        self.login_username = login_username
        self.login_password = login_password
        self.mobile_phone_num_1 = mobile_phone_num_1
        self.mobile_phone_num_2 = mobile_phone_num_2

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"{self.__dict__}"
