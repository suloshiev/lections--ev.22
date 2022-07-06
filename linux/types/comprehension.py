#1. ls =[]
# for i in range(0, 200):
#     if i % 2 == 0:
#         ls.append(i)
# print(ls)


#2. ls = []
# for i in range(0, 200):
#     if i % 2 == 0 and i % 3 == 0:
#         ls.append(i)
# print(ls)


# ls = []
# for i in range(0, 101):
#     if i % 2 == 0:
#         ls.append(i**2)
#     else:
#         i % 2 != 0
#         ls.append(i)
# print(ls)

#*********************************************************************

# list comprehension - генераторы списка

# new list = [expression for item in iterable <if condition == True>]


#list comprehension - это упрощенный подход к сохданию списка, который задейстувует цикл(for), а также конструкции if - else для определения того что в итоге окажется добавлено в наш список

# ls = []
# for i in range(0, 100, 2):
#     ls.append(i)
# print(ls)

# new_list = [i for i in range(0, 100, 2)]
# print(new_list)

# ls = [i**2 for i in range(0, 11)]
# print(ls)

# ls = [i*i for i in range(0, 11)]
# print(ls)

# fruits = ['apple', 'banana', 'kiwi', 'mango', 'lemon']
# ls = [i.capitalize() for i in fruits]
# print(ls)

# fruits = ['apple', 'banana', 'kiwi', 'mango', 'lemon']
# ls = [i for i in fruits if 'a' in i]
# print(ls)


# fruits = ['apple', 'banana', 'kiwi', 'mango', 'lemon']
# ls = [i for i in fruits if i != 'apple']
# print(ls)


# list_ = [[1,2,3],[4,5,6],[7,8,9]]
# #ls = [1,2,3,4,5,7,8,9]
# ls = []
# for inner_list in list_:
#     for num in inner_list:
#             ls.append(num)
# print(ls)

# list_ = [[1,2,3],[4,5,6],[7,8,9]]
# ls = [i for inner_list in list_ for i in inner_list]
# print(ls)

# import datetime


# start = datetime.datetime.now()
# ls = [i for i in range(1, 10000000)]
# # for i in range(1, 1000000):
# #     ls.append(i)

# finish = datetime.datetime.now()
# print(finish-start)


#2. ls = [i for i in range(0, 200) if i % 2 == 0 and i % 3 == 0]
# print(ls)

#3. ls = [i**2 if i % 2 == 0 else i**3 for i in range(0, 100)]
# print(ls)


# ls = [i + 10 if i == 8 else i+1 for i in range(0, 10)]
# print(ls)