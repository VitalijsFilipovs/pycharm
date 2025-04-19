# 1. Напишите функцию get_response(url), которая отправляет GET-запрос по заданному URL-адресу и возвращает объект ответа.
# Затем выведите следующую информацию об ответе:
# - Код состояния (status code)
# - Текст ответа (response text)
# - Заголовки ответа (response headers)
#
# Пример использования:
# url = "https://api.example.com"
# response = get_response(url)
# print("Status Code:", response.status_code)
# print("Response Text:", response.text)
# print("Response Headers:", response.headers)
#
# #-------------------------------------------------------------------
#
# import requests
#
# def get_response(url):
#     url = "https://facebook.com"
#     response = requests.get(url)
#     print("---------------------")
#
#     print("Status Code:", response.status_code)
#     print("---------------------")
#
#     print("Response Text:", response.text)
#     print("---------------------")
#
#     print("Response Headers:", response.headers)
#     print("---------------------")
#
# get_response("https://facebook.com")
#
# 2. Напишите функцию find_common_words(url_list), которая принимает список URL-адресов и возвращает список наиболее
# часто встречающихся слов на веб-страницах. Для каждого URL-адреса функция должна получить содержимое страницы с
# помощью запроса GET и использовать регулярные выражения для извлечения слов. Затем функция должна подсчитать количество
# вхождений каждого слова и вернуть наиболее часто встречающиеся слова в порядке убывания частоты.
#
# #---------------------------------------------------
#
# import requests
# import re
# from collections import Counter
#
# def find_common_words(url_list, top_n=20):
#     total_counter = Counter()
#
#     for url in url_list:
#         try:
#             response = requests.get(url)
#             html_text = response.text
#
#             words = re.findall(r'\b\w+\b', html_text.lower())           # Извлекаем слова
#
#             total_counter.update(words)                                        # Обновляем общий счётчик
#
#         except Exception as e:
#             print(f"Ошибка при запросе {url}: {e}")
#
#     most_common = total_counter.most_common(top_n)                              # Выводим N самых частых слов
#     print("\nНаиболее частые слова:")
#     for word, count in most_common:
#         print(f"{word}: {count}")
#
#     return most_common
#
# user_input = input("Введите URL-адреса через запятую: ")
# url_list = [url.strip() for url in user_input.split(',') if url.strip()]
#
# find_common_words(url_list)