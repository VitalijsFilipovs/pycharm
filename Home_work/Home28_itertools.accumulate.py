# Напишите программу, которая принимает список слов от пользователя и использует генераторное выражение (comprehension)
# для создания нового списка, содержащего только те слова, которые начинаются с гласной буквы. Затем программа должна
# использовать функцию map, чтобы преобразовать каждое слово в верхний регистр. В результате программа должна вывести
# новый список, содержащий только слова, начинающиеся с гласной буквы и записанные в верхнем регистре.
# from functools import reduce
#
#
# def list_sort():
#     words_list = input("Введите слова (через пробел): ").split()
#
#     vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')                 # Генераторное выражение для фильтрации слов, начинающихся с гласной буквы
#     filtered_words = [word for word in words_list if word.startswith(vowels)]
#
#     uppercased = list(map(lambda word: word.upper(), filtered_words))           # Используем map для преобразования слов в верхний регистр
#
#     print(f"Слова, начинающиеся с гласной буквы и в верхнем регистре: {uppercased}")
#     return uppercased
#
# list_sort()

#
#
# Напишите программу, которая принимает список чисел от пользователя и использует функцию reduce из модуля functools,
# чтобы найти произведение всех чисел в списке. Затем программа должна использовать функцию itertools.accumulate для
# накопления произведений чисел в новом списке. В результате программа должна вывести список, содержащий накопленные
# произведения.
#
#
# import functools
# import itertools
#
#
# def make_multiplier():
#     user_input = input("Введите список чисел (через пробел): ")
#     numbers = list(map(int, user_input.split()))
#
#     product = functools.reduce(lambda x, y: x * y, numbers) if numbers else 0       # Нахождение произведения всех чисел с помощью reduce
#
#     print(f"Произведение всех чисел: {product}")
#
#     accumulated_products = list(itertools.accumulate(numbers, lambda x, y: x * y))  # Накопление произведений с помощью accumulate
#
#     print(f"Накопленные произведения: {accumulated_products}")
#     return accumulated_products
#
# make_multiplier()