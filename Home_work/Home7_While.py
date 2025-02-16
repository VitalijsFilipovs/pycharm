# Напишите программу, которая запрашивает у пользователя натуральное десятичное число и выводит его двоичное
# представление. Реализуйте алгоритм перевода числа в двоичную систему счисления, используя основные концепции
# представления чисел (подсказка: через деление с остатком). Выведите полученное представление числа на экран.
# Запрос у пользователя
# number = int(input("Введите натуральное десятичное число: "))  # Получаем число от пользователя
#
# Функция для перевода десятичного числа в двоичное
def decimal_to_binary(n):
    if n == 0:
        return "0"

    binary_representation = ""  # Инициализируем пустую строку для двоичного представления

    while n > 0:  # Пока число больше 0
        remainder = n % 2  # Находим остаток от деления на 2
        binary_representation = str(remainder) + binary_representation  # Добавляем остаток вперед к строке
        n = n // 2  # Обновляем число, деля его на 2 (целочисленное деление)

    return binary_representation  # Возвращаем двоичное представление

binary_representation = decimal_to_binary(number)  # Получаем двоичное представление
print(f"Двоичное представление числа: {binary_representation}")  # Выводим результат

#--------------------------------------
# Напишите программу, принимающую число с плавающей точкой и округляющую его до целого числа в соответствии с правилами
# школьной математики. Использовать модуль math и методы из него нельзя. Учесть, что программа должна корректно работать
# с отрицательными числами.
# Запрос у пользователя
number = float(input("Введите вещественное число: "))  # Получаем число от пользователя
# Функция для округления числа
def round_number(num):
    # Проверяем, является ли число отрицательным
    if num < 0:
        # Если число отрицательное, округляем вниз
        return int(num) if num == int(num) else int(num) + 1
    else:
        # Если число положительное, округляем вверх
        return int(num) + (1 if num - int(num) >= 0.5 else 0)

rounded_value = round_number(number)  # Округляем число
print(f"Округленное значение: {rounded_value}")  # Выводим результат