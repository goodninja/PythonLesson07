import user_input
import os

clear = lambda: os.system('cls')

def menu():
    clear()
    print("""Телефонный справочник города N\n\n
    1. Добавить новый контакт в справочник\n
    2. Поиск контакта по справочнику\n""")
    num = user_input.user_inputnum()
    user_input.user_response(num)

menu()