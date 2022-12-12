import base64
import json
import os
import sys


# unde am transformat in baza 64
# https://www.base64encode.net/

# https://www.stechies.com/encoding-decoding-base64-strings-python/
# https://stackabuse.com/encoding-and-decoding-base64-strings-in-python/

# https://datagy.io/python-nested-dictionary/


def generate_structure(dictionary, path, tab):
    for key, value in dictionary.items():
        # print(path)
        if type(value) == dict:
            # print(key)
            path = os.path.join(path, str(key))
            if os.path.exists(path):
                raise Exception('[ERROR] - Directory already exists!')
            else:
                tab = tab + '---'
                print(tab, key)
                os.makedirs(path)
                generate_structure(value, path, tab)
                path = os.path.dirname(path)
                tab = tab[:-3]
        else:
            base64_bytes = value.encode('utf-8')
            path = os.path.join(path, str(key))
            tab = tab + '---'

            with open(path, "wb") as file_to_save:
                decoded_data = base64.decodebytes(base64_bytes)
                file_to_save.write(decoded_data)
                print(tab, key, ":", decoded_data)
            path = os.path.dirname(path)
            tab = tab[:-3]
            # print(key + ":" + value)


if __name__ == '__main__':
    if len(sys.argv) < 3:  # create_structure.py root_folder_path structure_json_file_path
        raise Exception('[ERROR] - Invalid number of arguments!')

    path_dir = sys.argv[1]
    json_file_path = sys.argv[2]

    if os.path.exists(path_dir) is False:
        raise Exception('[ERROR] - Directory not found!')

    if os.path.isdir(path_dir) is False:
        raise Exception('[ERROR] - Path is not directory')

    if os.path.exists(json_file_path) is False:
        raise Exception('[ERROR] - File not found!')

    if os.path.isfile(json_file_path) is False:
        raise Exception('[ERROR] - Path is not file!')

    if os.path.getsize(json_file_path) == 0:
        raise Exception('[ERROR] - Json file is empty!')

    try:
        with open(json_file_path) as json_file:
            data = json.load(json_file)
    except Exception as e:
        print(e)
    if data:
        tab = ""
        print("root")
        generate_structure(data, path_dir, tab)
    else:
        raise Exception('[ERROR] - Dictionary is empty!')
