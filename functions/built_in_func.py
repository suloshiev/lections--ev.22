# 1 встроенные функции
# input()
# print()
# str()
# sum()
# list()
# len()
# divmod()
# globals()
# locals()
# min()
# max() etc.


# map()
# filter()
# lambda
# enumerate()

# анонимные функции - lambda(такие же функции только без названия)
# lambda функции могут принимать сколько угодно аргументов, но всегда возвращают только одно выражение

# def sum_args(a, b):
#     result = a + b
#     return result

# def sum_args1(a, b): return a + b

# print(sum_args(1, 2))
# print(sum_args1(1, 2))


# sum_arg = lambda a,b: a + b
# print(sum_arg(1, 2))


# x = lambda a, b, c: a+b+c
# print(x(5, 6, 7))


# def myFunc(n):
#     return lambda a: a * n

# mydoubler = myFunc(3)
# mytripler = myFunc(5)

# print(mydoubler(11))
# print(mydoubler(22))
# print(mytripler(11))
# print(mytripler(22))


# ls = ['def', 'Ivan', 'John','',' ']
# new_list = sorted(ls, key=len)
# print(new_list)
#***********************************
#map(function,Iterable) - > применяет функцию к каждому элементу последовательности и возвращает mapobject(итератор) с результатами
#например с помощью map можно выполнять преобразование элементов. Перевести все строки в верхний регистр:
# list_of_words = ['one', 'two', 'three', 'dict']
# result = list(map(str.upper, list_of_words))
# print(result)
# result2= list(map(len, list_of_words))
# print(result2)


# ls = ['1', '2', '3', '4']
# result = list(map(int, ls))
# print(result)


# names = ['John', 'Jamie', 'Sansa', 'Tirion', 'Aibek']
# result = list(map(lambda x: f'Hello mr/mrs {x}', names))
# print(result)


# nums = [1,2,3,4,5]
# nums2 = [100,200,300,400,500]
# result = list(map(lambda x,y: x*y, nums, nums2))
# print(result)


# dict_ = {1: 2, 3: 4, 5: 6}
# result = dict(map(lambda items:(items[0], str(items[1])), dict_.items()))
# print(result)
#****************************************************************************


#filter(function,Iterable) ->применяет ко всем элементам Iterable функцию которую мы передаем и возвращаем filterobject(итератор) с теми объектами  для которых функция вернула True

# list_of_str = ['one', 'two', 'three', 'list', '', '100', '1', '50', 'John99']
# result = filter(str.isdigit, list_of_str)
# print(result)

# for x in result:
#     print(x)


# ls = [10, 11, 102, 213, 314, 515]
# result =list(filter(lambda x: x%2 != 0, ls))
# print(result)


# list_of_words = ['John', 'one', 'two', 'list', 'makers', 'ev.22']
# result = list(filter(lambda x :len(x)>=4, list_of_words ))
# print(result)
#*****************************************************************************
 
#enumerate(Iterable)
# ls = ['str1', 'str2', 'str3'] 
# # i = 0
# # for x in ls:
# #     print(f'element: {x}, index: {i}')
# #     i += 1

# for i, x in enumerate(ls): 
#     print(f'element: {x}, index: {i}')


# new_list = list(enumerate(ls))
# print(new_list)


#zip(iterables) - она запоминает каждый элемент итерируемых объектов между собой в тип данных - tuple и возвращает это

# list1 = [1,2,3]
# list2 = [100,200,300]

# result = list(zip(list1, list2))
# print(result)

# a = [1,2,3,4,5]
# b = [10,20,30,40]
# c = [100,200,300]
# result = list(zip(a,b,c))
# print(result)

#zip для созжания словарей

# d_keys = ['hostname', 'location', 'vendor', 'model', 'IOS', 'IP']
# d_values = ['london_r1', '21 New Blobe Walk', 'Cisco', '4451', '15.4', '10.255.0.1']
# dict_r1 = dict(zip(d_keys, d_values))
# print(dict_r1)


# d_keys = ['hostname', 'location', 'vendor', 'model', 'IOS', 'IP']
# data = {
#     'r1':['london_r1', '21 New Blobe Walk', 'Cisco', '4451', '15.4', '10.255.0.1'],
#     'r2':['london_r1', '21 New Blobe Walk', 'Cisco', '4451', '15.4', '10.255.0.1'],
#     'sw1':['london_sw1', '21 New Blobe Walk', 'Cisco', '3967', '13.2', '14.764.2.9']
# }
# london_data = {}
# for key in data.keys():
#     london_data[key] = dict(zip(d_keys,data[key]))
# print(london_data)
#****************************************************************************************

#all и any



#all -> возврщает True,если все элементы обьекта истинна(или объект пустой)

# ls = [[1], 1,'stroka', True]
# print(all(ls))

# ip = '10.255.0.0.1'
# result = all(i.isdigit() for i in ip.split('.'))
# print(result)

#any -> возвращает True,е если хотя бы один элемент истинный

# ls = [0, 0, '', False, 1]
# print(any(ls))

# def ignor_command(command):
#     """
#     Функция принимает есть ли в команде слово из списка ignore. True - если есть, False - если нет такого слова
#     """
#     ignore = ['rm -rf', 'alias', 'reset']

#     for word in ignore:
#         if word in command:
#             return True
#     return False
# #print(ignor_command('sudo rm -rf user'))
# command = 'sudo reset configuration'
# if ignor_command(command):
#     raise Exception('Invalyd command')
# print('vse ok')


# ignore = ['rm -rf', 'alias', 'reset']
# command = 'sudo reset comfiguration'

# if any([word in command for word in ignore]):
#     raise Exception
# print('vse ok!')
#******************************************************************************

from random import choices
from string import ascii_letters, digits
from itertools import repeat
result = 100000
q_password = int(input('введите кол-во паролей: '))
{
    f(choices(ascii_letters, k=10), choices(digits, k=5)) for f in repeat(lambda x, y: ''.join(set(x+y)), q_password)
}
print(result)
print(f'kol-vo parolei: {len(result)}')
from statistics import mean

dlina = {len{x} for x in result}
print(f'srednyaya dlina: {mean(dlina)}')