# # типы дaнных в питоне
# from operator import imatmul
# from types import NotImplementedType


# 1. NoneType - ничего пустота
# 2. boolean -правда или ложь (правда или ложь
# 3. чиловые типы данных: a. integer (int) целые числа
#                      b. float - числа с плавающей точкой (-1,2) 
#                      с. complex() комплексные числа(3+5i)
# 4. списковые типы данных:
#                         a. list (список) (массив) - {1,2,3 true,none, "hello"}
#                         b. tuple (кортеж) - ()
#                         c. range (1,3) - range (1,2)
#  5. str() - строки:"hello world ", "Salam 312" 
#  6. set() - множество                       
#  7. dict - словарь содкржит данные в виде ключа:значения -{1: "one"... }
#  ******************************************************************************
#  mutable  (изменяемые типы данных)
#  1. list() 
#  2. set ()
#  3. dict () 
#  immutable (неизменяемые типы данных) 
#  1. NotType
#  2. boolen 
#  3. int(), float(),complex()
#  4. str()
#  5. tuple() 
#  ******************************************************************************
"""стандартный вывод данных""" 
"""
в пайтоне для вывода данных в терминал используется функция prtint()
"""
print ("Hello world")

"""стандартный ввод данных через терминал используется функция input"""
a = input("число") 

# print (a)
# # type() выводит тип данных
# print (type(a))

# b = int (input ("введите число номер2:"))
# print (b)
# print(type(b))

# print (a, b, "Salam")

# a = 5
# b =10
# result = a ** b 
# print (a**b)
# print (result)

# min() max()

# a = {12, 25, 30}
# print (min(a))
# print (max(a))

# a = 2
# b = 5
# c = 7
# print (pow(a, b, c))

