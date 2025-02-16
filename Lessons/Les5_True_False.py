import math
a = 3.5
b = 11
print(pow(27,1/3))         # 27 v kubicheskom korne     pow=**
print(pow(2,3))            # 2 v stepeni 3
print(abs(-123))           # vivesti absoljutnoe znachenie
print(round(2.757, 2))     # 2 eto okruglenie do 100, 3 do tisjachi
print(max(23, 55 , 1100))  # vivodit maksimaljnoe chislo
print(min(1, 5, 55))       # vivodit minimaljnoe chislo
print(sum((55, 55, 55)))   # vivodit summu chisel

x = 10 # 1010 в двоичной системе
y = 5 # 0101 в двоичной системе
print(x & y) # Выводит 0   # Pobitovoe I
print(x | y) # Выводит 15  # pobitovoe ili
print(x ^ y) # Выводит 15  # XOR
print(x << 1) # Выводит 20 # sdvig v levo uvelichivaetsja
print(x >> 1) # Выводит 5  # sdvig v pravo umenjshaetsja

x = 5
print(x << 2) # rezultat 20 (5 * 2^2)

x = 20
print(x >> 2) # rezultat 5 (20 // 2^2)

x = 12 # (1100)
y = 10 # (1010)
print(x & y) # rezuljtat 8 (1000)
print(x ^ y) # rezuljtat 6 (0110)

---- NEW. Logoical data and comparisons
print(4 > 2)
print(4 < 2)
a = 5
b = 7.8
print(a > b)
print(a <= b)
res = a < b
print(res)
print(type(res)) # Bool eto True, False
res = False
print(res)
print(type(res))

print(5 == 7-2)
print(8 > 8)
print(6 == 6)
print(2 != 2)
print(8 % 2 == 7)
print(9 % 3 == 0)
print(10 % 3 == 0)

y = 1.85
print(y >= -2 and y <= 5)

x = 2
print(x >= 2 and x < 5)

---V OR istinna, esli istina hotjabi odno uslovie
---a v AND obsheje uslovie istina, jesli istina oba poduslovija

y = 2.85
print(y < -2 or y > 5)
print( -2 <= y <= 5)

x = 9
print(x % 2 == 0 or x % 3 == 0)
print(not(x % 2 == 0 and x % 3 == 0)) # Operator NOT invertiruet uslovie s True na False, i obratno

print(bool(0))   #bool vstroenaja funkcija vidaet True ili False
print(bool(" "))
print(bool([1, 2, 3]))