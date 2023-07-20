class Doctor:
    def __init__(self, doctor_id, employee, assigned_department ):
        self.doctor_id = doctor_id
        self.employee = employee
        self.assigned_department = assigned_department

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"{self.__dict__}"
