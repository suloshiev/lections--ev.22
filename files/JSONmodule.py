#JavaScript object Notation - JSON
#Единный формат хранения и передачи данных между компьютерами, сервисами, приложениями и языками программирования через сеть интернет

#<filenamr>.json


# {
#     'id':1,
#     'author':'John',
#     'posts':[]
# } --- Это JSON, задача научиться переводить JSON в Python Dict

#!!!
# JS object == []
# PY dict == {}
# JSON == {}


#Процессы Сериализации данных и их Дессериализации
#Сериализация (запись данных в JSON) - это перевод Python Dict в JSON формат (либо сохранить все в файл , либо сохраняем все как текстовые данные)
#dump - этот метод записывает объект в python в файл в формате JSON  
#dumps - этот метод записывает объект в python в строку в формате JSON 


#Десеарилизация - (чтение данных из JSON) это процесс перевода из JSONa в Python Dict
#load - метод, который считывает файл в формате JSON и переводит его в объект Python
#loads - метод, который считывает в текстовом формате JSON и переводит его в объект Python
#--------------------------------------------------------------------------

#Процесс десеарилизации

# import json
# from urllib.request import urlopen

# data = urlopen('https://randomuser.me/api/')
# print(type(data))
# #print(data)
# generate_to_dict = json.load(data)
# print(generate_to_dict)
# print(type(generate_to_dict))

#--------------------------------------------------------------------
# import json


# with open('downApi.json', 'r')as file:
#     data = file.read()
#     # print(data)
#     # print(type(data))
#     user = json.loads(data)
#     print(user)
#     print(type(user))

#---------------------------------------------------
#Процесс сериализации

# import json


# # dict_ = {
# #     'name':'John',
# #     'lastname':'Snow',
# #     'status': True,
# #     'wife': None,
# #     'children': False
# # }

# with open('new.json', 'w') as file:
#     json.dump(dict_, file)

import json

dict_ = {
    'name':'John',
    'lastname':'Snow',
    'status': True,
    'wife': None,
    'children': False
}

string = json.dumps(dict_)
print(string)
print(type(string))