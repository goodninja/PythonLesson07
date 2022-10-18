import internal_processing

def user_inputnum():
    inputnum = 0
    try:
        while inputnum < 1 or inputnum > 5:
            inputnum = int(input("Выберите нужную цифру, чтобы сделать запрос -> "))
    except ValueError:
        print('Не корректный ввод')
    return inputnum

def menu_point(number):
    if number == 1:
    # 1 Добавить контакт
        input_newname = input('Введите ФИО нового контакта для добавления в справочник: ')
        input_newphone = input('Введите номер телефона нового контакта: ')
        return internal_processing.add_contact(input_newname,input_newphone)
    # 2  Поиск контакта по данным
    elif number == 2:
        return internal_processing.name_or_phone_searching(input('Введите фамилию или номер телефона контакта для поиска: '))
# Вывод ответа
def user_response(numb):
    menu_point(numb)


