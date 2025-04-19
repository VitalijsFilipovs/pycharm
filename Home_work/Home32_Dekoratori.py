# 1. Реализовать класс Counter, который представляет счетчик.
# Класс должен поддерживать следующие операции:
# - Увеличение значения счетчика на заданное число (оператор +=)
# - Уменьшение значения счетчика на заданное число (оператор -=)
# - Преобразование счетчика в строку (метод __str__)
# - Получение текущего значения счетчика (метод __int__)
# Пример использования:
# counter = Counter(5)
# counter += 3
# print(counter)  # Вывод: 8
# counter -= 2
# print(int(counter))  # Вывод: 6

# class Counter:
#     def __init__(self, counter=0):
#         self.counter = counter
#
#     def __add__(self, count):
#         self.counter += count
#         return self         # Возвращаем текущий объект Counter
#
#     def __sub__(self, count):
#         self.counter -= count
#         return self         # Возвращаем текущий объект Counter
#
#     def __str__(self):
#         return f"Вывод: {self.counter}"     # Возвращаем строку с текущим значением счётчика
#
#     def __int__(self):
#         return self.counter                 # Возвращаем текущее значение счётчика как целое число
#
#
# my_counter = Counter(counter=5)             # Создание экземпляра Counter
#
# # Используем оператор + для добавления
# my_counter += 3
# print(my_counter)
#
# # Используем оператор - для вычитания
# my_counter -= 2
# print(my_counter)

# 2. Реализовать класс Email, представляющий электронное письмо. Класс должен
# поддерживать следующие операции:
# - Сравнение писем по дате (операторы <, >, <=, >=, ==, !=)
# - Преобразование письма в строку (метод __str__)
# - Получение длины текста письма (метод __len__)
# - Получение хеш-значения письма (метод __hash__)
# - Проверка наличия текста в письме (метод __bool__)
# Пример использования:

# email1 = Email("john@example.com", "jane@example.com", "Meeting", "Hi Jane, let's have a meeting tomorrow.", "2022-05-10")
# email2 = Email("jane@example.com", "john@example.com", "Re: Meeting", "Sure, let's meet at 2 PM.", "2022-05-10")
# email3 = Email("alice@example.com", "bob@example.com", "Hello", "Hi Bob, how are you?", "2022-05-09")
#
# print(email1)  # Вывод:
#
# """
# From: john@example.com
#
# To: jane@example.com
#
# Subject: Meeting
#
# Hi Jane, let's have a meeting tomorrow.
# """
# print(len(email2))  # Вывод: 24
# print(hash(email3))  # Вывод: -920444056
# print(bool(email1))  # Вывод: True
# print(email2 > email3)  # Вывод: True

# class Email:
#     def __init__(self, from_email, to_email, subject, body, date):
#         self.from_email = from_email        # Адрес отправителя
#         self.to_email = to_email            # Адрес получателя
#         self.subject = subject              # Тема письма
#         self.body = body                    # Текст письма
#         self.date = date                    # Дата письма
#
#     def __str__(self):
#         return f"From: {self.from_email}\n\nTo: {self.to_email}\n\nSubject: {self.subject}\n\n{self.body}"
#
#     def __len__(self):
#         return len(self.body)               # Возвращаем длину тела письма
#
#     def __hash__(self):
#         return hash(self.to_email)          # Хэшируем по адресу получателя
#
#     def __bool__(self):
#         return bool(self.to_email)          # Письмо считается истинным, если есть получатель
#
#     def __eq__(self, other):
#         if not isinstance(other, Email):
#             return NotImplemented
#         return self.date == other.date               # Сравниваем по дате
#
#     def __ne__(self, other):
#         return not self.__eq__(other.date)           # Неравенство по дате
#
#     def __gt__(self, other):
#         if not isinstance(other, Email):
#             return NotImplemented
#         return self.date > other.date           # Сравниваем по дате
#
#     def __lt__(self, other):
#         if not isinstance(other, Email):
#             return NotImplemented
#         return self.date < other.date           # Сравниваем по дате
#
#     def __ge__(self, other):
#         return self > other or self == other    # Проверка на большее или равное
#
#     def __le__(self, other):
#         return self < other or self == other    # Проверка на меньшее или равное
#
# # Примеры использования
# email1 = Email("jane@example.com", "john@example.com", "Meeting", "Hi Jane, let's have a meeting tomorrow.", "2022-05-10")
# email2 = Email("john@example.com", "jane@example.com", "Re: Meeting", "Sure, let's meet at 2 PM.", "2022-05-11")
# email3 = Email("alice@example.com", "bob@example.com", "Hello", "Hi Bob, how are you?", "2022-05-09")
#
# # Выводим информацию о письмах
# print(email1)
# print(len(email2))  # Вывод: 24
# print(hash(email3))  # Вывод: -920444056
# print(bool(email1))  # Вывод: True
# print(email2 > email3)  # Вывод: True