import time
import random
# Zagolovok cikla
# while True:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     if num1 > num2:
#         print(f"{num1} boljshe {num2}")
#     elif num2 > num1:
#         print(f"{num2} boljshe {num1}")
#     else:
#         print("Chisla ravni")
#
#     ask = input("Do you want to continue? (y/n): ").lower()
#     if ask == "n":
#         break

#---Summa posledovateljnosti---Iteracija
# Rabota cikla nazivaetsja ITERACIEJ
# num = int(input("\nEnter a number: "))   # Konechnoe chislo v summe
# s = 0           # Dlja hranenija vicheslennoj summi
# i = 1           # Znachenie tekushego slagaemogo
# while i <= num: # Zagolovok (telo) cikla
#     s += i      # s = s+i
#     i += 1      # i = i+1
#     print(s)
# print(f"Cikl zavershon. Summa ravna s = {s}.")

# ---Cikle s diapazonom---
# num = int(input("\nEnter a number: "))   # Konechnoe chislo v summe
# s = 0           # Dlja hranenija vicheslennoj summi
# i = 1           # Znachenie tekushego slagaemogo
# while i <= num and i <= 50: # Zagolovok (telo) cikla
#      s += i     # s = s+i
#      i += 1     # i = i+1
#      print(s)
# print(f"Cikl zavershon. Summa ravna s = {s}.")

#----Programma v umenshenie----
# n = -10
# i = -1
# while i >= n:
#     print(i)
#     i -= 1

#----Parolj abc----
# pass_true = "abc"
# ps = ""
# while ps != pass_true:
#     ps = input("Enter your password: ")
#
# print(f"Your password is: {ps}. Enter complited!")

#---Programma vvoda parolja---
# Установим правильный пароль
# correct_password = "123456"
# attempts = 0
# max_attempts = 4
#
# # Цикл для попыток ввода пароля
# while attempts < max_attempts:
#     user_input = input("Введите пароль: ")
#     if user_input == correct_password:
#         print("Пароль верный! Доступ разрешен.")
#         break  # Выход из цикла, если пароль верный
#     else:
#         attempts += 1
#         print(f"Неверный пароль. У вас осталось {max_attempts - attempts} попыток.")
#
# # Проверка, исчерпаны ли все попытки
# if attempts == max_attempts:
#     print("Вы исчерпали все попытки ввода пароля. Доступ запрещен.")

# num = int(input("Enter a number: "))
# i = 1
# while i <= num:
#     if i % 3 == 0:
#         print(i)
#     i+=1

# i = 0
# while True:
#     i += 1
#     break
#
# print("end loop")

# ---- Programma skladivaet nechetnie chisla------
# s = 0
# d = 1
# while d != 0:
#     d = int(input("Enter int number: "))
#     if d % 2 == 0:
#         continue   # Prodolzhaet programmku
#     s += d
#     print(f"s = {s}")
# print("end loop")


# s = 1/2 + 1/3 + 1/4 + 1/5 + 1/0
# s = 0
# i = -9 # i - eto schetchik
# while i < -1:
#     if i == 0:
#             break
#     s += 1/i
#     i += 1
# else:
#     print("Summa vicislenna korrektno")
# print(s)

# ---- Schitaet skoljko vremja rabotala programma---
# start_time = time.time()
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# summ = int(input(f"{num1} + {num2} = "))
# print(summ)
# end_time = time.time()
# result_time = end_time - start_time
# print(round(result_time, 2))

# Vichisljaet psevdosluchajnoe chislo
# s = random.randint(1, 100)
# print(s)

# Vivodit sluchajnoe chislo ot nulja do edinici
# a = random.random()
# print(a)

# b = random.randrange(1,10, step=3)
# print(b)

#-- Viberaet randomnoe imja
# list_names = ["bob", "jim", "helga", "john"]
# one_name = random.choice(list_names)
# print(one_name)