# Напишите функцию, которая принимает на вход список чисел и возвращает сумму квадратов только четных чисел из списка,
# используя функциональные подходы (например, map, filter и reduce).
# Пример вывода:
# Введите числа: 4, 6, 3, 4, 2, 3, 9, 0, 7
# Результат: 72
#
# from functools import reduce
#
# def sum_squares_even_numbers():
#     numbers = list(map(int, input("Введите числа через пробел: ").split()))
#
#     squares = list(map(lambda num: num**2, filter(lambda num: num % 2 == 0, numbers)))  # Фильтрация четных чисел и вычисление квадратов
#
#     summa = reduce(lambda total, square: total + square, squares) if squares else 0     # Сумма квадратов четных чисел
#
#     print(f"Сумма квадратов четных чисел: {summa}")
#     return summa
#
# sum_squares_even_numbers()
#
#
#
# Напишите функцию, которая принимает на вход список функций и значение, а затем применяет композицию этих функций к
# значению, возвращая конечный результат.
# Пример использования:
# add_one = lambda x: x + 1
# double = lambda x: x * 2
# subtract_three = lambda x: x - 3
# functions = [add_one, double, subtract_three]
# compose_functions(functions, 5) должно вывести 9
#
# def compose_functions(functions, value):
#     result = value                                  # Применяем каждую функцию из списка к значению
#     for function in functions:
#         result = function(result)
#     return result
#
# add_one = lambda x: x + 1                           # Определяем лямбда-функции
# double = lambda x: x * 2
# subtract_three = lambda x: x - 3
#
# functions = [add_one, double, subtract_three]       # Список функций
#
# user_value = int(input("Введите число: "))
#
# result = compose_functions(functions, user_value)   # применяем функции к введенному числу
#
# print(result)