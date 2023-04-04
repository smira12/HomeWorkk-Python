# Создать телефонный справочник который может:
#
# 1. Открыть файл телефонной книги
# 2. Сохранить файл в телефонной книги
# 3. Показать все контакты
# 4. Найти контакт
# 5. Добавить контакт
# 6. Изменить контакт
# 7. Удалить контакт
# 8. Выход

file_name = 'phonebook.txt'
my_file = open(file_name, 'a')
# my_file.close

def main_menu():
    print('\n main menu \n')
    print('1. Показать все контакты')
    print('2. Добавить контакт')
    print('3. Сохранить файл в телефонной книги')
    print('4. Выход')
    menu_point = input("Введите номер меню: ")
    file_contacts = {}
    if menu_point == '1':
        my_file = open(file_name, 'r')
        file_contacts = my_file.read()
        if len(file_contacts) == 0:
            print('Телефонная книга пуста!')
        else:
            print(file_contacts)
            my_file.close()
            enter = input('Нажмите Ввод что бы продолжить!')
            main_menu()
    elif menu_point == '2':
        new_contact(file_contacts)
        enter = input('Нажмите Ввод что бы продолжить!')
        main_menu()
    elif menu_point == '3':
        safe_file(new_contact)
        enter = input('Нажмите Ввод что бы продолжить!')
        main_menu()
    elif menu_point == '4':
        print('До скорой встречи')
        enter = input('Нажмите Ввод что бы продолжить!')
        main_menu()

def open_read(file_contacts):
    with open(file_name, 'r', encoding='UTF-8') as f:
        file_contacts = f.read()
        return file_contacts

def safe_file(file_contacts):
    with open(file_name, 'a', encoding='UTF-8') as f:
        f.write(new_contact(file_contacts))


def new_contact(file_contacts):
    last_name = input('Введите Фамилию: ')
    first_name = input('Введите Имя: ')
    phone_number = input('Введите номер телефона')
    description = input('Введите описание: ')
    return file_contacts

main_menu()