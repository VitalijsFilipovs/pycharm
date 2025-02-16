# def add(x, y):
#     result = x + y # result - lokaljnaja peremennaja
#     print(f"Result: {result}")
#     return result
#
# def main():
#     x = 10
#     y = 20
#     add(x, y)
# main()
# ----------------------------------------------
# global_var = 10
# def example_function():
#     # lokaljnaja peremennaja
#     local_var = 5
#     print("(1)lokaljnaja peremennja:", local_var)  # Dostup k lokaljnoj peremennoj
#     print("(2)globaljnaja peremennja:", global_var) # dostup k globaljnoj peremennoj
#
# def modify_global():
#     global global_var # ukazivaem chto budet izmenjatj globaljnaja peremennaja
#     global_var = 20
#     print("(3)globaljnaja peremennja izmenena na:", global_var)
#
# # Osnovnoj kod
# print("(4)Globaljnaja peremennaja do vizova funkcii:", global_var)
# example_function() # vizov funkcii s lokaljnoj peremennoj
# modify_global() # izmenenie globaljnoj peremennoj
# print("(5)Globaljnaja peremennaja posle vizova funkcii:", global_var)

# vivod =
# # (4)Globaljnaja peremennaja do vizova funkcii: 10
# # (1)lokaljnaja peremennja: 5
# # (2)globaljnaja peremennja: 10
# # (3)globaljnaja peremennja izmenena na: 20
# # (5)Globaljnaja peremennaja posle vizova funkcii: 20

# x = "(1)global"
#
# def outer_function():
#     x = "(2)enclosing"
#     print(x)
#
#     def inner_function():
#         x = "(3)local"
#         print(x)   # vivod: local
#     inner_function()
# outer_function()
#
# print(x)

# 1. Перепишите решение следующей задачи с использованием функции. У нас есть
# две логические переменные: isWeekday, isVacation (выходной день и каникулы).
# Они могут принимать разные значения, всего 4 комбинации: true - true, true - false,
# false - false, false - true. Есть правило: мы можем поспать, если день не рабочий
# или мы на каникулах. Напишите программу, которая в зависимости от значений
# двух переменных печатает, можем ли мы поспать или нет. То есть для значений
# isWeekday = False и isVacation = False программа должна печатать “можете
# поспать”.

# def can_sleep(is_weekday, is_vacation):
#     # Мы определяем функцию can_sleep, которая принимает два аргумента: is_weekday
#     # и is_vacation. Внутри функции мы проверяем, является ли день нерабочим
#     # (not is_weekday) или находимся ли мы на каникулах (is_vacation).
#     if not is_weekday or is_vacation:
#         return "Можем поспать"
#     else:
#         return "Не можем поспать"
#     # Если одно из условий истинно, функция возвращает строку "Можем поспать". В противном случае возвращает
#     # "Не можем поспать".
# # Примеры значений
# is_weekday = input("Print the day(working day?): ").strip().lower() == "true"
# is_vacation = input("Print the vacation: ").strip().lower() == "true"
# # В конце мы вызываем функцию с примерами значений и выводим результат.
# # Вы можете изменять значения is_weekday и is_vacation, чтобы проверить все возможные комбинации.
# result = can_sleep(is_weekday, is_vacation)
# print(result)

# 2. Даны два целых числа A и B (при этом A ≤ B). Напишите функцию, которая
# печатает все числа от A до B включительно.

# def print_numbers(A, B):
#     for number in range(A, B + 1):
#         print(number)
#
# # Запрос значений A и B у пользователя
# A = int(input("Введите начальное число A: "))  # Начальное число
# B = int(input("Введите конечное число B: "))    # Конечное число
#
# # Проверка, что A меньше или равно B
# if A <= B:
#     print_numbers(A, B)
# else:
#     print("Ошибка: A должно быть меньше или равно B.")