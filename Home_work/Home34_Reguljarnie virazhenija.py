# Напишите функцию extract_emails(text), которая извлекает все адреса электронной почты из заданного текста и возвращает
# их в виде списка.
# Пример использования:
#
# text = "Contact us at info@example.com or support@example.com for assistance."
#
# emails = extract_emails(text)
#
# print(emails)  # Вывод: ['info@example.com', 'support@example.com']
#
# import re
#
# def extract_emails(text):
#     if not text:
#         return []
#
#     email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'   # Регулярное выражение для поиска email
#     emails = re.findall(email_pattern, text)
#
#     return emails
#
# text = "Contact us at info@example.com or support@example.com for assistance."
# emails = extract_emails(text)
#
# print(emails)  # Вывод: ['info@example.com', 'support@example.com']
#
# ##########################################################################################################
#
# Напишите функцию highlight_keywords(text, keywords), которая выделяет все вхождения заданных ключевых слов в тексте,
# окружая их символами *. Функция должна быть регистронезависимой при поиске ключевых слов.
#
# Пример использования:
#
# text = "This is a sample text. We need to highlight Python and programming."
#
# keywords = ["python", "programming"]
#
# highlighted_text = highlight_keywords(text, keywords)
#
# print(highlighted_text)
#
# # Вывод: "This is a sample text. We need to highlight *Python* and *programming*."
#
# import re
#
# def highlight_keywords(text, keywords):
#     if not text or not keywords:
#         return text
#
#     pattern = r'(' + '|'.join(re.escape(keyword) for keyword in keywords) + r')'    # Создаем регулярное выражение для ключевых слов
#
#     highlighted_text = re.sub(pattern, r'*\1*', text, flags=re.IGNORECASE)     # Заменяем ключевые слова на их версию с обрамлением *
#
#     return highlighted_text
#
#
# text = "This is a sample text. We need to highlight Python and programming."
#
# keywords = ["python", "programming"]
#
# highlighted_text = highlight_keywords(text, keywords)
#
# print(highlighted_text)