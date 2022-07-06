# строки это набор последовательных символов которые мы храним для предоставления в текстовом файле

# name = "John"
# name1 = """
# john
# snow
# """
# name2 = str("John Snow")
# """сейчас все это мы выведем в терминал"""
# print (name)
# print(name1)
# print(name2)


# print(type(name))
# print(type(name1))
# print(type(name2))
# print(type(5))

#экранирование-это механизм при помощи которого можно вставлять символы которые сложно ввести с клавиатуры 

# \n - перенос строки 
# \t - горизонтальная таьуляция
# \f- перевод страницы
# \r-вохврат указателя (коретки)
# \v-вертикальная табуляция 

# name = "john\nSnow"
# LastName = "\vSnow"
# Last_Name ="\tSnow"
# print(name)
# print(LastName)
# print(Last_Name)

# name = "Raychel"
# print(name *6)
# print(name +"John")


# индексация символов в строке

from curses.ascii import        num


name = "John"
    #    J = 0 = -4
    #    O = 1 = -3
    #    H = 2 = -2 
    #    N = 3 = -1

# print (name[0]) #J
# print (name[-2]) #N 
# print (name[2]) #H
 
#  срезы по индексам

#  string {start:end:step}
#  len() - выводит длину строки

# print(len("Hello world!"))
# name = "John Snow"
# print (len(name))

# text = "Hello world! My name is Snow!"
# print(text[0:5])
# print(text[13:-1])
# print(text[13:])
# print(text[::2])
# print(text[::-1])
# print(text[::-2])
# print(text[:14:-1])
# print(text[:11:-2])

# конкретинация строк(соединение строк)

# word1 = "Hello"
# word2 = "world"
# probel = " "
# result = word1 + probel + word2
# print(result)

# print(word1 + probel + word2 + "!!!")
# str1 = word1 + probel + word2
# print(type(str1))

# Форматирование строк

# 1.с помощью %
# 2.с помощью .format()
# 3.Интерпритация строк (f-строки)

# name = input ("Enter your name: ")
# last_name = input("Enter your last name: ")
# print ("Hello, mr/mrs %s %s" %(name,last_name))

# .format
# name = input ("Enter your name: ")
# last_name = input("Enter your last name: ")

# print("Hello, mr/mrs {} {}".format(name,last_name))

# .f-строки

# name = input ("Enter your name: ")
# last_name = input("Enter your last name: ")
# print(f"Hello, mr/mrs {name} {last_name}")
# print ("Hello, mr/mrs " + name + last_name)
# print ("Hello, mr/mrs " + name + " " + last_name)