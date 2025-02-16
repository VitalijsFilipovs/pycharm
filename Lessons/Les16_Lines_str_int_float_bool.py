num = int(input("Enter a number: "))  # Запрашиваем у пользователя число
i = 1
while i <= 100:  # Цикл до 100
    first = num * i  # Умножаем num на i
    print(f"Your {num} * {i} = {first}")  # Выводим результат умножения
    i += 1  # Увеличиваем i на 1

# --------------- Novaja tema STROKI ------------------

s1 = "python"
print(s1)  # Выводит строку "python"

text = """
mfkdddfkfkmmgmbmb """  # Многострочная строка
print(text)  # Выводит многострочный текст

a = " "
print(a)  # Выводит пробел

num = 10
print(str(num - 5))  # Преобразует (10 - 5) в строку и выводит "5"

print("Dragon's mother said \"No\" ")  # Выводит строку с экранированием кавычек
print("""Dragon's mother said "No" """)  # Выводит строку с одинарными и двойными кавычками
print(f"Dragon's mother said \"No\"")  # f-строка с экранированием
print('''Khal Drogo's favorite word is "athjahakar"''')  # Многострочная строка

s1 = "I love Python"
s2 = "language"
s3 = s1 + " " + s2 + " " + "and Game DEF"  # Объединение строк
s4 = 5
print(s3 + " " + str(s4))  # Конкатенируем строки и преобразуем число в строку
print(s3 * 7)  # Повторяем строку 7 раз
print("h " * 10)  # Повторяем "h " 10 раз

a = "hello hhht  hhthhtth"
print(len(a))  # Выводит длину строки
l = len(a)
print(l)  # Тот же вывод, что и выше
b = ""
print(len(b))  # Выводит 0, так как строка пустая

a = "ab"
b = "abrakadabra"
print(a in b)  # Проверяет, есть ли подстрока 'ab' в 'abrakadabra'

a = "Hallo"
b = "Hallo"
print(a == b)  # Сравнение строк, выводит True
print("Kot" > "Kit")  # Сравнение строк по алфавиту
print("Kot" < "Kit")

print(ord("K"))  # Переводит букву в её ASCII код
print(ord("k"))
print(ord("o"))
print(chr(98))  # Переводит ASCII код обратно в символ
print(chr(1086))  # ASCII код в символ (в данном случае кириллица)

a = "Hallo python"
print(a[-2])  # Индексирование, выводит второй символ с конца
print(a[6])  # Выводит символ под индексом 6
print(a[0:5])  # Срез строки с 0 по 5
print(a[1:5])  # Срез строки с 1 по 5
print(a[4:])  # Срез строки с 4 до конца
print(a[:5])  # Срез строки от начала до 5
print(a[:])   # Копирует всю строку

str1 = "Hello World, gugugugug, kkkk, pppooo"
print(str1[0:11:2])  # Срез с шагом, выводит символы с 0 по 11 с шагом 2
print(str1[0::2])  # Удаляет каждый второй символ
print(str1[::-1])  # Разворачивает строку
print(str1[::-2])  # Разворачивает строку и удаляет каждый второй символ