# 5. Определите сумму всех элементов последовательности, завершающейся числом
# 0. Числа, следующие за первым нулем, учитывать не нужно. Числа считываем с
# клавиатуры с помощью input()
# num_sum=0
# line = " "
# while True:
#     num = int(input("Enter a number: "))
#     line = line + str(num) + ", "
#     num_sum += num
#     if num == 0:
#         break
# print(f"Summa vseh chisel {line} ravna {num_sum}")
from decimal import Decimal

# --------------------
# number = 123
# total_sum = 0
# while number > 0:
#     digit = number % 10
#     total_sum += digit
#     number //= 10 # number = number // 10
# print(f"Summa chisel {number} ravna: {total_sum}")

# import math
# print(math.pi)  # stavim tochku chtobi vizvatj metodi, kotorie estj v module math
# print(math.ceil(3.14)) # okrugljaem v boljshuju
# print(math.floor(3.14)) # okrugljajem v menshuju

# import math as m
# print(m.sqrt(9))
# print(int(8/4))
# from math import pi, e, log, ceil
# print(ceil(3.14))
# floor = 7
# print(floor(3.14))

# import decimal # pozvoljaet rabotatj s fiksirovannoj tochnostju
# from decimal import Decimal, getcontext
# price = Decimal(input("Enter price: "))
# quantity = Decimal(input("Enter quantity: ")) # pri decimal vvodim stokoj s kavichkami
# total = price * quantity
# total = total.quantize(Decimal("0.01")) # fiksirovannaja tochnostj dlja valjuti
# print(f"The total price is {total}")
#
# getcontext().prec = 100 # skoljko cifr posle zapjatoj
# num1 = Decimal("1")
# num2 = Decimal("7")
# div = num1 / num2
# print(div)

# from decimal import Decimal
#
# # sozdanie decimal iz stroki
# num_str = "3.14556669224456"
# decimal_num = Decimal(num_str)
# pri











