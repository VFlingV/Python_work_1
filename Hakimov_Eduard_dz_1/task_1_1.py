

def convert_time(duration: int) -> str:
    # пишите реализацию своей программы здесь
    s = duration
    m = 60
    h = 3600
    d = 86400
    if s < m:
        result = '{} сек'.format(s)
    elif m <= s and h > s:
        nm = s //m
        ns = s % m
        result = '{} мин {} сек'.format(nm , ns)
    elif s >= h and s < d:
        nh = s // h
        s = s % h
        nm = s // m
        ns = s % m
        result = '{} час {} мин {} сек'.format(nh, nm, ns);
    elif s >= d and s < one_week:
        my_day = duration // one_day
        duration = duration % one_day
        my_hour = duration // one_hour
        duration = duration % one_hour
        my_minute = duration // one_minute
        my_second = duration % one_minute
        print('{} дн {} час {} мин {} сек'.format(my_day, my_hour, my_minute, my_second));


    return result


duration = 80
result = convert_time(duration)
print(result)




