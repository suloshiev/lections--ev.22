
# Tuple -  это структура данных 
# неизменяемый
# индексируемый
# упорядоченный

# string1 = str('hello attackPython')
# string2 = 'hello world'
# list1 = list(i for i in range(5))
# list2 = [1,2,3,4,5]
# set1 = {}
# dict1 = {'key: 'value'}


# tuple1 = (1,2,3)
# type(tuple1)
# print(type(tuple1)) #-> class tuple

#tuple1 = 1,2
# tuple1[0]= 3 - #Error
# print(tuple1[0])


# print(tuple1[0])
# print(type(tuple1))

# tuple1 = 1,2
# tuple2 = (1,)
# tuple3 = tuple([1,2,3])
# tuple4 = tuple(range(5))


#emails = ('Python@gmail.com', 'Tima@mail.ru', 3,5,['potato','arbuz','apple'])

#print(type(emails[-1]))
# last_object = emails[-1]   #list class
# last_object.append('tomato')
# print(len(emails))


# print(dir(tuple))
# print('*')
# print(dir(list))

# tuple_sequance_first = (2,2,3,4)
# tuple_sequance = tuple(range(5))
# tuple_sequance += tuple_sequance_first
# print(tuple_sequance.count(2))
# indx = tuple_sequance.index(3)
# print(tuple_sequance[indx])

# for i in tuple_sequance:
#     print(i)


#names = ('Tima','Zhanylai','Aidana','Bermet','Ermek')
#print(names[0] + ' Hello') 
# for i in names:
#     print(f'hello {i.capitalize()}!!!')
#     print('it is len:', len(i))


# names_enter = ['Bermet','Ermek']
# for name in names:
#     if name.capitalize() in names_enter:
#         print(f'hello {name.capitalize()}!!!')
# else:
#     print(f'{name} go home!!!')


# first_step_names = []
# names = input("введите имя: ").split(' ')
# for name in names:
#      if len(name) > 4:
#          first_step_names.append(name)
# print(first_step_names)


# print('start for: ')
#for i in range(10):
 #    print(i)
# print('stop for: ')


# while 3 > 2:
#     print(f'{i} work')
#     i +=1

# i = 0
# num = 3
# while num > i:
#     print('i work')
#     i += 1

# m = a % 10
# a = a // 10
# while a > 0:
#     if a % 10 > m:
#         m = a % 10
#     a = a // 10
# print(m) 
