#методы строк

#dir() - функция клоторая вытаскивает методы типов данных
#print(dir(str))
#'<соединитель>'.join(<массив который нужно соединить>) - соединяет массив из строк по соединителю в одну строку . 
#ls = ['Milk', 'Bread', 'Water']
#joined = '!'.join(ls)
#print(joined)

#split(разделитель) - дробит строку по разделителю и возвращает тип данных list.
# text = 'milk.bread.water.apple'
# splited = text.split(',')
# print(splited)
# joined =', '.join(splited)
# print(joined)

#replace9<old value>, <new value>,[count] - меняет в строке хначение old na new value, усли вы укажите count то он заменит count еще раз

# text = 'ha ha ha ha'
# result = text.replace('ha', 'la', )
# print(result)
# print(text)

#strip() - убирает пробельные символы в насале и в конце строки

#rstrip() - в конце удаляет 
#lstrip() - в начале удаляет

# text = input('введите фио: ')
# result = text.lstrip()
# print(result)
# print(text.strip())
#print(text)

#count('simbol') - считает кол-во вхождений символов в строку

# text = 'Hello world! I\'m Earth!'
# result = text.count('l')
# print(result)

#index('<value>'), [start], [end] - выводит индекс значениея <value> в нашей строке.

text = 'Hello world! This is makers!'
result = text.index('!', 12)
print(result)
print(len(text))
print(text.find('t'))