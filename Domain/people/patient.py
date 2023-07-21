import datetime


class Patient:
    def __init__(self, patient_id, birth_date, name, sex, ssn, address,
                 type_insurance, using_bed_id,
                 register_number, assigned_doctor_id, assigned_nurse_id):
        self.patient_id = patient_id
        self.birth_date = birth_date
        self.name = name
        self.sex = sex
        self.ssn = ssn
        self.address = address
        self.type_insurance = type_insurance
        self.using_bed_id = using_bed_id
        self.register_number = register_number
        self.assigned_doctor_id = assigned_doctor_id
        self.assigned_nurse_id = assigned_nurse_id

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"{self.__dict__}"

    def get_age(self):
        live_length = datetime.datetime.now() - datetime.datetime.strptime(self.birth_date, "%Y-%m-%d")
        age = live_length.days // 365
        return age

    def get_name_and_age(self):
        return f"{self.name}({self.sex}/{self.get_age()})"
