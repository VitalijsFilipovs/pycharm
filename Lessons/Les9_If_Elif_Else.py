# 1. Даны два целых числа a и b. Напишите программу, которая находит большее из
# двух чисел и печатает сообщение, какое число больше.
from calendar import weekday

# a, b = map(int, input("Enter Your pair of integers").split (","))
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# if a > b:
#     print("Your first number is greater than the second number")
# elif a == b:
#     print("Your first number is equal to the second number")
# else:
#     print("Your first number is less than the second number")
#---------------------------------
# 2. Напишите программу, которая находит наибольшее из трех чисел

# a = int(input("Enter your first number: "))
# b = int(input("Enter your second number: "))
# c = int(input("Enter your third number: "))
#
# # print(max(a,b,c)) # Vivodit naiboljsheje chislo
# if b < a > c:
#     print(f"number {a} is biger number")
# elif a < b > c:
#     print(f"number {b} is biger number")
# else:
#     print(f"number {c} is biger number")

# 3. Есть логическая переменная weekday. Напишите программу, которая выводит
# сообщение “рабочий день”, если переменная истинна и сообщение “выходной” -
# если ложна

#weekday = bool(int(input(f"1 - Eto rabochij, 0 - Eto vihodnoj: ")))
# weekday = int(input(f"1 - Eto rabochij, 2 - Eto vihodnoj: "))
# if weekday == 1:
#     print(f"Eto rabochij")
# elif weekday == 2:
#     print(f"Eto vihodnoj")
# else:
#     print(f"OShibka")

# 4. У нас есть две логические переменные: isWeekday, isVacation (выходной день и
# каникулы). Они могут принимать разные значения, всего 4 комбинации: true - true,
# true - false, false - false, false - true. Есть правило: мы можем поспать, если день не
# рабочий или мы на каникулах. Напишите программу, которая в зависимости от
# значений двух переменных печатает, можем ли мы поспать или нет. То есть для
# значений isWeekday = False и isVacation = False программа должна печатать
# “можете поспать”.

isWeekday = bool(int(input("Rabochij denj vvedite = 1, Ne rabochij = 0: ")))
isVacation = bool(int(input("Vvedite esli kanikuli = 1, uchimsja = 0: ")))
# if isWeekday == False or isVacation == True:
#     print(f"Ne rabochij! Mozhem pospatj")
# else:
#     print(f"Go to work!")

#--- vtoroj variant
if not isWeekday or isVacation:
    print(f"Sleep")
else:
    print("Work")


