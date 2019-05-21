
import os, sys

# Задача-1: (СДЕЛАНО)
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# for i in range(1,10):
#     dir_path = os.path.join(os.getcwd(), f'dir_{i}')
#     try:
#         os.mkdir(dir_path)
#     except FileExistsError:
#         print('Такая директория уже существует')
# #
# for i in range(1,10):
#     dir_del = os.path.join(os.getcwd(), f'dir_{i}')
#     try:
#         os.rmdir(dir_del)
#     except FileExistsError:
#         print('Нечего удалять')

# Задача-2: (СДЕЛАНО)
# Напишите скрипт, отображающий папки текущей директории.

# for file in os.listdir():
#     if os.path.isdir(file) is True:
#         print(file)

# Задача-3: (СДЕЛАНО)
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
# print(os.getcwd())
# import shutil
# shutil.copy("C:/Users/User/Downloads/Romashchenko_lesson5.py", "C:/Users/User/Downloads/Romashchenko_lesson5_copy.py")
