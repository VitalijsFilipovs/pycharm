# МЕТОДЫ functools.partial
# Модуль functools в Python предоставляет функцию partial, которая позволяет
# создавать новые функции на основе существующих путем фиксирования некоторых
# аргументов. Это полезно, когда требуется создать функцию с некоторыми
# аргументами, которые будут использоваться всегда, а другие аргументы можно
# будет передавать динамически.

# from functools import partial
# # Создание новой функции, которая всегда будет использовать аргумент x = 2
# multiply_by_two = partial(lambda x, y: x * y, 2)
# result = multiply_by_two(5)
# print(result) # Выводит 10

# РЕКУРСИЯ
# Рекурсия - это процесс, когда функция вызывает саму себя. При
# использовании рекурсии важно определить условие выхода, чтобы избежать
# бесконечной рекурсии
#
# def countdown(n):
#     if n <= 0:
#         print("Готово")
#     else:
#         print(n)
#         countdown(n - 1)
#
# # Запускаем обратный отсчет с 5
# countdown(5)

# Если рекурсия не имеет достаточного условия выхода или вызывается слишком
# глубоко, может произойти переполнение стека. Это означает, что стек вызовов
# функций полностью заполняется, и программа завершается с ошибкой.
#
# Хвостовая рекурсия - это специальный вид рекурсии, при котором
# рекурсивный вызов является последней операцией в функции.
#
# В Python интерпретатор не оптимизирует хвостовую рекурсию, поэтому
# использование цикла может быть более эффективным способом решения задачи.
#
# Рекурсия может быть полезным инструментом при решении определенных задач.
# Она позволяет разбить сложную задачу на более простые подзадачи и решить их
# пошагово. Однако рекурсия также может быть неэффективной по памяти и времени,
# особенно при обработке больших данных или глубокой рекурсии.
#
# Рекурсия может быть применена во множестве задач, таких как вычисление
# факториала, поиск в глубину в дереве, генерация перестановок и комбинаций,
# решение задачи Ханойских башен и других

# ЗАДАНИЕ ДЛЯ ЗАКРЕПЛЕНИЯ
# 1. Что выведет этот код?

# def message():
#     print('Это рекурсивная функция')
# message()
# message()

# 2. В чем разница с этим фрагментом?
# def message(times):
#     if times > 0:
#         print('Это рекурсивная функция')
#         message(times - 1)
# message(5)

# 3. Что выведет этот код, в чем отличие от первых 2?

# def message(times):
#         if times > 0:
#             print('Это рекурсивная функция.')
#             message(times - 1)
#             print(times)
# message(5)


