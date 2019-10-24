from crypt import *
from RSA_keys import *

s = "."

while True:
    print("1. Генерировать ключи\n2. Шифровать сообщение\n3. Дешифровать сообщение\nq - для выхода\n")
    c = input("Введите соответсующий символ: ")
    print()

    if c == 'q': 
        break
    elif c == '1':
        openKeyFile = open('openKey.txt', 'w')
        closeKeyFile = open('closeKey.txt', 'w')

        openKey, closeKey = Key(8).getKeys()
        
        openKey = s.join(list(map(str, openKey)))
        closeKey = s.join(list(map(str, closeKey)))

        openKeyFile.write(openKey)
        closeKeyFile.write(closeKey)
    elif c == '2':
        print("1. Ввести сообщение\n2. Указать имя файла для шифрования\n")
        cc = input("Ввод: ")

        if cc == '1':
            text = input("Введите ваше сообщение:\n")

            

