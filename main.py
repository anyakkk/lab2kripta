import random
import math

hints = True
menu = "\n1)Шифр Цезаря\n2)Лозунговый шифр\n3)Шифр полибианского квадрата\n4)Шифрующая система Трисемуса\n5)Шифр Playfair\n6)Шифры системы омофонов\n7)Шифр Виженера\n8)Поменять текст\n9)Включить/Выключить подсказки\n"

# Шифр Цезаря
def Caesar():
    print("Шифр Цезаря")
    print("Исходний текст: " + text)
    Step = int(input("Введите шаг: ")) 
    Shift = ord("z") - ord("a") + 1
    cipher = ""
    for t in text:
        if "a" <= t <= "z":
            s = chr(ord(t) + Step)
            while s > "z":
                s = chr(ord(s) - Shift) 
            cipher += s
        elif "0" <= t <= "9":
            s = int(t) + Step
            while s > 9:
                s -= 10
            cipher += str(s)
        else:
            cipher += t
    print("Результат: " + cipher)


def printTable(arr):
    for i in range(len(arr)):
        print('[', end = "")
        for j in range(len(arr[i])):
            print(arr[i][j], end="")
            if j < len(arr[i])-1:
                print(", ", end="")
        print(']')

# Лозунговый шифр
def slogan():
    print("Лозунговый шифр")
    print("Исходний текст: " + text)
    Step = input("Введите лозунг: ")
    d = dict()
    used = []
    cipher = ""
    arr = [[], []]
    i = 0
    k = ord('a')
    for j in range(ord('a'), ord('z')+1):
        arr[0].append(chr(j))
        while (i < len(Step)) and (Step[i] in used):
            i += 1
        if i < len(Step):
            d[chr(j)] = Step[i]
            used.append(Step[i])
            arr[1].append(Step[i])
        else:
            while chr(k) in used:
                k += 1
            d[chr(j)] = chr(k)
            used.append(chr(k))
            arr[1].append(chr(k))
    if hints:
        printTable(arr)
    for t in text:
        if "a" <= t <= "z":
            cipher += d[t]
        else:
            cipher += t
    print("Результат: " + cipher)


# Шифр полибианского квадрата
def polybianSquare():
    print("Шифр полибианского квадрата")
    print("Исходний текст: " + text)
    d = dict()
    arr = []
    cipher = ""
    k = ord('a')
    for i in range(5):
        a = []
        for j in range(6):
            if k <= ord("z"):
                a.append(chr(k))
                d[chr(k)] = str((i+1)*10 + j+1)
            else:
                a.append('_')
            k += 1
        arr.append(a)
    if hints:
        printTable(arr)
    for t in text:
        if "a" <= t <= "z":
            cipher += d[t] + ' '
        else:
            cipher += t + ' '
    print("Результат: " + cipher)


# Шифрующая система Трисемуса (Тритемия)
def Trisemus():
    print("Шифрующая система Трисемуса (Тритемия)")
    print("Исходний текст: " + text)
    Step = input("Введите лозунг: ")
    uses = []
    arr = [[]]
    d = dict()
    cipher = ""
    for i in range(len(Step)):
        if Step[i] not in uses:
            arr[0].append(Step[i])
            uses.append(Step[i])
            d[Step[i]] = [0, i]
    j = 0
    k = 1
    a = []
    for i in range(ord('a'), ord('z')+1):
        if chr(i) not in uses:
            a.append(chr(i))
            uses.append(chr(i))
            d[chr(i)] = [k, j]
            j += 1
            if j == (len(arr[0])):
                arr.append(a)
                a = []
                j = 0
                k += 1
    if a != []:
        for i in range(len(arr[0]) - len(a)):
            a.append('_')
        arr.append(a)
    if hints:
        printTable(arr)
    for t in text:
        if "a" <= t <= "z":
            if d[t][0] < len(arr) - 1:
                ch = arr[d[t][0]+1][d[t][1]]
                if ch == "_":
                    ch = arr[0][d[t][1]]
            else:
                ch = arr[0][d[t][1]]
            cipher += ch
        else:
            cipher += t
    print("Результат: " + cipher)


