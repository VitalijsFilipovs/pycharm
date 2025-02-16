# numbers = (0, 1, 2, 3, 4, 53, 88)
# print(*numbers) # * - pechataet bez skobok
from inspect import stack

# numbers = [1, 2, 3, 4, 5]
# squared_numbers = [x**2 for x in numbers]
# print(squared_numbers) # [1, 4, 9, 16, 25]

# numbers = [1, 2, 3, 4, 5]
# squared_numbers = []
# for number in numbers:   # vozvedebie v kvadrat s ciklom for
#     squared_numbers.append(number ** 2) # Метод .append() добавления элемента в конец списка
# print(numbers)
# print(squared_numbers)

# numbers = [1, 2, 3, 4, 5]
# print(numbers)
# print([num ** 2 for num in numbers])

# numbers = [1, 2, 3, 4, 5]
# print(numbers)
# squared_numbers = [num ** 2 for num in numbers]
# print(squared_numbers)

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]]
# print(matrix[1])
# print(matrix[1][2])
# # print(matrix[1[2]]) # ne validno
# print([4, 5, 6][2])

# ----- # stack -Стек - это структура данных, работающая по принципу "последний вошел, первый вышел" (Last-In, First-Out).
# stack = []
# stack.append(1) # dobavlenie elementa v stek
# stack.append(2)
# stack.append(3)
# top_element = stack.pop() # izvlechenie verhnego elementa iz steka
# print(top_element)
# print(stack)

# numbers = [0, 1, 3, 14, 2, 7, 9, 8, 10]
# new = [20, 30]
# numbers.append(new)
# new.pop()
# numbers.pop()
# print(new)
# print(numbers)

# ------ ocheredj ------ Очередь - это структура данных, работающая по принципу "первый вошел,
# первый вышел" (First-In, First-Out).

# Класс deque из модуля collections предоставляет эффективную реализацию очереди в
# Python.

# from collections import deque
# queue = deque()
# queue.append(1) # Добавление элемента в очередь
# queue.append(2)
# first_element = queue.popleft() # Извлечение первого элемента из очереди
# print(first_element) # 1

# Сортировка # Метод sort() используется для сортировки элементов списка в порядке возрастания. Он
# изменяет сам список и не возвращает новый отсортированный список.

# my_list = [4, 2, 1, 3]
# my_list.sort()
# print(my_list) # [1, 2, 3, 4]

# my_list = [(2, 'b'), (1, 'a'), (2, 'c')]
# my_list.sort()
# print(my_list) # [(1, 'a'), (2, 'b'), (2, 'c')]

# a = ['бета', 'альфа', 'дельта', 'гамма']
# a.sort()
# print('Отсортированный список:', a)
# # Отсортированный список: ['альфа', 'бета', 'гамма', 'дельта']

# list comprehension
pairs = [(x,y) for x in range(3) for y in "ab"]
print(pairs)

# ekvivalent s ciklom for
pairs = []
for x in range(3):
    for y in "ab":
        pairs.append((x,y))
print(pairs)



