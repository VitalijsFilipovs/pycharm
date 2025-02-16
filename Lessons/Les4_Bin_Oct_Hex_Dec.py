name = input("Введите ваше имя: ")
age = float(input("Enter your age: "))
print(f"The next year,{name}, your age {age+1} year old" )

decimal_number = int(input("Enter a decimal number: "))
binary = bin(decimal_number)
print(binary)
print(oct(decimal_number))
print(hex(decimal_number))

binary_number = input("Enter your number:")
print(f"{int(binary_number, 2)}")
oct_number = input("Enter your octal number:")
print(f"{int(oct_number, 8)}")
hex_number = input("Enter your hexadecimal number:")
print(f"{int(hex_number, 16)}")

x = 9
y = 3
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x//y)  # // — целочисленное деление
print(x%y)   # 5 % 2 ==1  # 4/2+1 # % — остаток от деления
print(x**y)
print(2**4)       # ** — возведение в степень
print(16**0.5)    # korenj iz 16
print(8**(1/3))   # Tretja stepenj, poluchitj korenj ljuboj stepeni
print(9**(1/2))   # Vtoraja stepenj

z = 1.5e-3 # eksponencialjnaja forma predstavlenija boljshih i malenjkih chisel
# a ne ravno b
a = 0.1+0.2
b = 0.3
print(a == b)
# Zadachka skoljko jablok kazhdomu
n = int(input("Enter a number of students: "))
k = int(input("Enter a number of apples: "))
Apple_per_student = k//n
Remm_apples = k%n
print(f"Apple_per_student = {Apple_per_student}, Remm_apples = {Remm_apples}")