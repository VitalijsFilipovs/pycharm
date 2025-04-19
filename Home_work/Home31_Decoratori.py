# 1. Напишите декоратор validate_args, который будет проверять типы аргументов функции и выводить сообщение об ошибке,
# если переданы аргументы неправильного типа. Декоратор должен принимать ожидаемые типы аргументов в качестве параметров.
# Пример использования:
# @validate_args(int, str)
# def greet(age, name):
#     print(f"Привет, {name}! Тебе {age} лет.")
# greet(25, "Анна")  # Все аргументы имеют правильные типы
# greet("25", "Анна")  # Возникнет исключение TypeError
# Ожидаемый вывод:
# Привет, Анна! Тебе 25 лет.
# TypeError: Аргумент 25 имеет неправильный тип <class 'str'>. Ожидается <class 'int'>.
from urllib.response import addbase


# def validate_args(*expected_types):
#     def decorator(func):
#         def wrapper(*args):
#
#             for i in range(len(args)):
#                 if not isinstance(args[i], expected_types[i]):
#                     raise TypeError(
#                         f"Аргумент {args[i]} имеет неправильный тип {type(args[i])}. Ожидается {expected_types[i]}.")
#
#             return func(*args)
#         return wrapper
#     return decorator
#
#
# @validate_args(int, str)
# def greet(age, name):
#     print(f"Привет, {name}! Тебе {age} лет.")
#
#
# # Пример правильного вызова
# greet(25, "Анна")           # Все аргументы имеют правильные типы
#
# # Пример с неправильным типом аргумента
# try:
#     greet("25", "Анна")     # Возникнет исключение TypeError
# except TypeError as e:
#     print(e)

######################################################################################################################

# 2. Напишите декоратор log_args, который будет записывать аргументы и результаты вызовов функции в лог-файл.
# Каждый вызов функции должен быть записан на новой строке в формате "Аргументы: <аргументы>, Результат: <результат>".
# Используйте модуль logging для записи в лог-файл.
# Пример использования:
# @log_args
# def add(a, b):
#     return a + b
# add(2, 3)
# add(5, 7)
# Ожидаемый вывод в файле log.txt:
# Аргументы: 2, 3, Результат: 5
# Аргументы: 5, 7, Результат: 12
# Убедитесь, что перед запуском кода у вас создан файл log.txt в той же директории, где находится скрипт Python.
#
#
# def log_args(number_a, number_b):
#     def decorator(func):
#         def wrapper(a=None, b=None):
#             # Запрашиваем значение a, если number_a установлен в True
#             if number_a and a is None:
#                 a = input("Введите значение a: ")
#                 a = int(a)                              # Преобразуем в целое число
#
#             # Запрашиваем значение b, если number_b установлен в True
#             if number_b and b is None:
#                 b = input("Введите значение b: ")
#                 b = int(b)                              # Преобразуем в целое число
#
#             result = func(a, b)
#
#             # Записываем аргументы и результат в файл с кодировкой UTF-8
#             with open("log.txt", "a", encoding="utf-8") as file:
#                 file.write(f"Аргументы: a={a}, b={b}, Результат: {result}\n")
#
#             print(f"Результат: {result}")
#
#             return result
#         return wrapper
#     return decorator
#
# @log_args(number_a=True, number_b=True)
# def add(a, b):
#     return a + b
#
# # Пример вызова функции
# add()                       # Запрашивает оба значения
# add(2, 3)                 # Использует переданные значения
# add(b=5)                  # Запрашивает значение a, использует переданное значение b
#
# -----------------------------------------------------------------#
#
# log.txt
#
# Аргументы: a=5, b=6, Результат: 11
# Аргументы: a=2, b=3, Результат: 5
# Аргументы: a=99, b=88, Результат: 187
# Аргументы: a=5665, b=5566, Результат: 11231
#
# def log_args(*arg_names):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             arg_values = {}                              # Словарь для хранения аргументов и преобразованных значений
#
#             for i, name in enumerate(arg_names):         # Запрашиваем значения по именам из arg_names
#                 if i < len(args) and args[i] is not None:
#                     arg_values[name] = args[i]
#                 else:
#
#                     if name == 'operation':              # Запрашиваем значение только если его нет в args
#                         value = input(f"Введите аргументы для {name} (+, -, *, /): ")            # Запрашиваем операцию
#                         arg_values[name] = value         # Оставляем как строку
#                     else:
#                         value = input(f"Введите аргументы для {name}: ")                         # Запрашиваем для a и b
#                         arg_values[name] = float(value)  # Преобразуем в число
#
#
#             result = func(**arg_values)                  # Передаем аргументы в функцию
#
#             # Записываем аргументы и результат в файл с кодировкой UTF-8
#             with open("log.txt", "a", encoding="utf-8") as file:
#                 file.write(f"Аргументы: {arg_values}, Результат: {result}\n")
#
#             print(f"Результат: {result}")
#             return result
#
#         return wrapper
#     return decorator
#
#
# @log_args('a', 'b', 'operation')
# def add(a, b, operation):
#     if operation == "+":
#         return a + b
#     elif operation == "-":
#         return a - b
#     elif operation == "*":
#         return a * b
#     elif operation == "/":
#         if b == 0:
#             return "Ошибка: Деление на ноль"
#         return a / b
#     else:
#         return "Ошибка: Неизвестная операция"
#
# add()  # Запрашивает значения для a, b и operation


# import logging
#
# logging.basicConfig(filename="log.txt", level=logging.INFO, format="%(message)s", encoding="utf-8")     # Настраиваем логирование
#
# def log_args(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)          # Вызываем оригинальную функцию и записываем её результат
#
#         if kwargs:
#             log_message = f"Аргументы: {args}, {kwargs}, Результат: {result}"       # Обрабатываем формат вывода аргументов (скрываем пустой kwargs)
#         else:
#             log_message = f"Аргументы: {args}, Результат: {result}"
#
#         logging.info(log_message)               # Логируем результат
#         return result
#
#     return wrapper
#
# # Пример функций
# @log_args
# def add(a, b):
#     return a + b
#
# # Вызовы функций
# add(2, 3)
# add(5, 7)
