# 1. Создайте класс Rectangle для представления прямоугольника. Класс должен иметь атрибуты width (ширина) и height
# (высота), а также метод calculate_area(), который вычисляет площадь прямоугольника. Затем создайте экземпляр класса
# Rectangle с заданными значениями ширины и высоты и выведите его площадь.
#
# class Rectangle:                                # Конструктор класса Rectangle.
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def calculate_area(self):                   # Метод для вычисления площади прямоугольника.
#         return self.width * self.height
#
# my_obj = Rectangle(100, 100)        # Создаём экземпляр класса Rectangle с шириной 100 и высотой 100
# print(my_obj.calculate_area())
#
#
#
# 2. Создайте класс Student для представления студента. Класс должен иметь атрибуты name (имя) и age (возраст), а также
# метод display_info(), который выводит информацию о студенте. Затем создайте экземпляр класса Student с заданным именем
# и возрастом и вызовите метод display_info().
#
# class Student(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def display_info(self):                         # метод display_info(), который выводит информацию о студенте
#         return "Name: {}\nAge: {}".format(self.name, self.age)
#
# my_student = Student("John", 25)         # экземпляр класса Student с заданным именем и возрастом
# print(my_student.display_info())
