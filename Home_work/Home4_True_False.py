# Запрашиваем у пользователя первое логическое значение
first_value = input("Введите первое логическое значение (True или False): ")
# Запрашиваем у пользователя второе логическое значение
second_value = input("Введите второе логическое значение (True или False): ")

# Преобразуем введенные строки в логические значения
first_bool = first_value.lower() == 'true'
second_bool = second_value.lower() == 'true'

# Выполняем логические операции
and_result = first_bool and second_bool
or_result = first_bool or second_bool
not_first_result = not first_bool
not_second_result = not second_bool
equality_result = first_bool == second_bool
inequality_result = first_bool != second_bool

# Выводим результаты
print(f"Результат логического И: {and_result}")
print(f"Результат логического ИЛИ: {or_result}")
print(f"Результат логического НЕ (для первого значения): {not_first_result}")
print(f"Результат логического НЕ (для второго значения): {not_second_result}")
print(f"Результат сравнения на равенство: {equality_result}")
print(f"Результат сравнения на неравенство: {inequality_result}")