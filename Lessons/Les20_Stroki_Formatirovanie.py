# 1. Na vvod programme podaetsja slovo, sdelatj toljko pervuju bukvu zaglavnoj

# name = input("Enter your name: ")
# print(name.capitalize()) # metod capitalize delaet pervuju bukvu zaglavnoj

# 2. Na vhod programme podaetsja stroka. Neobhodimo prochitatj etu stroku i opredelitj chislo vhozhdenij defisov (-) v
# nejo. Na ekrane otobrazitj poluchennnoe chislo.

# user_input = input(f"Vvedite stroku: ")
# spec_symbol = user_input.find("-")
# print(user_input[spec_symbol])

# 3. Na vhod programme podaetsja stroka. Prochitajte etu stroku i s pomoshju metoda naidite v nej indeks pervogo
# vhozhdenija fragmenta "ra". Poluchenoe chislo (indeks) vivedite na ekran

# user_input = input("Vvedite stroku: ")
# i = "ra"
# print(user_input.index(i))

# 4. Na vhod programme podaetsja stroka. Prochitajte ejo i zamenite v nej dvojnie defisi (--), trojnie (---)
# na odinarnie (-), podumajte v kakoj posledovateljnosti nuzno vipolnjatj zamenu.
#
# s = input("Enter a string: ")
# s1 = s.replace("---", "-").replace("--", "-") # snachala trojnie, potom dvojnie defisi
# print(s1)

# 5. Na vhod programme podajutsja tri celih polozhiteljnih chisla (maksimum trehznachnie), zapisannie v odnu strochku
# cherez probel. Neobhodimo ih prochitatj iz vhodnogo potoka. Zatem, dlja dvuhznachnih i odnoznachnih chisel dobavitj
# sleva neznachashie nuli tak, chtobi vse chisla soderzhali po tri cifri. Vivesti na ekran poluchennie chisla v stolbik
# (kazhdoe s novoj strochki), v porjadke ih chtenija iz vhodnogo potoka.

# user_input = input("Enter three numbers without periods, maximum with three elements, separated by a space: ")
# a,b,c = map(str, input().split())
# print(a.rjust(3,"0"), b.rjust(3,"0"), c.rjust(3,"0"), sep="\n")

# a = "H+ello +w o r l d".split("+")
# print(a)

# 6. Na vhod programme podaetsja stroka, sostojashaja iz nazvanij gorodov, razdeljonnih probelom. Neobhodimo prochitatj
# etu stroku i preobrazovatj tak, chtobi nazvanija gorodov shli cherez tochku s zapjatoj (bez probelov).
# Rezuljtat (stroku otobrazite na ekrane

# user_input = input("Enter a number: ")
# x = user_input.split()
# print("; ".join(x)) # ; - eto razdelitelj

# text1 = "i'am a programmer"
# text2 = 'i\'am \t a prog\arammer' # \t - 4 probela. \n - perenos stroki na sledujushuju strochku \a - zvukovoj signal
# path = "D:\\Python\\Projects\\lessons\\text1.py"
# text3 = "She said: \"Hello!\""
# print(text3)

# name = "Maksym"
# age = 18
# print("Menja zovut {0}, mne {1} let. Ja ljublju programirovatj ".format(name, age))
# print(f"Menja zovut {name}, mne {age} let. Ja ljublju programirovatj ")
# print("Menja zovut " + name + ", mne " + str(age) +" let. Ja ljublju programirovatj ")

price = 9.99
q = 5
total = price * q
text = "Total: ${:.2f}".format(total)
print(text)
# {:.2f} - specifikator formatirovanija. : - nachalo, .2f - format chisla s dvumja znakami posle zapjatoj.f -eto float.
















