1. Напишите функцию merge_dicts, которая принимает произвольное количество словарей в качестве аргументов и возвращает
nовый словарь, объединяющий все входные словари. Если ключи повторяются, значения должны быть объединены в список.
Функция должна использовать аргумент **kwargs для принятия произвольного числа аргументов словаря.
Пример ввода:
{'a': 1, 'b': 2}
{'b': 3, 'c': 4}
{'c': 5, 'd': 6}
Пример вывода:
{'a': [1], 'b': [2, 3], 'c': [4, 5], 'd': [6]}

def merge_dicts(**kwargs):
    merged_dict = {}

    for dictionary in kwargs.values():
        for key, value in dictionary.items():
            if key in merged_dict:
                # Если ключ уже существует, добавляем значение в список
                if isinstance(merged_dict[key], list):
                    merged_dict[key].append(value)
                else:
                    merged_dict[key] = [merged_dict[key], value]
            else:
                # Если ключ не существует, просто добавляем его
                merged_dict[key] = value

    return merged_dict


# Пример использования
result = merge_dicts(
    dict1={'a': 1, 'b': 2},
    dict2={'b': 3, 'c': 4},
    dict3={'c': 5, 'd': 6}
)

print(result)

2. Напишите программу, которая принимает строку от пользователя и подсчитывает количество уникальных символов в этой
строке. Создайте функцию count_unique_chars, которая принимает строку и возвращает количество уникальных символов.
Выведите результат на экран.
Пример вывода:
Введите строку: hello
Количество уникальных символов: 4

def count_unique_chars(input_string):
    # Преобразуем строку в множество, чтобы получить уникальные символы
    unique_chars = set(input_string)
    # Возвращаем количество уникальных символов
    return len(unique_chars)
# Запрашиваем ввод строки у пользователя
user_input = input("Введите строку: ")
# Вызываем функцию и сохраняем результат
unique_count = count_unique_chars(user_input)
# Выводим результат на экран
print(f"Количество уникальных символов: {unique_count}")

3. Напишите программу, которая создает словарь, содержащий информацию о студентах и их оценках. Ключами словаря
являются имена студентов, а значениями - списки оценок. Создайте функцию calculate_average_grade, которая принимает
словарь с оценками студентов и вычисляет средний балл для каждого студента. Функция должна возвращать новый словарь,
в котором ключами являются имена студентов, а значениями - их средний балл. Выведите результат на экран.
Пример словаря с оценками
grades = {
    'Alice': [85, 90, 92],
    'Bob': [78, 80, 84],
    'Carol': [92, 88, 95]
}
Пример вывода:
{'Alice': 89.0, 'Bob': 80.66666666666667, 'Carol': 91.66666666666667}

def calculate_average_grade(grades):
    average_grades = {}     # Создаем новый словарь для хранения средних баллов
    for student, scores in grades.items():      # Проходим по каждому студенту и его оценкам в словаре
        average = sum(scores) / len(scores)             # Вычисляем средний балл
        average_grades[student] = average       # Сохраняем средний балл в новом словаре
    return average_grades

# Функция для ввода данных от пользователя
def input_grades():
    grades = {}
    while True:
        student_name = input("Введите имя студента (или 'стоп' для завершения): ")
        if student_name.lower() == 'стоп':
            break   # Завершаем ввод, если ввел 'стоп'

        scores_input = input(f"Введите оценки для {student_name}, разделенные запятыми: ")
        scores = list(map(int, scores_input.split(',')))        # Преобразуем введенные оценки в список чисел
        grades[student_name] = scores       # Сохраняем оценки в словаре

    return grades

grades = input_grades()

average_results = calculate_average_grade(grades)       # Вызываем функцию и сохраняем результат

print(average_results)