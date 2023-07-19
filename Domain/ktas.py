class KTAS:
    def __init__(self,
                 first_category_name, first_category_code,
                 second_category_name, second_category_code,
                 third_category_name, third_category_code,
                 fourth_category_name, fourth_category_code,
                 final_grade
                 ):
        self.first_category_name = first_category_name
        self.first_category_code = first_category_code
        self.second_category_name = second_category_name
        self.second_category_code = second_category_code
        self.third_category_name = third_category_name
        self.third_category_code = third_category_code
        self.fourth_category_name = fourth_category_name
        self.fourth_category_code = fourth_category_code
        self.final_grade = final_grade

    def __repr__(self):
        return f"{self.__dict__}"