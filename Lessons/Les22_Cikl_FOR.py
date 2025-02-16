# 1. Dana stroka, sostojashaja iz slov, razdelennih probelami. opredelite skoljko v nej slov.
# phr = input("Enter a phrase : ").split()
# print(f"Number of words: {len(phr)}")

# phr = input("Enter a phrase : ")
# print(f"Number of words: {phr.count(" ")+1}")

# 2.Napishite programmu, kotoraja scitaet vhozdenija zadannoj podstroki v zadannuju stroku.
# Naprimer, dlja podstroki "ab" i stroki "Abrakadabra" programma napechataet 2.
# count = 0
# user_inp = input("Enter a string: ").lower()
# text = input("Enter path: ").lower()
# # Используем метод count для подсчета вхождений user_inp в text
# count = text.count(user_inp)
# print(f"The string '{user_inp}' occurs {count} times in the text.")

# 3. Dana stroka, sostojashaja rovno iz dvuh slov, razdeljonnih probelami. Perestavte eti slova mestami.
# Rezuljtat zapishite v stroku i vivedite poluchivshijusja strok. Pri reshenii etoj zadachi ne stoit poljzovatsja
# cikljami i instrukciej if
# text = input("Введите текст: ")
# text = text.split(" ")
# print(text[1] + " " + text[0])

# for variable in iterable object:
        #operator1
        #operator2
        #....
        #operator_n

# list1 = [1, 2, 3, 4, 5]
# for item in list1:     # vivodit v stolbik
#     print(item)

# text = "pyton"
# for char in text:    # vivodit v stolbik
#     print(char)

# text = "pyton"
# i = 0
# while i < len(text):  # vivodit v stolbik
#     print(text[i])
#     i = i + 1

# for char in "Python":
#     print(char.upper())

# list1 = [1, 2, 3, 4, 5]
# for item in list1:     # vivodit v stolbik
#     a = item **2       # vozvodit korenj
#     print(a)

list1 = [1, 2, 3, 4, 5]
for i in [0, 1, 2, 3, 4]:   # list1 perevodit v nuli
    print(i)
    list1[i]=0
    print(list1)

# for i in range(3, 501, 2): # range (start, stop, step) - nachalo, konec, shag
#     print(i)

# text = "Hello world"
# for char in text:
#     print(char, end=" ")  # pechataet cherez probel

# text = "Hello world"    # peremennaja text
# for char in range(len(text)):  # peremennaja char. char i text sotrudnichajut
#     print(text[char].upper().split(), end=" ")
#     print(char**2)

# text = "Hello world"
# for i, d in enumerate(text):  # vivodit indeks i znachenie
#     print(i, d)



