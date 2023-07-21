import json

from Domain.department import Department
from Domain.emergency_nurse_record import EmergencyNurseRecord
from Domain.ktas import KTAS
from Domain.message import Message
from Domain.people._employee import Employee
from Domain.people.patient import Patient


class ObjEncoder(json.JSONEncoder):
    _instance = None

    def __new__(cls):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        super().__init__()

    def toJSON_as_binary(self, obj):
        if isinstance(obj, list):
            temp_list = list()
            for o in obj:
                str_obj = self.toJSON_an_object(o)
                temp_list.append(str_obj)
            list_json = json.dumps(temp_list, default=lambda o: o.__dict__)
            return list_json.encode('utf-8')
        return self.toJSON_an_object_with_encode(obj)

    def toJSON_an_object_with_encode(self, obj):
        json_string = self.toJSON_an_object(obj)
        return json_string.encode('utf-8')

    def toJSON_an_object(self, obj):
        print(obj.__dict__)
        string_converted_obj = json.dumps(obj, default=lambda o: o.__dict__)
        json_string = self.encode(string_converted_obj)
        return json_string


class ObjDecoder(json.JSONDecoder):
    _instance = None

    def __new__(cls):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        super().__init__()

    def binary_to_obj(self, binary_str):
        # object 대신 TRUE or FALSE 로 대답해주는 경우엔 그대로 전송되게 함
        if binary_str == "True":
            return binary_str
        elif binary_str == "False":
            return binary_str

        if isinstance(binary_str, bytes):  # binary -> utf-8
            binary_str = binary_str.decode('utf-8')

        # 리스트 내 튜플 타입 처리
        if binary_str.startswith("[("):
            result = self.list_str_convert(binary_str)
            return result
        if binary_str.startswith("("):
            result = self.tuple_str_convert(binary_str)
            return result
        if "'" in binary_str:
            binary_str = binary_str.replace("'", '"')
        json_string = json.loads(binary_str)  # utf-8 -> json

        if isinstance(json_string, list):
            result_obj = self.list_mapper(json_string)
        else:
            result_obj = self.object_mapper(json_string)
        if result_obj is not None:
            return result_obj
        if isinstance(json_string, str):
            json_string = json.loads(json_string)
        return json_string

        # json_to_object = json.loads(json_string)  # json -> dict(default)

    def tuple_str_convert(self, tuple_str):
        temp_list = tuple_str[1:len(tuple_str)-1].replace(" ", "").replace("'", '').split(',')
        result_list = list()
        for item in temp_list:
            if item.isdigit():
                result_list.append(int(item))
            else:
                result_list.append(item)
        return tuple(result_list)


    def list_str_convert(self, double_list_str):
        temp_list = double_list_str[1:len(double_list_str) - 1].replace(" ", "").replace("'", '').split('),(')
        result_list = list()
        for row in temp_list:
            if row.startswith('('):
                row = row[1:]
            if row.endswith(')'):
                row = row[:len(row)-1]
            str_list = row.split(',')
            result_list.append(tuple(str_list))
        return result_list

    def object_mapper(self, dict_obj):
        if isinstance(dict_obj, str):
            dict_obj = json.loads(dict_obj)
        if isinstance(dict_obj, str):
            dict_obj = json.loads(dict_obj)
        assert isinstance(dict_obj, dict)
        if "is_confirmed" in dict_obj.keys():
            return Message(**dict_obj)
        elif "mobile_phone_num_1" in dict_obj.keys():
            return Employee(**dict_obj)
        elif "first_category_name" in dict_obj.keys():
            return KTAS(**dict_obj)
        elif 'enr_id' in dict_obj.keys():
            return EmergencyNurseRecord(**dict_obj)
        elif 'department_id' in dict_obj.keys() and 'job_category' in dict_obj.keys():
            return Department(**dict_obj)
        elif 'patient_id' in dict_obj.keys() and 'birth_date' in dict_obj.keys():
            return Patient(**dict_obj)

    def list_mapper(self, list_obj):
        assert isinstance(list_obj, list)
        result_list = list()
        try:
            for o in list_obj:
                converted_o = self.object_mapper(o)
                result_list.append(converted_o)
        except:
            print("객체화 불가")
            result_list = list_obj
        return result_list


if __name__ == '__main__':
    test_str = f"""{[("IC-1", "김철수(M/55)", "김순재/조운", "접수중"),
                     ("IC-2", "관우(M/22)", "김순재/박사라", "접수중")]}"""
    result = ObjDecoder().binary_to_obj(test_str)
    print(result)
