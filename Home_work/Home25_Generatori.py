# 1. Напишите функцию find_longest_word, которая будет принимать список слов и возвращать самое длинное слово из списка.
# Аннотируйте типы аргументов и возвращаемого значения функции.
# Пример вызова функции и ожидаемого вывода:
#
# from typing import List
#
# def find_longest_word(words: List[str]) -> str:
#     if not words:                           # Проверяем, что список не пустой
#         return ''
#
#     longest_word = max(words, key=len)      # Находим самое длинное слово
#     return longest_word
#
# words = ["apple", "banana", "cherry", "dragonfruit"]
# result = find_longest_word(words)
#
# print(result)                               # Ожидаемый вывод: "dragonfruit"
#
# ----------------
#
# 2. Напишите программу, которая будет считывать данные о продуктах из файла и использовать аннотации типов для
# аргументов и возвращаемых значений функций. Создайте текстовый файл "products.txt", в котором каждая строка будет
# содержать информацию о продукте в формате "название, цена, количество". Например:
#
# Apple, 1.50, 10
#
# Banana, 0.75, 15
#
# В программе определите функцию calculate_total_price, которая будет принимать список продуктов и возвращать общую
# стоимость. Продумайте, какая аннотация должна быть у аргумента! Считайте данные из файла, разделите строки на
# составляющие и создайте список продуктов. Затем вызовите функцию calculate_total_price с этим списком и
# выведите результат.
#
#
# products.txt
#
# Apple, 1.50, 10
# Banana, 0.75, 15
# Kivi, 0.50, 20
# Avocado, 1.50, 25
#
# from typing import List, Tuple
#
# def read_products_from_file(filename: str) -> List[Tuple[str, float, int]]:
#     products = []
#     with open(filename, 'r') as file:
#         for line in file:
#             name, price, quantity = line.strip().split(',')
#             products.append((name, float(price), int(quantity)))    # Добавляем кортеж с данными о продукте
#     return products
#
# def calculate_total_price(products: List[Tuple[str, float, int]]) -> float:
#     total_price = 0.0
#     for name, price, quantity in products:
#         total_price += price * quantity                             # Умножаем цену на количество
#     return total_price
#
# filename = 'products.txt'                                           # Читаем данные из файла
# products = read_products_from_file(filename)
#
# total_price = calculate_total_price(products)                       # Вычисляем общую стоимость
#
# print(f"Общая стоимость продуктов: {total_price:.2f}")
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
