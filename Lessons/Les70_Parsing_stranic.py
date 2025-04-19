import requests
from bs4 import BeautifulSoup
html = requests.get("https://example.com").text
# print(html)

# Создание объекта Beautiful Soup из HTML-страницы
soup = BeautifulSoup(html, "html.parser")
print(type(soup))

print("1--------------------------------")
# Извлечение данных из тегов
title = soup.title
links = soup.find_all("a")
print(title)
print(title.text)
print(links)

print("2--------------------------------")
# Навигация по структуре документа
parent = soup.find("div").parent
next_sibling = soup.find("div").next_sibling

div = soup.find("div")
print(div)
print("3--------------------------------")
print(div.parent)

# Манипуляции с содержимым
new_tag = soup.new_tag("a", href="https://example.com")
soup.body.append(new_tag)
