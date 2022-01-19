
def convert_time(duration: int) -> str:
    # пишите реализацию своей программы здесь
    s = duration
    m = 60
    h = 3600
    d = 86400
    w = 604800
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
    elif s >= d and s < w:
        nd = s // d
        s = s % d
        nh = s // h
        s = s % h
        nm = s // m
        ns = s % m
        result = '{} дн {} час {} мин {} сек'.format(nd, nh, nm, ns);
    return result

duration = 400153

result = convert_time(duration) # подвис на том как вывести в принт в нормальном формате
print(result)




