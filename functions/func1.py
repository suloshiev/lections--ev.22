# def <name_of_function>(<>a, b #параметры):
#     <body> #некий код, некая логика
#     <return> #возвращаем что то

# <name_of_function>(<5, 6> #аргументы)

# параметры функции - это у нас переменные, которые будет принимать наша функция ,для того что бы, мы смогли работать с данными которые передаются в эту функцию

#Аргументы - данные, которые мы передаем для параметров при вызове функции

# return - нужен для того чтобы функция что то возвращала и для того что бы могли работать с результатом действия функции
# return - является необязательным оператором(возващает None - если не указать return)

# ls = []
# result = ls.append(1)
# print(ls)
# print('результат дейтсвия: ',result)

# result1 = ls.pop()
# print(ls)
# print('результат дейтсвия: ',result1)



# def sumTwoNums(num1, num2): #параметры
#     result = num1 + num2
#     print(result)
#     return result

# print(sumTwoNums(5, 5)) #аргументы

# def isEven(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False

# a = 10
# b = int(input('Enter: '))
# print(isEven(5))
# print(isEven(a))
# print(isEven(b))


# def isEven1(num: int) -> bool:
#     """
#     Наша функция проверяет является ли число, типа int, четным.
#     """
#     if num % 2 == 0:
#         return True
#     else:
#         return False
# isEven()
# isEven1()


# Anna, Ded, Kabak, Kazak, ono - полиндромы
# from typing import List


# def get_polidrom(words: List[str]) -> List[str]:
    # '''
    # Функция возвращает список из полиндромов
    # '''
    # result = []
    # for word in words:
    #     if word.lower() == word[::-1].lower():
    #         result.append(word)         
    # return result

# some_words = ['John', 'Ono', 'Peter', 'Kazak', 'Anna', 'Islam', 'Dovod', 'Piko']
# print(get_polidrom(some_words))

# def func():
#     print('Hello world!')
# func()

#************************************************
#default params
# def print_welcome(name:str = 'User') -> str:
#     print(f'Welcome, {name}!')

# print_welcome('Islam')


# def money(num:float, period: int) -> float:
#     '''Return final amount of money!''' 
#     if num < 30000:
#         raise Exception('вы ввели некорректное количество денег, мин ставка 30к!')
#     if period < 3:
#         raise Exception ('вы ввели некорректный срок для депозита, мин период вложения 3 года!')
#     i = 0
#     while i < period:
#         num = num + (num * 0.1)
#                                                         #num * 1.1 
#                                                         #num + (num / 100 * 10)
#         i += 1      #i + 1
#     return num
# price = float(input('Введите сумму денег: '))
# year = int(input('Введите срок вашего депозита: '))
# print(money(price, year))

# 'Hello world! My name is John, Last name Snow. Nice to meet you!'

# def get_reverse(text: str) -> str:
#     '''return reversed string'''
#     print(text)
#     spisok = text.split(' ')
#     result = ' '.join(spisok[::-1])
#     print(result)
#     return result

# get_reverse('Hello world! My name is John, Last name Snow. Nice to meet you!')

