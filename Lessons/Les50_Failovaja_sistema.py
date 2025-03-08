# АРГУМЕНТЫ КОМАНДНОЙ СТРОКИ И
# ПЕРЕМЕННЫЕ ОКРУЖЕНИЯ
# Аргументы командной строки - это строки, разделенные пробелами, и могут
# быть доступны программе через специальный объект sys.argv из модуля sys.
# При запуске .py-файла можно передать аргументы командной строки, которые могут
# быть использованы программой для выполнения определенных действий или
# настроек.
# Кроме того, во время выполнения программы можно получить доступ к переменным
# окружения, которые предоставляют информацию о системе или пользователе.

# МОДУЛЬ SYS
# Модуль sys предоставляет доступ к некоторым переменным и функциям, связанным
# с интерпретатором Python и работой программы. Одним из наиболее полезных
# атрибутов модуля является sys.argv, который представляет список аргументов
# командной строки, переданных программе при запуске. С помощью sys.argv можно
# обработать аргументы командной строки и использовать их в программе.

import sys

args = sys.argv
print(args)

# ЗАДАНИЕ ДЛЯ ЗАКРЕПЛЕНИЯ
# Создадайте файл test.py со следующим содержимым:
# import sys
# print('Список параметров, переданных скрипту')
# print(sys.argv)
# print([arg for arg in sys.argv if arg[0]!='-'])
# Запустите файл test.py следующим образом:
# $ python3 test.py -file test.txt -pi 3.14








