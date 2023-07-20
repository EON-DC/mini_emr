class DTOMaker:
    _instance = None

    def __new__(cls):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        pass

    def make_login_dto(self, username, password):
        return LoginDTO(username, password)

class LoginDTO:
    def __init__(self, username, password):
        self.login_username = username
        self.password = password

class PatientListDTO:
    def __init__(self):
        self.row_data = list()

    def add_row(self):
        viewing_bed_name
        patient_id
        patient_name
        patient_age
        assigned_doctor_name
        assigned_nurse_name
        state
        self.row_data.append()