#опараторы сравнения 
#условные операторы 
#логические операторы

# операторы сранения:
# <, >, ==(равно),<=, =>, != (не равно) 

# num1 = 18
# num2 = 15
# stroka1 = 'A'
# print(ord(stroka1))

# stroka2 = 'a'
# print(ord(stroka2))
# result = stroka1 > stroka2
# print(result)
    

# # # # # # #print(chr(1080)) - можно вывести символ из таблицы аски


# # # # # # #bool - True(1) or False(0)

# # # # # # #условные операторы 
# # # # # # # if
# # # # # # # elif
# # # # # # # else



# # # # # # if <condition>:
# # # # # #     если в if приходит True
# # # # # #      <bode if>
# # # # # # elif<condition>:
# # # # # #     <body>
# # # # # # else:
# # # # # #     <body>

# # # # # string = input('enter smt: ')

# # # # # if string == 'Hello':
# # # # #     print('Hello stranger!')
# # # # # elif string == 'mercedes':
# # # # #     print('mecedes-benz s class')
# # # # # else:
# # # # #     print('совпадений не найдено')        

# # # # # print('код закончился')

# # # # #sing up

# # # # email = input('enter your email: ')
# # # # password1 = input('enter password: ')
# # # # password2 = input('enter password confirmation: ')

# # # # if password1 != password2:
# # # #     raise Exception('passwords didn\'t match!!!')
# # # # else:
# # # #     print('Successfully signed up!')




# # # age = (input('enter your age: '))
# # # #print(type(age))
# # # if age.isdigit():
# # #     age = int(age)
# # # else:
# # #     print('введите корректные данные!')
# # #     raise Exception ('value error')
# # # if age < 18:
# # #     print(f'chuvak prihodi cherez {18-age} goda/let!')
# # # else:
# # #     print('vy podhodite!')

# # #логические операторы
# # 1.and - логическое и
# # 2.or - логическое или
# # 3.not - логическое отрицание

# my_age = 20
# your_age = 18
# result = my_age == 20 and your_age == 18
# print(result)

# result = my_age < 18 or your_age == 18
# print(result)

# result = not my_age == 20
# print(result)

# is_user_google_user = True
# is_user_github_user = True
# is_user_age_greater_21 = False
# user_account_coins = 8000

# if is_user_google_user and is_user_github_user and (is_user_age_greater_21 or user_account_coins > 5000):
#     print('you can enter the system mr John Snow')
# else:
#     print('Sorry, you couldnt enter')
