# 1. Напишите программу, которая принимает список чисел от пользователя и передает его в функцию modify_list, которая
# изменяет элементы списка. Функция должна умножить нечетные числа на 2, а четные числа разделить на 2.
# Выведите измененный список на экран. Объясните, почему изменения происходят только внутри функции и как работают
# изменяемые и неизменяемые параметры.
# Пример вывода:
# Введите список чисел, разделенных пробелами: 1 2 3 4 5
# Измененный список чисел: [2, 1, 6, 2, 10]
#
# def modify_list(numbers):
#     for i in range(len(numbers)):
#         if numbers[i] % 2 == 0:     # Четное число
#             numbers[i] = numbers[i] / 2
#         else:                       # Нечетное число
#             numbers[i] = numbers[i] * 2
#
# user_input = input("Введите список чисел, разделенных пробелами: ") # Запрашиваем у пользователя ввод списка чисел
# numbers_list = list(map(int, user_input.split()))
#
# modify_list(numbers_list)  # Вызываем функцию для изменения списка
#
# print("Измененный список чисел:", numbers_list)
#
# 2. Напишите программу, которая принимает произвольное количество аргументов от пользователя и передает их в функцию
# calculate_sum, которая возвращает сумму всех аргументов. Используйте оператор * при передаче аргументов в функцию.
# Выведите результат на экран.
# Пример вывода:
# Введите числа, разделенные пробелами: 1 2 3 4 5
# Сумма чисел: 15
#
# def calculate_sum(*args):
#     return sum(args)
#
# user_input = input("Введите числа, разделенные пробелами: ")  # Запрашиваем у пользователя ввод чисел
# numbers = map(int, user_input.split())
#
# result = calculate_sum(*numbers) # Вызываем функцию для вычисления суммы
#
# print("Сумма чисел:", result)
#
#
#
