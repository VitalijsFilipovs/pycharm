# 1. Напишите программу, которая запрашивает у пользователя строку и определяет, является ли она панграммой.
# Панграмма - это фраза, содержащая все буквы алфавита. Программа должна игнорировать регистр букв и пробелы при проверке
# панграммы. Выведите соответствующее сообщение на экран с помощью команды print. Решить задачу для латиницы.
# Пример вывода:
# Введите строку: The quick brown fox jumps over the lazy dog
# Строка является панграммой.
#
# def is_pangram(text):
#     alphabet = 'abcdefghijklmnopqrstuvwxyz' # Определяем латинский алфавит
#     normalized_text = text.lower().replace(' ', '')  # Приводим строку к нижнему регистру и удаляем пробелы
#     return set(alphabet).issubset(set(normalized_text))  # Проверяем, содержит ли строка все буквы алфавита
# user_input = input("Enter a string: ")
# if is_pangram(user_input):
#     print("Yes, it is a pangram")
# else:
#     print("No, it is not a pangram")
#
# 2. Напишите программу, которая запрашивает у пользователя строку и выводит на экран количество гласных и согласных
# букв в ней. Используйте функцию len() для подсчета количества букв. Выведите результат на экран с помощью команды
# print. Решить задачу для латиницы.
# Пример вывода:
# Введите строку: Hello World
# Количество гласных букв: 3
# Количество согласных букв: 7
#
# def count_vowels_and_consonants(text):
#     vowels = "aeiouAEIOU"
#     consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
#
#     vowel_count = 0
#     consonant_count = 0
#
#     for char in text:           # Проходим по всем символам в тексте
#         if char in vowels:      # Проверяем, гласная ли это буква
#             vowel_count += 1    # Увеличиваем счетчик гласных
#         elif char in consonants:    # Проверяем, согласная ли это буква
#             consonant_count += 1    # Увеличиваем счетчик согласных
#     return vowel_count, consonant_count   # Возвращаем найденные значения
# user_input = input("Введите строку: ")
# vowels, consonants = count_vowels_and_consonants(user_input)# Вызываем функцию и получаем количество гласных и согласных
#
# print(f"Количество гласных букв: {vowels}")
# print(f"Количество согласных букв: {consonants}")
