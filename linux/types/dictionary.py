# dict() - словарь -> упорядоченная коллекция элементов (python 3.7 -> ordered).Квждый элемент в словаре содержитсяв паре ключ:значение.

# Ключи должны быть униканильными и быть неизменяемым типом данных(str,int,tuple etc).Тогда как значениями могут выступать любые типы данных.
# thisdict = {
#     'brand':'Ford',
#     'model':'Mustang',
#     'year':1964
# }
# print(thisdict)
# print(type(thisdict))

# Hash tables,ассоцитивный массив,dictionary, object(js) == dictionary(py)

# a = {1,2,3,4,} - set(множества)

# some_tuple = 1,2,3 - литералами явл запятые (tuple)
# print(type(some_tuple))
# print(some_tuple)


# some_dict = {}
# print(type(some_dict))
# key_values = {
#     'key':'value',
#     'key1':'value1'
# }
# print(type(key_values))
# dict_created_with_function = dict()
# print(type(dict_created_with_function))

# dict_ = dict((('key','value'),('key2','value2')))
# print(dict_)
# print(type(dict_))
#****************************************************************

from email.policy import default
from urllib.parse import uses_relative


# user_info = {
#     'first_name':'John',
#     'last_name':'Snow',
#     'age':24,
#     'email':'johnsnow24@gmail.com',
#     'role':'moderator',
#     'list':[1,2,3],
    # [1,2,3]:'list' -> error
    #'first_name':'Raychel',
#}
# print(user_info['first_name'])
# print(user_info.get('age'))
#print(dir(dict))
# print(user_info.items())
# for items in user_info.items():
#     print(items)

# print(user_info.keys()) #before changes
# user_info['height'] = 185
# user_info['age'] = 30
# print(user_info.keys()) #after changes
# print(user_info)
# for key in user_info.keys():
#     print(key)

# value() -> выводит только значения ключей

# for value in user_info.values():
#     print(value)

# pop() -> удаляет жлемент по по определенному ключу
# popitem() -> удаляет последнюю пару в словаре  

#print(user_info)

# user_info.pop('list')
# user_info.pop('email')
# user_info.popitem()
# user_info.popitem()
#print(user_info)

#setdefault(key,[default_value]) - работает так же как и метод get(),но если такого значения не существует ,то ог создаст новую пару згачения.

#1 способ применения , получение значений 
# dict_  = {'name':'John','age':23}
# result = dict_.setdefault('age')
# print(result)

#2 способ применения, добавление пары

# dict_  = {'name':'John','age':23}
# result = dict_.setdefault('address','Toktogula str.')
# print(result)

# dict_  = {'name':'John','age':23}
# result = dict_.setdefault('address',)
# print(dict_)


# .update -> изменяет значение


# print(user_info)
# user_info.update({'first_name':'Raychel'})
# user_info.update({'height': 185})

# print(user_info)

# 2.способ 

# user_info['first_name'] = 'Raychel'
# user_info['height'] = 185
# print(user_info)

#******************************************************************************

roles = {
    0:'Admin',
    1:'Moderator',
    2:'Ventor',
    3:'Customer',
    4:'Guest',
}

users = [
    {
        'id':1,
        'name':'John',
        'role': roles[0], 
    },
    {
        'id':2,
        'name':'Raychel',
        'role': roles[3],
    },
    {
         'id':3,
        'name':'Aibek',
        'role': roles[4],
    },
]
product = {
        'id': 1,
        'title': 'Samsung Galaxy s20',
        'discription':'Lorem Ipsum',
        'price': 1000
    }

print(users)
print(product)
user_id = int(input('введите ваш id: '))
if users[user_id]['role'] == roles[0][1]:
    product['discription'] = input('введите новое описание продукта: ')
else:
    raise Exception('у вас недостаточно прав!!!')
print(product)