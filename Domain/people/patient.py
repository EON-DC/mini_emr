class Patient:
    def __init__(self, patient_id, birth_date, name, sex, ssn, address, type_insurance, allocated_bed_location_id,
                 register_number):
        self.patient_id = patient_id
        self.birth_date = birth_date
        self.name = name
        self.sex = sex
        self.ssn = ssn
        self.address = address
        self.type_insurance = type_insurance
        self.allocated_bed_location_id = allocated_bed_location_id
        self.register_number = register_number

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"{self.__dict__}"
