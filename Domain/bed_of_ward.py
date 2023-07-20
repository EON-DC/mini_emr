class BedOfWard:
    def __init__(self, bed_id, assigned_ward, additional_info, viewing_bed_name):
        self.bed_id = bed_id
        self.assigned_ward = assigned_ward
        self.additional_info = additional_info
        self.viewing_bed_name = viewing_bed_name

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"{self.__dict__}"
