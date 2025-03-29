# 1. Создайте класс Rectangle для представления прямоугольника.
# Класс должен иметь атрибуты width (ширина) и height (высота) со значениями по умолчанию, а также методы
# calculate_area() для вычисления площади прямоугольника и calculate_perimeter() для вычисления периметра прямоугольника.
# Переопределить методы __str__, __repr__.
# Затем создайте экземпляр класса Rectangle и выведите информацию о нем,
# его площадь и периметр.
#
# class Rectangle:                                # Конструктор класса Rectangle.
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def calculate_area(self):                   # Метод для вычисления площади прямоугольника.
#         return self.width * self.height
#
#     def calculate_perimeter(self):              # Метод для вычисления периметра прямоугольника.
#         return self.width * 2 + self.height * 2#
#
#     def __str__(self):                          # Переопределить методы __str__.
#         return "Rectangle(width={}, height={})".format(self.width, self.height)
#
#     def __repr__(self):                         # Переопределить методы __repr__.
#         return "Rectangle(width={}, height={})".format(self.width, self.height)
#
# my_obj = Rectangle(100, 100)        # Создаём экземпляр класса Rectangle с шириной 100 и высотой 100
# print(my_obj)
# print(f"calculate_area: {my_obj.calculate_area()}")
# print(f"calculate_perimeter: {my_obj.calculate_perimeter()}")
#
# 2. Создайте класс BankAccount для представления банковского счета. Класс должен иметь атрибуты account_number
# (номер счета) и balance (баланс), а также методы deposit() для внесения денег на счет и withdraw() для снятия денег
# со счета. Затем создайте экземпляр класса BankAccount, внесите на счет некоторую сумму и снимите часть денег.
# Выведите оставшийся баланс. Не забудьте предусмотреть вариант, при котором при снятии баланс может стать меньше нуля.
# В этом случае уходить в минус не будем, вместо чего будем возвращать сообщение "Недостаточно средств на счете".
#
# class BankAccount:
#     def __init__(self, account_number, balance=0):
#         self.balance = balance
#         self.account_number = account_number
#
#     def deposit(self, amount):                  # Метод для внесения денег на счет.
#         self.balance += amount
#         return f"Успешно внесено: {amount}. Текущий баланс: {self.balance}."
#
#     def withdraw(self, amount):                 # Метод для снятия денег со счета.
#         if amount > self.balance:               # Проверка на наличие достаточно средств
#             return "Недостаточно средств на счете."
#         elif amount <= 0:                       # Проверка, чтобы сумма снятия была положительной
#             return "Сумма для снятия должна быть положительной."
#         else:
#             self.balance -= amount              # Уменьшаем баланс на сумму снятия
#             return f"Успешно снято: {amount}. Текущий баланс: {self.balance}."
#
# my_account = BankAccount("ID_1533", 1000)
#
# # Вносим деньги на счет
# deposit_message = my_account.deposit(500)  # Вносим 500
# print(deposit_message)
#
# # Снимаем деньги со счета
# withdraw_message = my_account.withdraw(300)  # Снимаем 300
# print(withdraw_message)
#
# # Попробуем снять деньги, чтобы проверить на недостаток средств
# withdraw_message2 = my_account.withdraw(1500)  # Пытаемся снять 1500
# print(withdraw_message2)
#
# print(f"Оставшийся баланс: {my_account.balance}")
