# ----- NE DEKORATOR ----- #
# def decorator(func):
#         print("Sejchas vipolnim funkciju")
#         func()
#         print("Funkcija vipolnena")
###############################################################

# ----- DEKORATOR ----- #

# def decorator(func):
#     def wrapper():
#         print("Sejchas vipolnim funkciju")
#         func()
#         print("Funkcija vipolnena")
#     return wrapper
#
#
# @decorator
# def my_function():
#     print("my_function")
#
# my_function()
#
# print("----------------------------")
#
# @decorator
# def my_another_function():
#     print("my_another_function")
#
# my_another_function()
#
# print("----------------------------")
#
# result =decorator(my_function)
# result()
#
# print("----------------------------")
############################################################

# def uppercase_decorator(function):
#     def wrapper(*args, **kwargs):
#         func = function(*args, **kwargs)
#         make_uppercase = func.upper()
#         return make_uppercase
#     return wrapper
#
# @uppercase_decorator
# def return_hello():
#     return "Hello World!"
#
# print(return_hello())
#
# print("----------------------------")
#
# @uppercase_decorator
# def return_person(person):
#     return f"Hello {person}!"
#
# print(return_person("Bob"))

####################################################
# ----- PARAMETRICHESKIJ DEKORATOR -----

# def param_decorator(ask_name):
#     def decorator(func):
#         def wrapper():
#             if ask_name:
#                 name=input("Как вас зовут? ")
#             result = func()
#             if ask_name:
#                 print(f"Ваше имя {name}, ваш возраст - {result}")
#             else:
#                 print(f"Ваш возраст - {result}")
#         return wrapper
#     return decorator
#
#
# @param_decorator(True)
# def ask_age():
#     age=input("Сколько вам лет? ")
#     if age.isdigit():
#         return age
#     return "неизвестно"
# ask_age()

#################################################################

# ------ Декоратор @functools.wraps ------

# import functools
#
# def decorator(func):
#     @functools.wraps(func)
#     def wrapper():
#         print(f"documentation: :")
#         print(func.__doc__)
#         print(f"Sejchas vipolnim funkciju '{func.__name__}'")
#         func()
#         print("Funkcija vipolnena\n")
#
#     return wrapper
#
# @decorator
# def my_function():
#     """
#     my_function documentation
#     """
#     print("my_function")
#
# my_function()
#
# print("-------------------")
#
# print(f"documentation: :")
# print(my_function.__doc__)
# print(f"Sejchas vipolnim funkciju {my_function.__name__}")

###################################################################

# def border_decorator(func):
#     def wrapper():
#         print("*" * 100)
#         func()
#         print("*" * 100)
#     return wrapper
#
# def repeat_decorator(func):
#     def wrapper():
#         for i in range(10):
#             func()
#     return wrapper
#
# @border_decorator
# @repeat_decorator
#
# def print_line():
#     print("-" * 100)
#
# print_line()






























