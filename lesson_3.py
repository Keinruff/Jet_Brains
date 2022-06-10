
# section 1
# В звдвниях не требуется делать проверки исключения и прочее,   для  экономии врмени  с проверками, проверки не делал.
# предпологается там где требует вводить цифры будут вводится цифры.

def func_1(chisl, znam):
    if int(znam) == 0:
        print('Деление на 0, запрещено')
        return
    print(f'Резальтат от деления  равен: {int(chisl ) /int(znam)}')
    return
# по стандарту 2 пустых строки после обьявления функций


func_1(input('Ведите числитель: '), input('Ведите Знаменатель: '))
print('*' * 30)

# section 2


def func_2(name=str(None), surname=str(None), berth=str(None), city=str(None), mail=str(None), tel=str(None)):
    rez = name + ' ' + surname + ', ' + berth + '. City ' + city + ', e-Mail: ' + mail + ' Tel: ' + tel
    return rez


print(func_2(input('Ведите имя: '), surname=input('Ведите Фамилию: ')))
print ('*' * 30)
#
i = input('Ведите Имя: ')
f = input('Ведите Фамилию: ')
b = input('Ведите День рождения: ')
e = input('Ведите E-Mail: ')
t = input('Ведите Телефон: ')
c = input('Ведите Город: ')
print(func_2(name=i, surname=f, berth=b, city=c, tel=t, mail=e))
print('*' * 30)


# section 3


def my_func(a, b, c):
    if int(a) >= int(b) and int(a) >= int(c):
        if int(b) >= int(c):
            a_b = int(a) + int(b)
            return a_b
        a_c = int(a) + int(c)
        return a_c
    b_c = int(b) + int(c)
    return b_c


print('Введите 3 числа: ')
print(my_func(input('A= '), input('B= '), input('C= ')))
print('*' * 30)


# section 4

def func_4(n, x, y):
    n = int(n)
    x = int(x)
    y = int (y)
    if int(n) == 1:
        c = int(x) ** int(y)
        return c
    if int(n) == 2:
        if y < 0:
           x = 1 / x
        r = x
        y = abs(y)
        while y != 1:
            y -= 1
            x *= x
        return x

n = input('Введите числовой вариант решения: 1 - простое рещение, 2- сложное решение: ')
x = input(' Действительное положительне X= ')
y = input('Целое трицательноеY= ')
print(func_4(n,x,y))


# section 5


def func_5():
    sum = 0
    a = 0
    while a != 1:
        st1 = input('Введите строку разделенну пробелом, для выхода укажите "*": ')
        st1 = st1.split()
        print(st1)
        for el in st1:
            print(el)
            if str(el) == '*':
                print(f'Сумма всех чисел в строке: {sum}')
                return 'Функция завершена'
            sum += int(el)
        print(f'Сумма всех чисел в строке: {sum}')

print(func_5())


# section 6 - 7
#  смыл задачи не понял, мы же изучили функцию делающую это. И на явно тут нарпрашивается, завернул ее в свою функцию
#  весь смысл использваония высокоуровневых языков программирования в использвоании наработанного до тебя опыта.
#  если терубется самостоятлеьо написать аналог функции .title() , укажите это вкомментарии сделаю в составе следующей задачи.
def int_func(a):
    a = a.title()
    return a

print(int_func(input('Ведите строку: ')))