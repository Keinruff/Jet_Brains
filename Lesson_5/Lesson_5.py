# # Chapter1
# import os
#
# print('Удаление файла в дирректории.')
# try:
#     os.remove("Chapter_1.txt")
# except:
#     print('Файл не найден.')
# print('Созадние новго файла.')
#
# f = 0
# with open(r'Chapter_1.txt', 'w', encoding='utf-8') as file:
#      print('Запущен цикл ввода данных в файл, для выхода введите  для выхода нажмите Enter в пустой строке')
#
#      while True:
#          f += 1
#          text = input(f'Введите текст {f} строки: ')
#          file.writelines(text + '\n')
#
#          if text == '':
#              break


# Chapter2
# with open(r'Chapter_2.txt', 'r', encoding='utf-8') as file:
#     text = file.readlines()
#     print(text)
#     for i, l in enumerate(text, 1):
#         sr = len(l.split())
#         print(f'Строка №{i} содержит {sr} слов.')


# Chapter3
with open(r'Chapter_3.txt', 'r', encoding='utf-8') as file:
    summ = 0
    count = 0
    for i in file:
        summ += float(i.split()[1])
        count += 1
        if float(i.split()[1]) < 20000:
            print(i.split()[0])
    avg = summ/count
    print(f'Седний доход: {round(avg,2)}')
