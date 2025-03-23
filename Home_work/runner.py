# import sys
# import os
# import subprocess
#
# # Проверяем количество аргументов командной строки
# if len(sys.argv) != 2:                                               # Ожидаем один аргумент - путь к файлу
#     print("Ошибка: Необходимо указать путь к файлу .py для запуска.")
# else:
#     file_path = sys.argv[1]                                          # Получаем путь к файлу из аргументов командной строки
#
#     if os.path.isfile(file_path) and file_path.endswith('.py'):      # Проверяем, существует ли файл и является ли он файлом .py
#         try:
#             subprocess.run(['python', file_path], check=True)   # Пытаемся запустить файл с использованием Python
#         except subprocess.CalledProcessError:
#             print("Ошибка: Не удалось запустить файл.")
#         except Exception as e:
#             print(f"Произошла ошибка: {e}")
#     else:
#         print("Ошибка: Указанный файл не существует или не является файлом .py.")