import math                   # as m kak math
from math import factorial  # vstavljaet faktorial iz math
import factorial            # vstavljaet toljko factorial
print(math.pi)              # 3.141592653589793
print(math.ceil(-3.14))     # -3
print(math.ceil(3.14))      # 4
print(math.floor(3.14))     # 3
print(math.factorial(3))    # 6
print(math.factorial(4))    # 24
print(factorial(3))         # 6
print(math.trunc(3.14))     # 3
print(int(3.14))            # 3
print(math.log(2.7))        # 0.9932517730102834
print(math.log10(100))      # 2.0
-----------------
x = int(input("Vvedite chislo: "))
print(abs(x))                       # Funkcija ABS vivodit absoljutnoe znachenie chisla
-----------------
a, b, c, d, e = map(int, input("Vvedite 5 celih chisel: ").split())  # Vvesti 5 celih chisel
print(min(a, b, c, d, e))    # Minimaljnoe chislo
print(max(a, b, c, d, e))    # Maksimaljnoe chislo
print(sum((a, b, c, d, e)))  # Summa chisel # Funkcija sum trebuet dvojnih skobok (())
-----------------
a, b = map(int, input("Vvedite 2 kateta: ").split())
c = math.sqrt(a**2 + b**2)
print(c)
-----------------
# Zadachka pro lagerj

n = int(input("Skoljko detej edut v lagerj: "))
m = int(input("Skoljko vozhatih edut v lagerj: "))
print(math.ceil((n+m)/20))

