from crypt import *
from RSA_keys import *
import os
import time

def clear():
    os.system("clear")

s = "."

crypt = Crypt()

clear()

while True:
    print("1. Генерировать ключи\n2. Шифровать сообщение\n3. Дешифровать сообщение\nq - для выхода\n")
    c = input("Введите соответсующий символ: ")
    print()
    clear()

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

        openKeyFile.close()
        closeKeyFile.close()
    elif c == '2':
        key = 0

        print("1. Ввести открыиый ключ\n2. Указать имя файл с открытым ключом")
        cc = input("Ввод: ")

        clear()

        if cc == '1':
            key = input("Введите открытый ключ: ")
        elif cc == '2':
            fileName = input("Введите имя файла с открытым ключем: ")
            clear()
            f = open(fileName, 'r')

            key = list(map(int, f.readline().split(".")))
            f.close()
        else:
            print("Ошибка")

        print("1. Ввести сообщение\n2. Указать имя файла для шифрования\n")
        cc = input("Ввод: ")

        clear()

        if cc == '1':
            text = input("Введите ваше сообщение:\n")
            clear()
            f = open("crypto.txt", 'w')
            timeStart = time.time()
            f.write(crypt.encrypt(text, key))
            print("Шифрование заняло", time.time() - timeStart, "сек")
            time.sleep(3)
            f.close()
        elif cc == '2':
            fileName = input("Введите имя файла: ")
            clear()
            file = open(fileName, 'r')
            fileText = file.readline()

            encryptFile = open("crypto.txt", 'w')
            timeStart = time.time()
            encryptFile.write(crypt.encrypt(fileText, key))
            print("Шифрование заняло", time.time() - timeStart, "сек")
            time.sleep(3)

            file.close()
            encryptFile.close()
    elif c == '3':
        key = 0

        print("1. Ввести закрытый ключ\n2. Указать имя файл с закрытым ключом")
        cc = input("Ввод: ")

        clear()

        if cc == '1':
            key = input("Введите закрытый ключ: ")
            clear()
        elif cc == '2':
            fileName = input("Введите имя файла с закрытым ключем: ")
            clear()
            f = open(fileName, 'r')

            key = list(map(int, f.readline().split(".")))
            f.close()
        else:
            print("Ошибка")

        print("1. Ввести шифрованное сообщение\n2. Указать имя файла для дешифровки\n")
        cc = input("Ввод: ")
        clear()

        if cc == '1':
            text = input("Введите ваше сообщение:\n")
            clear()
            f = open("decrypto.txt", 'w')
            timeStart = time.time()
            f.write(crypt.decrypt(text, key))
            print("Дешифрование заняло", time.time() - timeStart, "сек")
            time.sleep(3)
            f.close()
        elif cc == '2':
            fileName = input("Введите имя файла: ")
            clear()
            file = open(fileName, 'r')
            fileText = file.readline()

            decryptFile = open("decrypto.txt", 'w')
            timeStart = time.time()
            decryptFile.write(crypt.decrypt(fileText, key))
            print("Дешифрование заняло", time.time() - timeStart, "сек")
            time.sleep(3)

            file.close()
            decryptFile.close()
