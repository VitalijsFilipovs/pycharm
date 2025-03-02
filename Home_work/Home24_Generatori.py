# 1. Напишите генератор, который будет принимать на вход числа и возвращать их сумму. Генератор должен использовать
# инструкцию yield для возврата текущей суммы и должен продолжать принимать новые числа для добавления к сумме.
# Если генератор получает на вход число 0, он должен прекращать работу и вернуть окончательную сумму. Напишите программу,
# которая будет использовать этот генератор для пошагового расчета суммы чисел, вводимых пользователем.
#
# def my_generator():
#     total = 0
#     while True:
#         try:
#             number = int(input("Введите число (0 для окончания): "))
#             if number == 0:                 # Если введено 0, прекращаем работу генератора
#                 yield total
#                 break
#             total += number
#             yield total                     # Возвращаем текущую сумму
#         except ValueError:
#             print("Пожалуйста, введите корректное число.")
#
# gen = my_generator()                        # Используем генератор
#
# for current_sum in gen:
#     print(f"Текущая сумма: {current_sum}")
#
#
# 2. Напишите генератор, который будет генерировать арифметическую прогрессию
#
# def arithmetic_progression(start, difference, count):
#     current = start
#     for _ in range(count):
#         yield current
#         current += difference
#
# # Пример использования генератора
# start_value = int(input("Введите начальное значение прогрессии: "))
# difference_value = int(input("Введите разность прогрессии: "))
# count_value = int(input("Введите количество элементов прогрессии: "))
#
# print("Арифметическая прогрессия:")
# for number in arithmetic_progression(start_value, difference_value, count_value):
#     print(number)