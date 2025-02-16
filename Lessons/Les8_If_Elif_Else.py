# Uslovnie operatori If, Elif, Else

# print(4 > 2)
# a = 5
# print(a < 0)

# x = -4
# if x < 0:
#     # telo uslovnogo operatora if (s otstupom)
#     x = -x
# print(x)

# x = 4
# if x < 0:
#     x = -x
#     print(x)
# print("The end")

# a = float(input("Enter a : "))
# b = float(input("Enter b : "))
# if a < b:
#         a, b = b, a  # Vot tak mozhno pomenjatj znachenie dvuh peremennih
# print(a, b)

# x = int(input("Enter a number: "))
# if x >= -4 and x <= 10:  #  x <= -4 and x <= 10
#     print("X v diapazone")
# # print("X vne diapazona")

# x = int(input("Enter a number: "))
# if x:
#     print("The number is true")

# if True:
#     print("True")

# list_marks = [1, 2, 4, 3] # kollekcija znachenij
# if 5 in list_marks:
#     print("Student budet otchislen")
# else:
#     print("Student ne budet otchislen")

# x = int(input("Enter a number: "))
# if x < 0:
#     print("The number is negative.")
# else:
#     print("The number is positive.")

# x = int(input("Enter a number: "))
# if x % 2 == 0:
#     print("The number is even( chotnoe ).")
# else:
#     print("The number is odd ( ne chotnoe ).")

# x = int(input("Enter a number: "))
# y = int(input("Enter another number: "))
# if x > y:
#     print(f"{x} is greater than {y}")
# elif x < y:
#     print(f"{x} is less than {y}")
# # else:
# #     print(f"{x} is equal to {y}")
# elif x == y:
#     print(f"{x} is equal to {y}")
# else:
#     print(f"Error: {x} != {y}")

# a = "1.Python"
# b = "2.C++"
# c = "3.JAVA"
# d = "4.JavaScript"
# print(a, b, c, d, sep="\n")
# ask = int(input("Choose the course (1 to 4): "))
# if ask == 1:
#     print(f"You chose {a}")
# elif ask == 2:
#     print(f"You chose {b}")
# elif ask == 3:
#     print(f"You chose {c}")
# elif ask == 4:
#     print(f"You chose {d}")
# else:
#     print(f"You didn't chose anything")

# a = 12   # Ternarnij uslovnij operator
# b = 7
# # if a > b:
# #     rest = a
# # else:
# #     rest = b
# # print(rest)
# rest = a if a > b else b
# print(rest)

# age = 10
# status = "+18" if age >= 18 else "not now 18"
# print(status)

# d = if 5 > 2: # Uslovnij operator nichego ne vozvrashaet, on proverjaet true, false, a vot ternarnij operator (tri operandi) vozvrashaet

rain = input("Is it rain now? (Y/N): ").upper()
if rain == "Y":
    wind = input("Is it wind? (Y/N): ").upper()
    if wind == "Y":
        print(f"Stay at home")
    elif wind == "N":
        print("Take an ubrella ang go walk")
    else:
        print("Sorry, I don't understand")
elif rain == "N":
    print("Have a nice day, go a walk")
else:
    print("Sorry, I don't understand")

