10. Модуль collections

from collections import Counter, defaultdict, namedtuple, deque

# Подсчет элементов с помощью Counter
def count_elements():
    elements = input("Введите элементы через пробел: ").split()  # Ввод элементов
    counter = Counter(elements)  # Подсчитываем элементы
    print(f"Подсчет элементов: {counter}")  # Вывод подсчета
    return counter  # Возвращаем Counter

# Создание defaultdict
def create_defaultdict():
    my_dict = defaultdict(int)  # Создаем defaultdict с типом int
    my_dict['a'] += 1  # Увеличиваем значение по ключу 'a'
    my_dict['b'] += 2  # Увеличиваем значение по ключу 'b'
    print(f"Defaultdict: {my_dict}")  # Вывод defaultdict
    return my_dict  # Возвращаем defaultdict

# Создание namedtuple
def create_namedtuple():
    Point = namedtuple('Point', ['x', 'y'])  # Создаем namedtuple
    point = Point(10, 20)  # Создаем экземпляр
    print(f"Namedtuple Point: {point}")  # Вывод namedtuple
    return point  # Возвращаем namedtuple

# Использование deque
def use_deque():
    my_deque = deque()  # Создаем deque
    my_deque.append(1)  # Добавляем элемент в конец
    my_deque.appendleft(2)  # Добавляем элемент в начало
    print(f"Deque: {my_deque}")  # Вывод deque
    return my_deque  # Возвращаем deque

# Подсчет уникальных элементов с помощью Counter
def count_unique_elements():
    elements = input("Введите элементы через пробел: ").split()  # Ввод элементов
    counter = Counter(elements)  # Подсчитываем элементы
    unique_count = sum(1 for count in counter.values() if count == 1)  # Подсчет уникальных
    print(f"Количество уникальных элементов: {unique_count}")  # Вывод количества
    return unique_count  # Возвращаем количество уникальных

# Создание defaultdict с списками
def create_defaultdict_with_lists():
    my_dict = defaultdict(list)  # Создаем defaultdict с типом list
    my_dict['a'].append(1)  # Добавляем элемент в список по ключу 'a'
    my_dict['a'].append(2)  # Добавляем еще один элемент
    print(f"Defaultdict с списками: {my_dict}")  # Вывод defaultdict
    return my_dict  # Возвращаем defaultdict

# Использование deque для очереди
def use_deque_as_queue():
    my_deque = deque()  # Создаем deque
    my_deque.append(1)  # Добавляем элемент в конец
    my_deque.append(2)  # Добавляем элемент в конец
    first = my_deque.popleft()  # Удаляем элемент из начала
    print(f"Deque как очередь: {my_deque}, удаленный элемент: {first}")  # Вывод deque и удаленного элемента
    return my_deque  # Возвращаем deque

# Использование namedtuple для хранения данных
def use_namedtuple_for_data():
    Person = namedtuple('Person', ['name', 'age'])  # Создаем namedtuple
    person = Person(name='Alice', age=30)  # Создаем экземпляр
    print(f"Namedtuple Person: {person}")  # Вывод namedtuple
    return person  # Возвращаем namedtuple

# Подсчет частоты слов в предложении
def count_word_frequency():
    sentence = input("Введите предложение: ")  # Ввод предложения
    words = sentence.split()  # Разбиваем на слова
    counter = Counter(words)  # Подсчитываем частоту слов
    print(f"Частота слов: {counter}")  # Вывод частоты
    return counter  # Возвращаем Counter