Calculator


while True:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    operation = int(input("Enter the operation: 1. Plus 2. Minus 3. Division 4. Multiplication: "))
    if operation == 1:
         result = a + b
         print(f"The sum of yours numbers is : {result}")
    elif operation == 2:
        result = a - b
        print(f"The minus of yours numbers is : {result}")
    elif operation == 3:
        result = a / b
        print(f"The division of yours numbers is : {result}")
    elif operation == 4:
        result = a * b
        print(f"The multiplication of yours numbers is : {result}")
    else:
        print("Invalid operation")
    exit_cycle = input("Do you want to exit the program? (y/n): ")
    if exit_cycle == "y":
        break
print("See you later Aligator :)")

Programma ugadaj chislo

import time
import random

a = int(input("Enter a number from 0 to ?: "))
comp = random.randint(0,a)
start = time.time()
user = int(input(f"Ugadajte chislo ot 0 do {a}: "))
while user != comp:
    if user > comp:
        print("Vashe chislo boljshe zagadannogo")
    elif user < comp:
        print("Vashe chislo menshe zagadannogo")
    user = int(input(f"Ugadajte chislo ot 0 do {a}: "))
else:
    print("Vi molodec ugadali chislo!")
end = time.time()
result = end - start
print(f"Vi ugadali chislo za {round(result,1)} sekund")

