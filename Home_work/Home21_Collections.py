# 1. Напишите программу, которая подсчитывает количество вхождений каждого слова в тексте и выводит на экран наиболее
# часто встречающиеся слова. Для решения задачи используйте класс Counter из модуля collections. Создайте функцию
# count_words, которая принимает текст в качестве аргумента и возвращает словарь с количеством вхождений каждого слова.
# Выведите наиболее часто встречающиеся слова и их количество.
# Пример вывода:
# Введенный текст: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sed lacinia est.
# sed: 2
# Lorem: 1
#
# from collections import Counter
#
# def count_words(text):
#     """Подсчитывает количество вхождений каждого слова в тексте."""
#     words = text.lower().split()  # Приводим текст к нижнему регистру и разбиваем на слова
#     counter = Counter(words)  # Подсчитываем количество вхождений каждого слова
#     return counter  # Возвращаем объект Counter
#
# def print_most_common_words(text, n=20):
#     """Подсчитывает слова и выводит n наиболее часто встречающихся слов и их количество."""
#     word_count = count_words(text)  # Вызываем функцию для подсчета слов
#     words = word_count.most_common(n)  # Получаем n наиболее распространенных слов
#     for word, count in words:  # Выводим каждое слово и его количество
#         print(f"{word}: {count}")
#
# if __name__ == '__main__':
#     text = input("Input text: ")  # Запрашиваем текст у пользователя
#     print("Most common words:")
#     print_most_common_words(text, 20)  # Выводим наиболее часто встречающиеся слова
#
# 2. Напишите программу, которая создает именованный кортеж Person для хранения информации о человеке,
# включающий поля name, age и city. Создайте список объектов Person и выведите информацию о каждом человеке на экран.
# Пример вывода:
# Name: Alice, Age: 25, City: New York
# Name: Bob, Age: 30, City: London
# Name: Carol, Age: 35, City: Pari
#
# def tuple_to_list():
#
#     my_tuple1 = (1, 'Alice', 25, 'New York')    # Создаем кортежи с данными о людях
#     my_tuple2 = (2, 'Bob', 30, 'London')
#     my_tuple3 = (3, 'Carol', 35, 'Paris')
#
#     people = [my_tuple1, my_tuple2, my_tuple3]  # Создаем список кортежей
#
#     for person in people:                       # Выводим информацию о каждом человеке
#         print(f'Name: {person[1]}, Age: {person[2]}, City: {person[3]}')
#
#     return people
#
# tuple_to_list()                                 # Вызов функции
#
# 3. Напишите программу, которая принимает словарь от пользователя и ключ, и возвращает значение для указанного ключа с
# использованием метода get или setdefault. Создайте функцию get_value_from_dict, которая принимает словарь и ключ в
# качестве аргументов, и возвращает значение для указанного ключа, используя метод get или setdefault в зависимости от
# выбранного варианта. Выведите полученное значение на экран.
# Пример словаря:
# my_dict = {'apple': 5, 'banana': 6, 'cherry': 7}
# Пример вывода:
# Введите ключ для поиска: banana
# Использовать метод get (y/n)? y
# Значение для ключа 'banana': 6
#
# def get_value_from_dict():
#     my_dict = {'apple': 5, 'banana': 6, 'cherry': 7}
#
#     key = input("Введите ключ для поиска: ")                            # Запрашиваем ключ для поиска
#
#     use_get = input("Использовать метод get (y/n)? ").strip().lower()   # Запрашиваем, использовать ли метод get
#
#     if use_get == 'y':                                                  # Используем метод get для получения значения
#
#         value = my_dict.get(key, None)                                  # Возвращает None, если ключ не найден
#         if value is not None:
#             print(f"Значение для ключа '{key}': {value}")
#         else:
#             print(f"Ключ '{key}' не найден в словаре.")
#     else:                                                               # Используем метод setdefault для получения значения
#
#         value = my_dict.setdefault(key, 0)                              # Устанавливает значение по умолчанию 0, если ключ не найден
#         print(f"Значение для ключа '{key}': {value}")
#
# get_value_from_dict()