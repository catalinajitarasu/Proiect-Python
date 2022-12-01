import base64
import json
import os

# unde am transformat in baza 64
# https://www.base64encode.net/

# https://www.stechies.com/encoding-decoding-base64-strings-python/
# https://stackabuse.com/encoding-and-decoding-base64-strings-in-python/

if __name__ == '__main__':
    path_dir = "C:\\Users\\Catalina\\OneDrive\\Desktop\\Proiect-Python\\root"
    with open('C:\\Users\\Catalina\\OneDrive\\Desktop\\Proiect-Python\\Laborator\\file.json') as json_file:
        data = json.load(json_file)
    print(len(data))
    for i in data.items():
        # print(i)
        # cand valoarile cheilor sunt stringuri se creeaza in root fisierele
        if type(i[1]) is str:
            base64_bytes = i[1].encode('utf-8')
            # print(base64_bytes)
            path = os.path.join(path_dir, str(i[0]))
            with open(path, "wb") as file_to_save:
                decoded_data = base64.decodebytes(base64_bytes + b'==')
                # print(decoded_data)
                file_to_save.write(decoded_data)
        # cand valorile cheilor sunt dictionare se creaza directoarele in root dar
        # ce este dictionar trebuie creat in fiecare subdirector
        if type(i[1]) is dict:
            # print(str(i[0]))
            # creez directorul (cheia)
            path = os.path.join(path_dir, str(i[0]))
            os.makedirs(path)
            # in interiorul directorului trebuie sa formez fisierele/directoarele din dictionar
        