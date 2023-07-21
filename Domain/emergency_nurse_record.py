class EmergencyNurseRecord:
    def __init__(self, enr_id, register_id, onset_time, ktas_id, cheif_complain, description, recorder_nurse_id,
                 saved_time, responser, memo):
        self.enr_id = enr_id
        self.register_id = register_id
        self.onset_time = onset_time
        self.ktas_id = ktas_id
        self.cheif_complain = cheif_complain
        self.description = description
        self.recorder_nurse_id = recorder_nurse_id
        self.saved_time = saved_time
        self.responser = responser
        self.memo = memo

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"{self.__dict__}"
