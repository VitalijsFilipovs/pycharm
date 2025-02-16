# hash_value = hash("hello")
# print(hash_value) # Выводит целочисленное значение хэша
#
# print(hash("hello"))
#
# print(hash("hello2-2, bbbvvg996688"))
#
# print(hash(True))
#
# print(hash(1))
# #1
# print(hash(1.0))
# #1
# print(hash('1'))
# #-3723884734378080930
# print(hash('строка'))
# #295037195106125010
# print(hash((1,2,3)))
# #2528502973977326415
#
# s = {"hello", "python", "hi", True, 1, 1.0}
# print(s)
#
# # s1 = {2, 5}
# # s2 = {1, 5, 6}
# set1 = {1, 2, 3}
# set2 = {2, 3, 4}
# intersection = set1.intersection(set2) # peresechenie
# union = set1.union(set2)               # objedinenije
# difference = set1.difference(set2)     # razlichija
# symmetric_difference = set1.symmetric_difference(set2)   # simetrichnije razlichija
# print(intersection) # Выводит {2, 3}
# print(union) # Выводит {1, 2, 3, 4}
# print(difference) # Выводит {1}
# print(symmetric_difference) # Выводит {1, 4}
#
# set_nums = {2, 3, (1, 2)}
# print(hash(set_nums))

# 3. Какой будет результат выполнения фрагмента кода?
# users = {"Tom", "Bob", "Alice"}
# users2 = {"Sam", "Kate", "Bob"}
# users3 = users.intersection(users2)
# print(users3)

# set_nums = {2, 3, 4}
# print(type(set_nums))
# print({3} in set_nums)
#
# my_set = {1, 2, 3}
# empty_set = set()
# print(len(my_set)) # Выводит размер множества
# print(2 in my_set) # Выводит True, так как элемент 2 содержится во множестве

# Стать IT-шником может каждый ICH
# Добавление/удаление элемента во множество
# Добавить элемент в множество:
# ● с помощью функции add
# Удалить элемент
# ● с помощью функций remove, discard
# Очистить множество
# ● с помощью функции clear

# Добавление/удаление элемента во множество
# my_set = {1, 2, 3}
# print(my_set)
# my_set.add(4) # {1, 2, 3, 4}
# print(my_set)
# my_set.remove(2) # {1,3,4}
# print(my_set)
# my_set.discard(5) # ничего не изменится
# print(my_set)
# my_set.clear()
# print(my_set) # Выводит пустое множество

# Сравнение множеств
# Множества можно сравнить на:
# ● равенство (==)
# ● неравенство (!=)
# ● подмножество (<=, <)
# ● надмножество (>=, >)

set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1 == set2) # Выводит False
print(set1 < set2) # Выводит False, set1 не является подмножеством set2

# Итерирование по множеству с помощью цикла for
my_set = {1, 2, 3}
for item in my_set:
 print(item) # Выводит каждый элемент множества



















