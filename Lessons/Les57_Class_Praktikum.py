# 1. Создать класс Car (машина) со следующими полями: model, year, color.
# 2. Создать 10 объектов этого класса, описывающих модели разных марок, лет и
# цветов.
# 3. Создать список из этих объектов.
# 4. Написать функцию, которая принимает список объектов класса Car и цвет и
# возвращает список машин этого цвета. Напечатать этот список, выводя
# название модели, год и цвет. Использовать filter и lambda функции.
from datetime import date


# class Car:
#     def __init__(self, model, year, color):
#         self.model = model  # Модель
#         self.year = year    # Год выпуска
#         self.color = color  # Цвет
#
#     def __str__(self):
#         return f"Модель: {self.model}, Год: {self.year}, Цвет: {self.color}"
#
# # Создание объектов класса Car
# car1 = Car('Toyota Camry', 2015, 'Green')
# car2 = Car('Honda Accord', 2018, 'Red')
# car3 = Car('Ford Mustang', 2020, 'Black')
# car4 = Car('Chevrolet Corvette', 2019, 'White')
# car5 = Car('Nissan Altima', 2017, 'Blue')
# car6 = Car('Hyundai Elantra', 2021, 'Silver')
# car7 = Car('BMW M3', 2021, 'Black')
# car8 = Car('Mercedes-Benz C-Class', 2020, 'Gray')
# car9 = Car('Audi A4', 2019, 'White')
# car10 = Car('Volkswagen Golf', 2022, 'Red')
#
# # Создание списка из объектов
# car_list = [car1, car2, car3, car4, car5, car6, car7, car8, car9, car10]
#
# # Функция для фильтрации автомобилей по цвету
# def filter_cars_by_color(cars, color):
#     return list(filter(lambda car: car.color.lower() == color.lower(), cars))
#
# # Пример использования функции
# color_to_filter = 'Red'
# filtered_cars = filter_cars_by_color(car_list, color_to_filter)
#
# # Печать отфильтрованных машин
# for car in filtered_cars:
#     print(car)

# 1. Создать класс Person с полями имя и дата рождения.
# 2. Создать 10 объектов этого класса с разными именами.
# 3. Создать класс Employee который содержит поле имя и возраст.
# 4. Написать функцию, которая из списка объекта класса Person создает список
# из объектов класса Employee, вычисляя возраст каждого Person по дате
# рождения. Подумать, где должна быть реализована функция, вычисляющая
# возраст по дате рождения. Варианты: в конструкторе класса Employee, в
# качестве глобальной функции, в качестве метода класса (какого?).
# Получившийся список должен содержать сотрудников, старше 18 лет.
# Использовать map и filter. У классов Person и Employee должны быть
# определены конструкторы. Реализация трансформации список персонов в
# сотрудников должна быть в одну строчку.
# 5. Вывести получившихся сотрудников на экран.
# 6. Используя функцию forAll() убедиться, что все сотрудники действительно
# старше 18 лет.

from datetime import date, datetime


class Person:
    def __init__(self, first_name, birthday):
        self.first_name = first_name
        self.birthday = birthday  # Дата рождения в формате date

    def __str__(self):
        return f'{self.first_name}, День рождения: {self.birthday}'

        # Метод для вычисления возраста

    def get_age(self):
        today = date.today()
        age = today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
        return age


class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Сотрудник: {self.name}, Возраст: {self.age}'

    # Создание 10 объектов класса Person


person1 = Person('Victor', date(1968, 8, 8))
person2 = Person('Alica', date(1985, 5, 15))
person3 = Person('Goga', date(2003, 10, 1))
person4 = Person('Tom', date(1990, 12, 25))
person5 = Person('Sara', date(1975, 4, 12))
person6 = Person('Mira', date(1999, 7, 20))
person7 = Person('John', date(1982, 3, 30))
person8 = Person('Ahmed', date(2000, 11, 11))
person9 = Person('Lana', date(1995, 2, 28))
person10 = Person('Mark', date(1980, 9, 9))

# Список всех персоны
person_list = [person1, person2, person3, person4, person5, person6, person7, person8, person9, person10]


# Функция для создания списка объектов Employee из объектов Person
def create_employees(persons):
    return list(
        filter(lambda emp: emp.age > 18,
               map(lambda p: Employee(p.first_name, p.get_age()), persons))
    )


# Создание списка сотрудников
employee_list = create_employees(person_list)

# Вывод сотрудников на экран
for employee in employee_list:
    print(employee)


# Убедитесь, что все сотрудники старше 18 лет
def for_all(employees):
    return all(employee.age > 18 for employee in employees)


print("Все сотрудники старше 18 лет:", for_all(employee_list))