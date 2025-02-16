Semenov Artjom
Summary session
A = "1"; B = 2; C = 1;
print(C + B)
print("1" + 2)
print(A + B)

name = input("Enter your name: ")
print("Your name is " + name)

name = input("Enter your name: ")
city = input("Enter your city: ")
print(f"Hallo {name}, welcome to {city}")  # f - dlja napisanija strok

name = input("Enter your name: ")
num1 = int(input(f"Hallo {name} ! Enter first number: "))  # snachala rabotaet funkcija input,
num2 = int(input(f"Hallo {name} ! Enter second number: "))  #  zatem funckcija int perevodit v celoe chislo
print(f"The + of {num1} and {num2} is {num1 + num2}")
print(f"The - of {num1} and {num2} is {num1 - num2}")
print(f"The * {num1} and {num2} is {num1 * num2}")
print(f"The / of {num1} and {num2} is {num1 / num2}")
print(f"The ** of {num1} and {num2} is {num1 ** num2}")

binary_number = input("Enter a binary number: ")
decimal_number = int(binary_number, 2)  # objazateljno stavim 2, chobi citalosj binarnoe chislo
print(f"Your bin is {binary_number}, Your decimal is {decimal_number}")

oct_number = input("Enter a octal number: ")
decimal_number = int(oct_number, 8)  # objazateljno stavim 8, chobi citalosj vosmirichnoe chislo
print(f"Your oct_number is {oct_number}, Your decimal is {decimal_number}")