def func(a: int, b: int) -> int:
    c = a + b
    return c #none
d = 7
f = 6
print(func(d, f))

def convert_time(duration: int) -> str:
    # пишите реализацию своей программы здесь
    return "верните итоговую строку с результатом"


duration = 400153
result = convert_time(duration)
print(result)

s = duration
m = 60
h = 3600
d = 86400

# 1 минута
one_minute = 60
# 1 час
one_hour = 3600
# 1 день
one_day = 86400
# 1 неделя
one_week = 604800
# 1 месяц (30.44 дней)
one_month = 2629743
# 1 год (365.24 дней)
one_year = 31556926

#Пользователь вводит продолжительность duration в секундах:
duration = int (input('Укажите продолжительность в секундах: '))

#вывод информации до минуты:
if duration<one_minute:
    print ('{} сек'.format(duration))
#вывод информации до часа:
elif one_minute <= duration and one_hour > duration:
    my_minute=duration//one_minute
    my_second=duration%one_minute
    print ('{} мин {} сек'.format(my_minute,my_second));
#вывод информации до суток:
elif duration >= one_hour and duration < one_day:
    my_hour=duration // one_hour
    duration=duration % one_hour
    my_minute = duration // one_minute
    my_second = duration % one_minute
    print ('{} час {} мин {} сек'.format(my_hour,my_minute,my_second));
    lab = '{} сек'.format(duration)
    print('{} час {} мин {} сек'.format(my_hour,my_minute,my_second))