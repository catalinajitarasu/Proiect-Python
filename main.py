import base64
import json
import os

# unde am transformat in baza 64
# https://www.base64encode.net/

# https://www.stechies.com/encoding-decoding-base64-strings-python/
# https://stackabuse.com/encoding-and-decoding-base64-strings-in-python/

# https://datagy.io/python-nested-dictionary/


def iterate_dict(dict_to_iterate, path):
    for key, value in dict_to_iterate.items():
        print(path)
        if type(value) == dict:
            print(key)
            path = os.path.join(path, str(key))
            os.makedirs(path)
            iterate_dict(value, path)
            path = os.path.dirname(path)
        else:
            base64_bytes = value.encode('utf-8')
            path = os.path.join(path, str(key))
            with open(path, "wb") as file_to_save:
                decoded_data = base64.decodebytes(base64_bytes + b'==')
                file_to_save.write(decoded_data)
            path = os.path.dirname(path)
            print(key + ":" + value)


if __name__ == '__main__':
    path_dir = "C:\\Users\\Catalina\\OneDrive\\Desktop\\Proiect-Python\\root"
    with open('C:\\Users\\Catalina\\OneDrive\\Desktop\\Proiect-Python\\Laborator\\file.json') as json_file:
        data = json.load(json_file)
    iterate_dict(data, path_dir)
