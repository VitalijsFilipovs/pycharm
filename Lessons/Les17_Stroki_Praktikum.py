# 1. Дана строка с именем, например, “Иван”. Написать программу, которая печатает
# приветствие, например, “Привет, Иван!”.
# user_name = input("Enter your name: ")
# print(f"\033[34m Hello, {user_name}\033[m") # Dobavljaem cvet

# 2. Веб-страницы состоят из строк типа "<i>Yay</i>" - выводит текст Yay курсивом. В
# этом примере, строка-тег “i” означает <i> и </i>, которые окружают слово Yay. Нам
# дана строка-тэг и текст. Написать программу, которая выводит тег вокруг данного
# текста, например, "<i>Yay</i>". Например, ('i', 'Hello') → '<i>Hello</i>'.
# text = input("Enter a string: ")
# modified_string = "<i>" + text + "</i>"
# print(modified_string)

# 3. Дана строка. Написать программу, которая создает строку из трех копий последних
# двух символов данной строки. Данная строка должна быть длиной минимум 2.
# (('Hello') → 'lololo'), ('ab') → 'ababab'.
# text = input("Enter a string: ")
# if len(text) > 2:
#     a = text[-2:] * 3
#     print(a)
# else:
#     print("text must be longer than 2")

# 4. Дана строка, написать программу, которая печатает строку без первого и
# последнего символа от данной строки, например, “Иван” - “ва”. “Python” -> “ytho”.
# string = input("Enter a string: ")
# print(string[1:-1])

# 5. Даны две строки разной длины (одна может быть пустой). Написать программу,
# которая печатает строку вида короткая+длинная+короткая, где короткая строка
# снаружи длинной. Например, 'Hello', 'hi' → 'hiHellohi'.
# string1 = input("Enter a string: ")
# string2 = input("Enter another string: ")
# if len(string1) > len(string2):
#     print(string2 + string1 + string2)
# else:
#     print(string1, string2, string1, sep="")

# 6. Написать программу, которая печатает True, если слова “cat” и “dog” встречаются в
# строке одинаковое количество раз (и напечатать false - если разное количество
# раз). 'catdog' → True, 'catcat' → False, '1cat1cadodog' → True

# string = input("Enter a string: ")
# cat_int=string.count('cat')
# dog_int=string.count('dog')
# # if cat_int == dog_int:
# #     print(True)
# # else:
# #     print(False)
# print(cat_int==dog_int) # vivodit ili true ili false
# print(string)
# print(f"cat = {cat_int}")
# print(f"dog = {dog_int}")

# 6 zadacha, drugim putjom

# string1 = input("Введите строку: ")
# cat_int = 0
# dog_int = 0
# i = 0
#
# while i <= len(string1) - 3:  # Убедимся, что осталось достаточно символов для проверки
#     if string1[i:i+3] == "cat":  # Проверка подстроки "cat"
#         cat_int += 1
#     if string1[i:i+3] == "dog":  # Проверка подстроки "dog"
#         dog_int += 1
#     i += 1  # Переход к следующему символу
#
# print(cat_int == dog_int)  # Проверка равенства количества "cat" и "dog"
# print(f"cat = {cat_int}")  # Печать количества "cat"
# print(f"dog = {dog_int}")  # Печать количества "dog"

# 7. Написать программу, которая печатает количество вхождений данной подстроки в
# строку. Например, для подстроки hi, 'abc hi ho' → 1, для подстроки “well”, 'ABCwell
# well') → 2.

# string = input("Введите строку: ")
# substring = input("Введите подстроку для поиска: ")
# count = string.lower().count(substring.lower())  # Подсчет вхождений подстроки в строке
# print(f"Количество вхождений '{substring}' в строке: {count}") # Вывод результата

