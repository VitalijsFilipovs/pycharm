# 1. Напишите программу, которая открывает файл, считывает из него два числа и выполняет операцию их деления.
# Если число отрицательное, выбросите исключение ValueError с сообщением "Число должно быть положительным".
# Обработайте исключение и выведите соответствующее сообщение.
#
# numbers.txt
# -1
# -2
#
# def main():
#     filename = 'numbers.txt'                # Имя файла
#     try:
#         with open(filename, 'r') as file:
#             num1, num2 = map(float, file)   # Считываем и преобразуем числа
#             if num1 < 0 or num2 < 0:
#                 raise ValueError("Число должно быть положительным")
#             print(f"Результат деления: {num1 / num2}")
#     except ValueError as ve:
#         print(f"Ошибка: {ve}")
#
# if __name__ == '__main__':
#     main()
#
#
# 2. Напишите программу, которая открывает файл, считывает его содержимое и выполняет операции над числами в файле.
# Обработайте возможные исключения при открытии файла (FileNotFoundError) и при выполнении операций над числами
# (ValueError, ZeroDivisionError). Используйте конструкцию try-except-finally для обработки исключений и закрытия
# файла в блоке finally.
#
# numbers.txt
# -1
# -2

# def main():
#     filename = 'numbers.txt'    # Имя файла
#     file = None                 # Переменная для хранения ссылки на файл
#
#     try:
#         file = open(filename, 'r')                          # Открываем файл для чтения
#         numbers = [float(line.strip()) for line in file]    # Считываем и преобразуем строки в числа
#
#         sum_result = sum(numbers)           # Выполняем операции над числами
#         product_result = 1
#         for num in numbers:
#             product_result *= num
#
#         print(f"Сумма: {sum_result}")
#         print(f"Произведение: {product_result}")
#
#         if len(numbers) >= 2:               # Пример деления, если есть хотя бы два числа
#             division_result = numbers[0] / numbers[1]
#             print(f"Результат деления {numbers[0]} / {numbers[1]} = {division_result}")
#
#     except FileNotFoundError:
#         print("Ошибка: Файл не найден.")
#     except ValueError as ve:
#         print(f"Ошибка: Неверное значение в файле. {ve}")
#     except ZeroDivisionError:
#         print("Ошибка: Деление на ноль.")
#     finally:
#         if file:
#             file.close()                    # Закрываем файл в блоке finally
#
# if __name__ == '__main__':
#     main()