def findInTable(table, char, size):
    for i in range(len(table)): 
        if table[i] == char: 
            return (i // size, i % size)

def printByIndex(i, j, size, table):
    if i*size + j > len(table):
        print(i*size+j - len(table), end = '')
    else:
        print(table[i*size + j], end ='')

alph = 'abcdefghijklmnopqrstuvwxyz'
alph = [a for a in alph]

# Шифр Playfair
def Playfair():
    print("Шифр Playfair")
    print("Исходний текст: " + text)
    t = [t for t in text]

    key = input('Введите ключ: ')
    size = int(input('Введите размер таблицы: '))
    key_set = set()
    old_key = key
    key = ''
    for i in range(len(old_key)):
        if not old_key[i] in key_set:
            key += old_key[i]
            key_set.add(old_key[i])

    table = []
    for i in range(len(key) + len(alph)):
        if i < len(key):
            table.append(key[i])
        elif not alph[i - len(key)] in key_set:
            table.append(alph[i - len(key)])

    for i in range(1, len(t)):
        if t[i] == t[i - 1]:
            t.insert(i, 'x')

    if len(t) % 2 != 0:
        t.append('x')

    pair = []
    for i in range(0, len(t), 2):
        pair.append(t[i : i + 2])     
    if hints:    
        printTable(pair)

    print("Результат: ", end='')
    vertical_size = math.ceil(len(table)/size)
    for p in pair:
        p1i, p1j = findInTable(table, p[0], size) 
        p2i, p2j = findInTable(table, p[1], size)

        if p1i == p2i:
            printByIndex(p1i, (p1j+1)%size, size, table)
            printByIndex(p2i, (p2j+1)%size, size, table)
        elif p1j == p2j:
            printByIndex((p1i+1)%vertical_size, p1j, size, table)
            printByIndex((p2i+1)%vertical_size, p2j, size, table)
        else:
            printByIndex(p1i, p2j, size, table)
            printByIndex(p2i, p1j, size, table)
    print()


# Шифры системы омофонов
def Homophones():
    print("Шифры системы омофонов")
    print("Исходний текст: " + text)
    seed = 0
    codes = 2
    homocodes = {}
    count = 2
    nums = set()
    for i in alph:
        lst = []
        for j in range(count):
            r = random.randint(0, (len(alph)*10*count))
            while r in nums:
                r = random.randint(0, (len(alph)*10*count))
            nums.add(r)
            lst.append(r)
        homocodes[i]= lst

    random.seed(seed)
    cipher = ""
    for i in range(len(text)):
        index = random.randint(0, codes-1)
        cipher += str(homocodes[text[i]][index]) + ' '
    print("Результат: " + cipher)

# Шифр Виженера
# https://www.dcode.fr/tools/trithemius/images/trithemius-grid.png
def Vigener():
    print("Шифр Виженера")
    print("Исходний текст: " + text)
    Step = input("Введите ключ: ")
    cipher = ""
    i = 0
    for t in text:
        ch = ord(t) + (ord(Step[i]) - ord('a'))
        if ch < ord('a'):
            ch += len(alph)
        if ch > ord('z'):
            ch -= len(alph)
        cipher += chr(ch)
        i += 1
        if i == len(Step):
            i = 0
    print("Результат: " + cipher)

text = input("Введите текст: ").lower()
while True:
    print(menu)
    step = input("Выберите номер действия: ")
    if step in {'1', '2', '3', '4', '5', '6', '7', '8', '9'}:
        step = int(step)
        if step == 8:
            text = input("Введите текст: ").lower()
        elif step == 9:
            hints = not hints
        elif step == 1: Caesar()
        elif step == 2: slogan()
        elif step == 3: polybianSquare()
        elif step == 4: Trisemus()
        elif step == 5: Playfair()
        elif step == 6: Homophones()
        elif step == 7: Vigener()
    else:
        print("Неверный ввод")