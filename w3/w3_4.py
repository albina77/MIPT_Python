import json

with open(r'C:\Users\79821\Downloads\advanced_python_1sem_2020-master\advanced_python_1sem_2020-master\w3\seminar_materials\1.json', 'r') as file:
    File = json.loads(file.read())
    File['glossary']['GlossDiv']['GlossList']['GlossEntry']['week'] = 3

with open(r'C:\Users\79821\Downloads\advanced_python_1sem_2020-master\advanced_python_1sem_2020-master\w3\seminar_materials\1.json', 'w') as file:
    json_string = json.dumps(File) #variant 1
    file.writelines(json_string)
#    json.dump(File, file) #variant 2