# Chapter1
import os

print('Удаление файла в дирректории.')
try:
    os.remove("Chapter_1.txt")
except:
    print('Файл не найден.')
print('Созадние новго файла.')

f = 0
with open(r'Chapter_1.txt', 'w', encoding='utf-8') as file:
     print('Запущен цикл ввода данных в файл, для выхода введите  для выхода нажмите Enter в пустой строке')

     while True:
         f += 1
         text = input(f'Введите текст {f} строки: ')
         file.writelines(text + '\n')

         if text == '':
             break
