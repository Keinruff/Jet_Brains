print(f'А теперь давай поиграем, тема СПОРТ , Планируем наши рекорды !!!')
first_rez = int(input('Введите ваш текущий результат  (дистанция в километрах): '))
last_rez = int(input('Какую цель вы ставите пееред собой? (дистанция в километрах): '))
if first_rez >= last_rez:
    print(f'Вы меня не обманите вы достигли  своей цели')
day_rez = 1
while first_rez <= last_rez:
    first_rez = first_rez + first_rez * 0.1
    day_rez += 1
print(f'На {day_rez}  день вы достигните своего результата, в этот день вы пробежите {first_rez} киломтеров')