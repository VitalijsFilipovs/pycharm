# name = "Max"
# age = 30
# text = f"My name is {name} and I am {age} years old."
# print(text)

# price = 9.99
# q = 5
# total = price * q
# text = f"Total: ${total:.2f}"
# print(text)

# name = "Max"
# age = 30
# text = f"My name is {name:>30} and I am {age:=^10} years old."
# print(text)
# print(f"{"Hello":*<10}")

# 1. Na vhod prihodjat imja-familija-pol-vozvrast. Programma vivodit privetstvennuju stroku.
# v kotoroj vstavleni imja familija, i pishet dopolniteljno chto srednij vozvrast vseh ljudej
# tvoego pola sredi vstrechennih ranee - takoj-to.
# realizovatj bez hranenija spiskov ili inih massivov v pamjati

# # Инициализация переменных
# total_age_men = 0
# total_age_women = 0
# count_men = 0
# count_women = 0
#
# while True:
#     name = input("Введите ваше имя: ")
#     last_name = input("Введите вашу фамилию: ")
#     gender = input("Введите ваш пол (M для мужчин, W для женщин): ")
#     age = int(input("Введите ваш возраст: "))
#     print(f"Привет, {name} {last_name}!")
#
#     # Обработка данных в зависимости от пола
#     if gender.upper() == "M":
#         total_age_men += age
#         count_men += 1
#         if count_men > 0:
#             average_age_men = total_age_men / count_men
#             print(f"Средний возраст мужчин: {average_age_men:.1f} лет")
#     elif gender.upper() == "W":
#         total_age_women += age
#         count_women += 1
#         if count_women > 0:
#             average_age_women = total_age_women / count_women
#             print(f"Средний возраст женщин: {average_age_women:.1f} лет")
#
#     else:
#         print("Некорректный ввод пола. Пожалуйста, введите 'M' для мужчин или 'W' для женщин.")
#
#     # Вопрос о продолжении
#     continue_response = input("Хотите продолжить? (yes/no): ").strip().lower()
#     if continue_response != "yes":
#         break  # Выход из цикла, если пользователь не хочет продолжать
# # Вывод итоговой информации
# if count_men > 0 or count_women > 0:
#     print(f"Общее количество мужчин: {count_men}, Общее количество женщин: {count_women}")
# else:
#     print("Не было введено ни одного респондента.")

# 2. Napishite programmu, kotoraja vivodit na ekran sledujushij tekst, ispuljzuja strokovie literali i ekranirovanie
# simvolov: hello
# print("Hello\tWorld!\nHow are you?")

# 3. Prihodit tekst iz 5 strok, nado
#   1, sdelatj tak chto bi vse predlozhenija s boljshoj bukvi
#   2, ne bilo podrjad neskoljko probelov, zapjatih mnogotochij, i t.p.
#   3, stroka ne dolzha nachinatsja s probelov, dopustima toljko tabulljacija otstup
#   4, ne zabivajte, chto tochka ne vsegdaa znachit konec predlozhenija. naprimet i t.p. i t.d.

# text = " ".join(""""    eto primer teksta. s neskoljkimi strokami! on nachitaetsja s probelov?
# i t.d. estj lishnie probeli, i dazhe mnogotochie... """.split())
# formated_text = text.split(". ")
# print(formated_text)
# i = 0
# while i < len(formated_text):
#     formated_text[i] = formated_text[i].capitalize()
#     i += 1
# print(formated_text)

# # 4. Vivesti tretij simvol etoj stroki
# text = input("Vvesti stroku: ")
# print(text[2]) # index 2, eto tretij simvol
# print(text[-2]) # vtoroj simvol s konca
# print(text[::-1]) # perevorachivaet strochku
# print(text[0:5]) # pervie 5 simvolov
# print(text[0:-2]) # bez 2 poslednih simvolov
# print(text[::2]) # vivodit chotnie indeksi
# print(text[1::2]) # vivodit nechotnie simvoli
# print(len(text)) # dlina stroki



