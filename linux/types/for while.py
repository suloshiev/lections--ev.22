# types = (str, int, float, list, tuple)

# for value in types:
#     print(value, True if'__iter__' in dir(value) else False)



# name_lists = ['Ermek', 'Aidana', 'Tima','Bermet']

# for name in name_lists:
#     if name.lower() == 'aidana':
#         continue
#     print(f'Hi {name}!')

# name_lists = ['Ermek', 'Aidana', 'Tima','Bermet']
# name_lists.insert(len(name_lists)//2,'Ramazan')

# for name in name_lists:
#     if name =='Ramazan':
#         break
#     print(f'Hi {name}!')


# a = bool(23)
# while a: 
#     if input('enter message: ') in 'war drags black '.split():
#         print('Your BLOCK!!!')
#         break


#1) input(Email) 2) Show Emails
#test@test.com test@mail.ru Testgmail.ru
#CRUD - Create Read Update Delete

# DB_emails = []

# while True:
#     print(' 1) Input Email   2) Show db_emails   3) Delete email in DB_emails   4)stop!!!   5)rename email')
#     choices = int(input('enter choice: '))
#     if choices == 1:
#         email = input('enter email: ')
#         if email.endswith('@gmail.com'):
#             if email in DB_emails:
#                 print('email уже существует!!!')
#                 continue
#             DB_emails.append(email)
#             continue
#         print('invalid email, only GMAIL!!!')
#     elif choices == 2:
#         print(DB_emails)
#     elif choices == 3:
#         email = input('enter email: ')
#         if email in DB_emails:
#             # index = DB_emails.index(email)
#             # DB_emails.pop(index)
#             DB_emails.remove(email)
#         else:
#             print(f'{email} не существует!!!')
#     elif choices == 4:
#         break
#     elif choices == 5:
#         old_email = input('enter email: ')
#         if old_email in DB_emails:
#                 new_email = input('enter new email: ') 
#                 if email.endswith('@gmail.com'):
#                     DB_emails.remove(old_email)
#                     DB_emails.append(new_email)

#     else:
#         print('Eror!!!')


# for i in range(5):
#     if i == 3:
#         continue/break
#     print(i)