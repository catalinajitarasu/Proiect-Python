import base64
import json
import os


# unde am transformat in baza 64
# https://www.base64encode.net/

# https://www.stechies.com/encoding-decoding-base64-strings-python/
# https://stackabuse.com/encoding-and-decoding-base64-strings-in-python/

# https://datagy.io/python-nested-dictionary/


def generate_structure(dictionary, path,tab):
    for key, value in dictionary.items():
        # print(path)
        if type(value) == dict:
            # print(key)
            path = os.path.join(path, str(key))
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
                # decoded_data = base64.decodebytes(base64_bytes + b'==')
                decoded_data = base64.decodebytes(base64_bytes)
                file_to_save.write(decoded_data)
                print(tab, key, ":", decoded_data)
            path = os.path.dirname(path)
            tab = tab[:-3]
            # print(key + ":" + value)


if __name__ == '__main__':
    path_dir = "C:\\Users\\Catalina\\OneDrive\\Desktop\\Proiect-Python\\root"
    with open('C:\\Users\\Catalina\\OneDrive\\Desktop\\Proiect-Python\\Laborator\\test1.json') as json_file:
        data = json.load(json_file)
        tab = ""
    print("root")
    generate_structure(data, path_dir, tab)
