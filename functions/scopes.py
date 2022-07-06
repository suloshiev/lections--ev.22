#Oбласти видимости и пространства имен

# Built-in (встроенная) - print, len, max, int
# Global (глобальная) 
# Enclosed (не локальная, nonlocal)
# local(локальная область видимости)
 

# def print_list(some_list):
#     for element in some_list:
#         print(element)
# element = 'q'
# print_list([1,2,3,4,5,6,7])
# print(element)

# a = 10 #global
# print #built - in
# def hello(): #global
#     a = 'Hello World'#local
#     print(a, 'local inside at func')
# hello()
# print(a,'global')

# x = 'global'
# print(x,'1')  #1 global

# def enclosed():
#     x = 'enclosed'
#     def local():
#         x = 'local'
#         print(x,'3 ')#local
#     print(x,'2 ') #enclosed
#     local()
#     print(x,'4') #enclosed
# enclosed()
# print(x,'5')#global


# def func():
#     print(a)
#     a = 5

# a = 'str'
# func()


# num = 10
# def func():
#     def inner_func():
#         print(num)
#     inner_func()
# func()


# var  = 100 #global variable
# def increment():
#     var = var + 1 # try to update a global variable(using increment -> var += 1)
#     #print(var)
# increment()


#global -> позволяет менять значение глобавльной переменной находясь в локальной области видимости

#nonlocal -> позволяет менять значение не локальной переменной находясь в локальной области видимости


# var = 100
# def increment():
#     global var
#     var += 1
# increment()
# print(var)


# def counter():
#     num = 0
#     def incrementer():
#         nonlocal num
#         num += 1
#         return num
#     return incrementer

# c = counter()
# print(c())
# print(c())
# print(c())


#print(len(dir(__builtins__)))


# print(abs(-15)) #стандарстный вызов встроенной функции
# abs = 15 #переопределяю встроеннок имя  abs в глобальной области
# del abs
# print(abs(-15))


# a = [[1,2,3], [3,3,5]]
# # sums = []
# # for x in a:
# #     sums.append(sum(x))
# #     print(sums)
# #     print(max(sums))


# res = max([sum(x) for x in a])
# print(res)


# alice = [54,10,20]
# john = [10,35,15]

# def compareScores(a, j):
#     score_a = 0
#     score_j = 0
#     for i in range(0,len(a)):
#         if a[i]> j[i]:
#             score_a == 1
#         elif j[i] > a[i]:
#             score_j +=1
#         else:
#             pass
#     return {'alice': score_a, 'john': score_j}
# print(compareScores(alice,john))
# print(compareScores([45,19,20],[12,67,56]))


str_ = 'pythoniiist'
dict_ ={i: str_.count(i) for i in str_}
print(dict_)
