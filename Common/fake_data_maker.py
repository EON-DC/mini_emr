import random
import datetime

from faker import Faker
import numpy as np


class FakeDataMaker:
    def __init__(self):
        self.faker = Faker("ko-KR")

    @staticmethod
    def get_random_temp():
        bt = int(np.random.normal(scale=4) + 370)
        return bt

    @staticmethod
    def get_random_hr():
        hr = int(np.random.normal(scale=10) + 80)
        return hr

    @staticmethod
    def get_random_rr():
        rr = int(np.random.normal(scale=4) + 16)
        return rr

    @staticmethod
    def get_random_register_num_list(size):
        result_list = list()
        while len(result_list) < size:
            rand_num = f"{int(random.random() * (10 ** 6)):06d}"
            if rand_num not in result_list:
                result_list.append(rand_num)
        return result_list

    @staticmethod
    def get_random_back_ssn_num_list(option_: str):
        if option_ == 'young':
            gender = random.randint(3, 5)
        else:
            gender = random.randint(1, 3)
        back_num = f'{int(random.random() * (10 ** 6)):06d}'
        return f'{gender}{back_num}'

    @staticmethod
    def get_random_date_time():
        date = datetime.datetime.strptime("2022-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")
        random_hour = random.randint(1, 1000)
        temp_date = date + datetime.timedelta(hours=random_hour)
        return temp_date

    def get_random_date_time_str(self):
        return self.get_random_date_time().strftime("%Y-%m-%d %H:%M:%S")

    def get_random_fake_name(self):
        return self.faker.name()

    @staticmethod
    def get_random_type_job():
        return random.randint(1, 3)
        # if num == 1:
        #     return "nurse"
        # elif num == 2:
        #     return "doctor"
        # elif num == 3:
        #     return "admin"
        # print(num)
        # raise 'randint 확인'

    def get_random_phone_num(self):
        return self.faker.phone_number()

    def get_random_time(self) -> str:
        time_str = self.faker.time()
        return time_str

    def get_random_login_id(self) -> str:
        simple_profile = self.faker.simple_profile()
        return simple_profile['username']

    def get_random_simple_profile(self) -> dict:
        # {'username': 'jinyeongsug', 'name': '이현우', 'sex': 'M',
        # 'address': '경상북도 광명시 역삼거리 (영미김이읍)',
        # 'mail': 'eungyeong71@dreamwiz.com', 'birthdate': datetime.date(1912, 12, 10)}
        return self.faker.simple_profile()

    def get_random_ssn(self) -> str:
        return self.faker.ssn()

    def get_random_lorem(self) -> str:
        return self.faker.catch_phrase()
