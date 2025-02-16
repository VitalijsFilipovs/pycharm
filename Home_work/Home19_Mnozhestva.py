# 1. Напишите программу, которая принимает список слов и возвращает список, содержащий только анаграммы.
# Анаграммы - это слова, составленные из одних и тех же букв, но в разном порядке.
# Создайте функцию anagrams, которая принимает список слов в качестве аргумента и возвращает список анаграмм. Используйте
# множества и сортировку букв в слове для проверки на анаграмму. Выведите результат на экран.
# Пример переданного списка слов:
# ['cat', 'dog', 'tac', 'god', 'act']
# Пример вывода:
# Анаграммы: ['dog', 'god'], ['cat', 'tac', 'act']

def anagrams(words):
    anagram_dict = {}
    for word in words:  # Проходим по каждому слову в списке
        letter_set = frozenset(word)  # Используем frozenset для создания ключа

        if letter_set in anagram_dict:  # Проверяем, существует ли уже этот ключ
            anagram_dict[letter_set].append(word)  # Добавляем слово в соответствующую группу анаграмм
        else:
            anagram_dict[letter_set] = [word]

    # Извлекаем только группы анаграмм, которые содержат более одного слова
    result = [group for group in anagram_dict.values() if len(group) > 1]
    return result

user_input = input("Введите список слов, разделенных запятыми: ")
words_list = [word.strip() for word in user_input.split(",")]  # Преобразуем ввод в список, удаляя лишние пробелы

anagram_groups = anagrams(words_list)  # Получаем группы анаграмм

print(f"Анаграммы: {anagram_groups}")

# 2. Напишите функцию is_subset, которая принимает два множества set1 и set2 и проверяет, является ли set1 подмножеством
# set2. Функция должна возвращать True, если все элементы из set1 содержатся в set2, и False в противном случае. Функция
# должна быть реализована без использования встроенных методов issubset или <=.
# Пример множеств
# {1, 2, 3}
# {1, 2, 3, 4, 5}
# Пример вывода:
# True

def is_subset(set1, set2):

    for element in set1:    # Проходим по каждому элементу из set1

        if element not in set2:     # Если элемент не содержится в set2, возвращаем False
            return False

    return True     # Если все элементы из set1 найдены в set2, возвращаем True

input_set1 = input("Введите элементы первого множества, разделенные запятыми: ")
input_set2 = input("Введите элементы второго множества, разделенные запятыми: ")

# Преобразуем ввод в множества
set1 = set(map(int, input_set1.split(',')))
set2 = set(map(int, input_set2.split(',')))

# Проверка на подмножество
result = is_subset(set1, set2)
print(f"{set1} является подмножеством {set2}: {result}")
















