from os import write

import requests
import json

# response = requests.get("https://facebook.com")
# # print(response.status_code) # Выводит код состояния ответа
# print(response.text) # Выводит данные, полученные от сервера
# print("---------------------")
# print(response.content)
# print("---------------------")
# print(response.status_code)
# print("---------------------")
# print(response.headers)
# print("---------------------")
# print(response.json())
# print("----------------------")
# print(response.json()["origin"])
# print("----------------------")

# response = requests.get("https://api.github.com/users/github")
# data = response.json()
# for k, v in data.items():
#     print(f"{k}: {v}")
# print("----------------------")

# response = requests.get("https://example.com")
# print(response.cookies) # Выводит cookie, полученные от сервера
# cookies = {"session_id": "123456789"}
# response = requests.get("https://example.com", cookies=cookies)
# # print("----------------------")

# response = requests.get('https://random-data-api.com/api/v2/users?size=10')
# res=response.json()
# for person in res:
#     print(person)
#     print(f"{person['last_name']:15} {person['first_name']:15} {person['email']}")
# print("----------------------")

# Skachivaem kartinku kota

import requests
from charset_normalizer.md__mypyc import exports

res = requests.get('https://api.thecatapi.com/v1/images/search')
# print(res.json())
# print(res.text)

data_json = res.json()
data_img = data_json[0]["url"]
print(data_img)
get_img = requests.get(data_img)
# print(get_img.content)
with open("cat.jpg", "wb") as f:
    f.write(get_img.content) 




