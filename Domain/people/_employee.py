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

    def get_job(self):
        if self.type_job == 1:
            return "의사"
        elif self.type_job == 2:
            return "간호사"
        elif self.type_job == 3:
            return "행정 직원"
        raise "type job 확인 요망"