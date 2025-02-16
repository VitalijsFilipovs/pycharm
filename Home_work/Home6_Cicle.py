import random

1. Напишите программу, которая генерирует случайное число от 1 до 100,
а затем предлагает пользователю угадать это число. Если пользователь угадывает число,
программа выводит сообщение о победе. Если пользователь не угадывает число, программа сообщает,
больше или меньше загаданное число и предлагает попробовать снова. Используйте цикл с инструкцией break,
чтобы остановить выполнение цикла, когда число угадано.
Пример вывода:
Угадайте число от 1 до 100: 50
Загаданное число меньше.
Попробуйте снова: 75
Загаданное число больше.
Попробуйте снова: 63
Поздравляю! Вы угадали число 63!

# random_number = random.randint(1, 100)
# print("Choose a number from 1 to 100")
# while True:
#
#         user_choice = int(input("Your choice: "))
#
#         if user_choice == random_number:
#             print(f"Congratulations! You chose {random_number}!")
#             break
#
#         elif user_choice > random_number:
#             print(f"Sorry, you chose a big number than {random_number}!")
#
#         else:
#             print(f"Sorry, you chose a small number than {random_number}!")
#-----------------------------------------------------------------------------

2. Напишите программу, которая запрашивает у пользователя число N и выводит первые N чисел Фибоначчи.
Числа Фибоначчи - это последовательность чисел, где каждое следующее число является суммой двух предыдущих чисел
(начиная с 0 и 1). Используйте цикл while для решения задачи. Выведите числа через запятую с помощью команды print.
Пример вывода:
Введите число N: 7
Первые 7 чисел Фибоначчи: 0, 1, 1, 2, 3, 5, 8

# N = int(input("Input number N: "))
# a, b = 0, 1
#
# if N <= 0:
#     print("Please, enter number bigger than 0.")
# else:
#     fibonacci_numbers = []
#     count = 0
#
#     while count < N:
#         fibonacci_numbers.append(a)
#         a, b = b, a + b
#         count += 1
#
# print(f"First {N} Fibonacci numbers: {', '.join(map(str, fibonacci_numbers))}")
#-------------------------------------------------------

3. Напишите программу, которая запрашивает у пользователя целое положительное число и проверяет, является ли оно простым.
Простое число - это число, которое делится только на 1 и на само себя без остатка. Используйте цикл while и
проверку деления числа на все числа от 2 до N-1 для решения задачи. Выведите соответствующее сообщение на экран с
помощью команды print.
Пример вывода:
Введите целое положительное число: 17
Число 17 является простым.

N = int(input("Input integer positive number: "))

if N <= 1:
    print("Number must be more than 1.")
else:
    is_prime = True
    divisor = 2
    while divisor < N:
        if N % divisor == 0:
            is_prime = False
            break
        divisor += 1

    if is_prime:
        print(f"The number {N} is prime.")
    else:
        print(f"The number {N} is not prime.")
