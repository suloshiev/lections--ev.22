from requests import delete
from views import list_of_products, retrieve_product, create_product, update_product, delete_product

def main():
    print('Привет! Тебе доступны следующие функции: \n\tLIST-1:\n\tRETREIEVE-2\n\tCREATE-3\n\tUPDATE-4\n\tDELETE-5')

    choice = input('введите дейтсвие(1,2,3,4,5): ')
    if choice == '1':
        print(list_of_products())
    elif choice == '2':
        print(retrieve_product())
    elif choice == '3':
        print(create_product())
    elif choice == 4:
        print(update_product())
    elif choice == 5:
        print(delete_product())
    else:
        print('Invalid choice!')
        main()


    ask = input('хотите продолжить?(YES/NO): ')
    if ask.lower() == 'yes':
        main()
    else:
        print('пока! пока!')


main()
