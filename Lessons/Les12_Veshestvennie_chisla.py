# 1, U nas estj celoe chislo x. Napisatj programmu raznicu 21 - x

# x = int(input("Enter a integer number: "))
# if x <= 21:
#     print(21 - x)
# else:
#     print(2 * (21 - x))

# Vtoroj variant programmi

# x = int(input("Enter a integer number: "))
# result = print(21 - x) if x <= 21 else print(2 * (21 - x)) # Ternarbij uslovnij operator

# --------------------------

# 2, U nas estj celoe chislo X. Napishite programmu, kotoraja pechataet raznicu 100 i X, esli X boljshe 10 i menjshe 100, i pechataet X v protivnom sluchae

# x = int(input("Enter a number: "))
# if 10 < x < 100:
#     print(100 - x)
# else:
#     print(x)

# Vtoroj variant programmi

# x = int(input("Enter a number: "))
# result = print(100 - x) if x < 100 and x > 10 else print(x)

# Ili esho variant

# x = int(input("Enter a number: "))
# result1 = (100 - x) if x < 100 and x > 10 else (x)
# print(result1)

# -----------------------------

# 3, Programma s zaprosom celogo chisla, proverjaet prostoe chislo ili sostavnoe

# x = int(input("Enter a number: "))
# i = 2
# while i < x:
#     if x % i == 0:
#         print(f"Vashe chislo sostavnoe")
#         break
#     else:
#         i += 1
# else:
#     print(f"Vashe chislo prostoe")

# --- Vtoroj variant

# x = int(input("Enter a number: "))
# if x <= 1:
#     print("Chislo dolzhno bitj boljshe 1")
# else:
#     is_true = True
#     i = 2
#     while i < x:
#         if x % i == 0:
#             is_true = False
#             break
#         i += 1
#     if is_true:
#         print(f"Chislo prostoe")
#     else:
#         print(f"Chislo sostavnoe")

# --- Tretij variant

x = int(input("Enter a number: "))
count = 0
while count < x:
    if count == 5:
        continue
    else:
        print(count)
        count += 1
