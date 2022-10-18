import re
import files_processing

def add_contact(input_person,phone):
    input_phone = uniq_numbers(phone)
    files_processing.write_file(input_person,input_phone)
    print('Данные добавлены')

def name_or_phone_searching(string):
    if uniq_numbers(string).isdigit():
        string = uniq_numbers(string)
    phone_book = files_processing.read_file()
    answer = []
    for x in range(len(phone_book)):
        if string in phone_book[x]:
            answer.append(phone_book[x])
    if len(answer)!=0:
        for i in range(len(answer)):
            answer[i] = answer[i].split(";")
            print(str(answer[i][1]) + "\n" + str(answer[i][2]))
        exp = input('Выгрузить результаты поиска в отдельный файл? Введите "Да" или "Нет" -> ')
        if exp.lower() == "да":
            files_processing.export_file(answer)
            print("Результаты поиска выгружены в отдельный файл")
    else:
        print('Человек с указанной фамилией не найден')

# Телефонный формат = 84955556777
def uniq_numbers(number):
    number = number.replace(" ","")
    number = re.sub(r'\D',"",number)
    number = re.sub('^7',"8",number)
    return number
