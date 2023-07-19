import json

from Domain.message import Message


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
        if isinstance(binary_str, bytes):  # binary -> utf-8
            binary_str = binary_str.decode('utf-8')
        json_string = json.loads(binary_str)  # utf-8 -> json
        if isinstance(json_string, list):
            result_obj = self.list_mapper(json_string)
        else:
            result_obj = self.object_mapper(json_string)
        if result_obj is not None:
            return result_obj
        return json_string

        # json_to_object = json.loads(json_string)  # json -> dict(default)

    def object_mapper(self, dict_obj):
        if isinstance(dict_obj, str):
            dict_obj = json.loads(dict_obj)
        if isinstance(dict_obj, str):
            dict_obj = json.loads(dict_obj)
        assert isinstance(dict_obj, dict)
        if "is_confirmed" in dict_obj.keys():
            return Message(**dict_obj)

    def list_mapper(self, list_obj):
        assert isinstance(list_obj, list)
        result_list = list()
        for o in list_obj:
            converted_o = self.object_mapper(o)
            result_list.append(converted_o)
        return result_list


if __name__ == '__main__':
    msg_1 = Message(1, 1, 22, "안녕", False)
    msg_2 = Message(2, 1, 21, "sdfsdlfsjdfl", False)
    msg_3 = Message(None, 7, 21, "abcde", False)
    msg_4 = Message(2, 5, 100, "fghij", True)

    msg_list = [msg_1, msg_2]
    print(id(msg_1))
    print(id(msg_2))


    msg_5 = Message(1, 1, 22, "안녕", False)
    print(id(msg_5))
    msg_list.remove(msg_5)

    print(msg_list)

    # encoder = ObjEncoder()
    # decoder = ObjDecoder()

    # list_obj_ = [msg_1, msg_2, msg_3, msg_4]
    # bytes_list_obj = encoder.toJSON_as_binary(list_obj_)
    # result_list = decoder.binary_to_obj(bytes_list_obj)

    # result = encoder.toJSON_as_binary(msg_1)
    # print(result)

    # result_obj = decoder.binary_to_obj(result)
    # print(result_obj)
