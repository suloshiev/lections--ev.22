# Обработка исключений
# Операторы:try...except

#Ошибки связанные с кодом:
# SyntaxError
# IndentationError
# TabError

# #Исключения - Invalid values
# ZeroDivisionError
# ArithmeticError
# NameError
# IndexError
# KeyError
# ValueError
# ImportError
# BaseException  #прородитель всех ошибок


# try:
#     <Body try>
# except:
#     <body except>


# num1 = int(input('Введите число: '))
# print(num1)
# print('очень важная строчка кода: ')

# try:
#     num1 = int(input('Введиет число: '))
#     print(num1)
# except:
#     ZeroDivisionError
#     ArithmeticError
#     NameError
#     IndexError
#     KeyError
#     ValueError
#     ImportError
#     BaseException 
#     print('Vy vveli nekorektnye dannye, ispravte eto!!!')
# print('очень важная строчка кода')

#1. importt sys
# list_ = [1,2,3,4,5]
# index = int(input('vvedite index: '))
# try:
#     res = list_[index]
#     print(res)
# except:
#     import sys
#     print(f'oops, we catched {sys.exc_info()[0]} error!')

#2.Exception as e
# list_ = [1,2,3,4,5]
# index = int(input('vvedite index: '))
# try:
#     res = list_[index]
#     print(res)
# except Exception as e:
#     print(f'oops, we catcheed {e.__class__} error!')


# list_ = [1,2,3,4,5]
# try:
#     index = int(input('vvedite index: '))
#     res = list_[index]
#     print(res)
# except IndexError:
#     print('IndexError')
# except ValueError:
#     print('ValueError')


#else в try...except
#finally в try...except
# try:
#     <body>
# except:
#     <body>
# else:
#     <body> #Сработает если в оперторе трай не случилась ошибка

# finally:
#     <body> сработает при любом исходе


try:
    num1 = int(input('Enter: '))
    num2 = int(input('Enter: '))
    result = num1 / num2
except ZeroDivisionError:
    print('На ноль делить нельзя!!!')
except ValueError:
    print('Invalyd symbols')
else:
    print(result)
finally:
    print('Код закончился')