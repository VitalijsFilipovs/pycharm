# Окно 5: Асинхронные генераторы (Async Generators)
#
# import asyncio
#
# # 1. Напишите асинхронный генератор, который возвращает числа от 1 до n с задержкой в 1 секунду.
# async def async_numbers(n):
#     for i in range(1, n + 1):
#         await asyncio.sleep(1)  # Задержка в 1 секунду
#         yield i  # Возврат числа
#
# # Пример использования:
# # async def main():
# #     async for num in async_numbers(5):
# #         print(num)
# # asyncio.run(main())
#
# # 2. Напишите асинхронный генератор, который читает данные из API с использованием `asyncio` и возвращает каждую запись.
# async def async_fetch_data(url):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             data = await response.json()
#             for item in data:
#                 yield item  # Возврат каждой записи
#
# # Пример использования:
# # async def main():
# #     async for record in async_fetch_data('https://api.example.com/data'):
# #         print(record)
# # asyncio.run(main())
#
# # 3. Напишите асинхронный генератор, который возвращает строки из файла с задержкой.
# async def async_read_file_lines(filename):
#     async with aiofiles.open(filename, 'r') as file:
#         async for line in file:
#             await asyncio.sleep(1)  # Задержка в 1 секунду
#             yield line.strip()  # Возврат строки
#
# # Пример использования:
# # async def main():
# #     async for line in async_read_file_lines('example.txt'):
# #         print(line)
# # asyncio.run(main())
#
# # 4. Напишите асинхронный генератор, который возвращает данные из базы данных с использованием асинхронного драйвера.
# async def async_read_db_records(db_file):
#     conn = await aiosqlite.connect(db_file)
#     async with conn.execute("SELECT * FROM table_name") as cursor:
#         async for row in cursor:
#             yield row  # Возврат каждой записи
#     await conn.close()
#
# # Пример использования:
# # async def main():
# #     async for record in async_read_db_records('example.db'):
# #         print(record)
# # asyncio.run(main())
#
# # 5. Напишите асинхронный генератор, который возвращает данные из веб-сокета.
# async def async_read_websocket(url):
#     async with websockets.connect(url) as websocket:
#         while True:
#             message = await websocket.recv()
#             yield message  # Возврат сообщения
#
# # Пример использования:
# # async def main():
# #     async for message in async_read_websocket('ws://localhost:8765'):
# #         print(message)
# # asyncio.run(main())
#
# # 6. Напишите асинхронный генератор, который возвращает данные из нескольких источников одновременно.
# async def async_multiple_sources(urls):
#     for url in urls:
#         async for data in async_fetch_data(url):
#             yield data  # Возврат данных из каждого источника
#
# # Пример использования:
# # async def main():
# #     urls = ['https://api.example.com/data1', 'https://api.example.com/data2']
# #     async for record in async_multiple_sources(urls):
# #         print(record)
# # asyncio.run(main())
#
# # 7. Напишите асинхронный генератор, который возвращает данные из очереди.
# async def async_read_queue(queue):
#     while True:
#         item = await queue.get()
#         if item is None:
#             break
#         yield item  # Возврат элемента из очереди
#
# # Пример использования:
# # async def main():
# #     queue = asyncio.Queue()
# #     await queue.put('data1')
# #     await queue.put('data2')
# #     await queue.put(None)  # Завершение
# #     async for item in async_read_queue(queue):
# #         print(item)
# # asyncio.run(main())
#
# # 8. Напишите асинхронный генератор, который возвращает данные из нескольких файлов одновременно.
# async def async_read_multiple_files(filenames):
#     for filename in filenames:
#         async for line in async_read_file_lines(filename):
#             yield line  # Возврат строки из каждого файла
#
# # Пример использования:
# # async def main():
# #     filenames = ['file1.txt', 'file2.txt']
# #     async for line in async_read_multiple_files(filenames):
# #         print(line)
# # asyncio.run(main())
#
# # 9. Напишите асинхронный генератор, который возвращает данные из API с использованием пагинации.
# # async def async_paginated_fetch(url):
# #     page = 1
# #     while True:
# #         response = await fetch_data(f"{url}?page={page}")
# #         if not response:
# #             break
# #         for item in response:
# #             yield item  # Возврат каждой записи
# #         page += 1
#
# # Пример использования:
# # async def main():
# #     async for record in async_paginated_fetch('https://api.example.com/data'):
# #         print(record)
# # asyncio