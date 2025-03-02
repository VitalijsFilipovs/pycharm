# d = {1: [1, 2, 3], 2: None}
# l = {1,2,3}
# print(l)
# print(d)
#
# if 4 in d:
#     print(d[4])

# Метод get

# my_dict = {"apple": 5, "banana": 2, "orange": 8}
# print(my_dict.get("apple")) # Выводит 5
# print(my_dict.get("grape")) # Выводит None
# print(my_dict.get("grape", 0)) # Выводит 0, так как клĀча "grape" нет в словаре
# print(my_dict.get("apple", 15))

# Метод setdefault

# my_dict = {"apple": 5, "banana": 2, "orange": 8}
# print(my_dict.setdefault("apple", 10)) # Выводит 5
# print(my_dict.setdefault("grape", 15)) # Выводит 15, добавлāет новуĀ пару клĀч-значение
# print(my_dict) # Выводит {'apple': 5, 'banana': 2, 'orange': 8, 'grape': 15}

# КЛАСС ORDEREDDICT. ПОНЯТИЕ LRUКЕША

# from collections import OrderedDict
#
# ordered_dict = OrderedDict()
# ordered_dict["apple"] = 5
# ordered_dict["banana"] = 2
# ordered_dict["orange"] = 8
# print(ordered_dict)

####   LRU cash   #####

# from collections import OrderedDict
#
#
# def lru_cache(capacity, cache, key, value):
#     # Если ключ уже существует, обновляем значение и перемещаем элемент в конец словаря
#     if key in cache:
#         cache.pop(key)  # Удаляем старую запись
#     elif len(cache) >= capacity:
#         cache.popitem(last=False)  # Удаляем первый элемент (самый старый)
#
#     # Добавляем новый элемент или обновляем существующий
#     cache[key] = value
#
#
# # Устанавливаем емкость кэша
# capacity = 3
# cache = OrderedDict()
#
# # Добавляем элементы в кэш
# lru_cache(capacity, cache, "key1", "value1")
# lru_cache(capacity, cache, "key2", "value2")
# lru_cache(capacity, cache, "key3", "value3")
#
# # Выводим текущее состояние кэша
# print(cache)  # Выводит: OrderedDict([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3')])
#
# # Обновляем значение для "key2"
# lru_cache(capacity, cache, "key2", "new_value2")
# print(cache)  # Выводит: OrderedDict([('key1', 'value1'), ('key3', 'value3'), ('key2', 'new_value2')])
#
# # Добавляем новый элемент, что приводит к удалению "key1"
# lru_cache(capacity, cache, "key4", "value4")
# print(cache)  # Выводит: OrderedDict([('key3', 'value3'), ('key2', 'new_value2'), ('key4', 'value4')])

# OrderedDict({'key1': 'value1', 'key2': 'value2', 'key3': 'value3'})
# OrderedDict({'key1': 'value1', 'key3': 'value3', 'key2': 'new_value2'})
# OrderedDict({'key3': 'value3', 'key2': 'new_value2', 'key4': 'value4'})

###### КЛАСС DEFAULTDICT  #######
# Класс defaultdict представляет словарь, который автоматически создает значения для
# несуществующих ключей при первом обращении.

# from collections import defaultdict
# my_dict = defaultdict(int)
# my_dict["apple"] = 5
# print(my_dict["apple"]) # Выводит 5
# print(my_dict["banana"]) # Выводит 0, так как ключа "banana" нет, но defaultdict автоматически создал его со значением 0

######   КЛАСС COUNTER    #######
# Класс Counter предоставляет удобную структуру для подсчета элементов в
# итерируемом объекте.

# from collections import Counter
# my_list = [1, 2, 3, 1, 2, 3, 1, 2, 4, 5, 4, 3]
# my_counter = Counter(my_list)
# print(my_counter) # Выводит Counter({1: 3, 2: 3, 3: 3, 4: 2, 5: 1})
# print(my_counter[1]) # Выводит 3, так как элемент "1" встречается 3 раза в списке

###### ИМЕНОВАННЫЕ КОРТЕЖИ ######
# Именованные кортежи namedtuple представляют удобную структуру для создания
# простых классов без методов, которые используются только для хранения данных.

# from collections import namedtuple # Создаем именованный кортеж с именами полей 'name' и 'age'
# Person = namedtuple('Person', ['name', 'age'])
# person1 = Person(name='Alice', age=30)
# print(person1.name)
# print(person1.age)

####### ВВЕДЕНИЕ В СЕРИАЛИЗАЦИЮ/ ДЕСЕРИАЛИЗАЦИЮ  ######
# Модуль json предоставляет функции для сериализации и десериализации данных в
# формате JSON.

# import json
# # Сериализация Python-объекта в JSON-строку
# data = {"name": "John", "age": 25, "city": "New York"}
# json_str = json.dumps(data)
# print(json_str) # Выводит '{"name": "John", "age": 25, "city": "New York"}'
# # Десериализация JSON-строки в Python-объект
# json_str = '{"name": "John", "age": 25, "city": "New York"}'
# data = json.loads(json_str)
# print(data["name"]) # Выводит 'John'







