# 1. Напишите программу, которая принимает в качестве аргумента командной строки путь к файлу .py и запускает его.
# При запуске файла программа должна выводить сообщение "Файл <имя файла> успешно запущен". Если файл не существует
# или не может быть запущен, программа должна вывести соответствующее сообщение об ошибке.

# import sys
#
# if len(sys.argv) != 2:
#     print("Hallo world")
# else:
#     file_path = sys.argv[1]


# 2. Напишите программу, которая принимает в качестве аргумента командной строки путь к директории и выводит список
# всех файлов и поддиректорий внутри этой директории. Для этой задачи используйте модуль os и его функцию walk.
# Программа должна выводить полный путь к каждому файлу и директории.

# import os
# import sys
#
# def list_files_and_directories(directory):
#
#     if not os.path.exists(directory):                       # Проверяем, существует ли указанная директория
#         print(f"Директория '{directory}' не существует.")
#         return
#
#     for root, dirs, files in os.walk(directory):            # Используем os.walk для обхода директории
#         for dir_name in dirs:                               # Выводим полный путь к поддиректориям
#             print(os.path.join(root, dir_name))
#         for file_name in files:                             # Выводим полный путь к файлам
#             print(os.path.join(root, file_name))
#
# if __name__ == "__main__":
#     if len(sys.argv) != 2:                                  # Проверяем, передан ли аргумент командной строки
#         print("Использование: python Home26_Console.py <+ путь_к_директории>")  # python C:\Users\elekt\PycharmProjects\Project1\Home_work\Home26_Console.py C:\Users\elekt\PycharmProjects\Project1
#     else:
#         directory_path = sys.argv[1]
#         list_files_and_directories(directory_path)



