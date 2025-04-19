# 1. Напишите программу, которая запрашивает у пользователя URL-адрес веб-страницы, использует библиотеку Beautiful Soup
# для парсинга HTML и выводит список всех ссылок на странице.
#
# import requests
# from bs4 import BeautifulSoup
#
# user_input = input("Введите URL-адрес: ")               # Запрашиваем ссылку у пользователя
#
# response = requests.get(user_input)                     # Загружаем HTML-код страницы
# html = response.text
#
# soup = BeautifulSoup(html, 'html.parser')       # Создаём объект BeautifulSoup
#
# links = soup.find_all('a')                              # Ищем все теги <a> и выводим href
#
# print("\nНайденные ссылки:")
# for link in links:
#     href = link.get('href')
#     if href:
#         print(href)
#
# 2. Напишите программу, которая запрашивает у пользователя URL-адрес веб-страницы и уровень заголовков, а затем использует
# библиотеку Beautiful Soup для парсинга HTML и извлекает заголовки нужного уровня (теги h1, h2, h3 и т.д.) с их текстом.
#
# import requests
# from bs4 import BeautifulSoup
#
# url = input("Введите URL-адрес: ")
#
# response = requests.get(url)                            # Загружаем HTML-страницу
# html = response.text
#
# soup = BeautifulSoup(html, 'html.parser')       # Создаём объект BeautifulSoup
#
# levels = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']           # Ищем все заголовки h1–h6
# headings = soup.find_all(levels)
#
# print("\nНайденные заголовки (h1–h6):")
# for heading in headings:
#     print(f"{heading.name.upper()}: {heading.get_text(strip=True)}")