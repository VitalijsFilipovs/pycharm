##############  ITERATORI ############

# Итератор - это объект, который предоставляет последовательный доступ к
# элементам коллекции или последовательности.
# Итераторы реализуют два основных метода: __iter__(), который возвращает сам
# итератор, и __next__(), который возвращает следующий элемент в
# последовательности.
# Метод __next__() вызывается при каждой итерации, чтобы получить следующий
# элемент.

# nums = [1, 2, 3, 4, 5]
# it = nums.__iter__()  # chislam prisvaem iterator
# print(it)
# print(type(it))
# print(it.__next__())
# print(it.__next__())
# print("-------------")
# print(it.__next__())
# nums[3] = 0  # podmenili indeks cifri 4 (indeks 3) na NOLJ
# print(nums)
# #print(it.__next__())
# print(list(it))

# my_list = [1, 2, 3]
# it = my_list.__iter__()
# print(it)
# it = iter(my_list)
# print(it)
# print(it.__next__())
# print(next(it))
# print(next(it))
# print(next(it, None))
# print(next(it, None))
# print(next(it, None))

# my_list = [1, 2, 3]
# it = my_list.__iter__()
# print(it)
# iterator = iter(my_list)
# while True:
#     print(next(iterator))
#     try:
#         next(iterator)
#     except StopIteration:
#         break

################### GENERATORI ####################

# Генераторы - это функции, которые возвращают последовательность
# значений, сохраняя при этом свое состояние между вызовами.
# Ключевое слово yield используется в генераторах для определения значений,
# которые будут возвращены при каждом вызове метода __next__() / функции next().

# def my_generator():
#     yield 1
#     yield 2
#     yield 3
# gen = my_generator()
# print(gen)
# print(type(gen))
# print(next(gen)) # Выводит 1
# print(next(gen)) # Выводит 2
# print(next(gen)) # Выводит 3

#return v generatore

# def process_data(data):
#     for i in data:
#         if i == "STOP":
#             return "Processing stopped"
#         yield i
#
# gen = process_data(["a", "b", "c", "STOP", "d"])
# for item in gen:
#     print(item)



# def process_data(data):
#     for i in data:
#         if i == "STOP":
#             return "Processing stopped"
#         yield i
#
# gen = process_data(["a", "b", "c", "STOP", "d"])
#
# for item in gen:
#     try:
#         print(item)
#     except StopIteration as e:
#         print(e.value)

########### ----------------------- ################
# Генераторные выражения - это компактный способ создания генераторов в
# Python, используя синтаксис списковых включений.
# Они позволяют создавать генераторы без явного определения функции с ключевым
# словом yield.

# my_generator = (x ** x for x in range(10))
# for item in my_generator:
#     print(item)

# # Запрашиваем у пользователя ввод числа N
# N = int(input("Введите число N: "))
#
# # Генератор, который возвращает квадраты чисел от 1 до N
# my_generator = (x**2 for x in range(1, N + 1))
#
# # Итерация по генератору и вывод значений
# for item in my_generator:
#     print(item)







