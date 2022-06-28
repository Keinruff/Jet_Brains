# section 1


li = ['fio', 1, ['s', 'f']]
print(type(li[0]))
print(type(li[2]))

# section 2

li = input('Введите строку через пробел').split()
for i in range(1, len(li), 2):
    k = li[i-1]
    li[i-1] = li[i]
    li[i] = k
print(li)


# section 3

li = ['', 'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октабрь', 'Ноябрь', 'Декабрь']
print(li[int(input('Введите номер месяца: '))])

di = {    '1':'Январь'
        , '2':'Февраль'
        , '3':'Март'
        , '4':'Апрель'
        , '5':'Май'
        , '6':'Июнь'
        , '7':'Июль'
        , '8':'Август'
        , '9':'Сентябрь'
        , '10':'Октабрь'
        , '11':'Ноябрь'
        , '12':'Декабрь'
       }

print(di.get(input('Введите номер месяца: ')))


# section 4

li = input('Введите строку через пробел: ').split()
for i in range(len(li)):
    print(f'{i+1} Строка: {str(li[i])[:10]}')


# section 5
my_list = [7, 5, 3, 3, 2]
r = int(input('Введите новый рейтинг'))
for i in range(1, len(my_list)):
    if r > my_list[i-1] and i-1 == 0:
        my_list.insert(i-1, r)
        break
    elif (r < my_list[i-1] and r >= my_list[i]) :
        my_list.insert(i, r)
        break
    elif i == len(my_list)-1: # данный блок накостылилил, если честно не понял почему так, хотелось бы узнать как еще можно это решить
        my_list.append(r)
        break
    print(i)
print(my_list)



