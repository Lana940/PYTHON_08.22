def sum_str(*args):   # * oznachaet neogranichennoe chislo argumentov
    res = ''
    for i in args:
        res+=i
    return res
print(sum_str('q','e','r','l'))
print(sum_str(1,8,9))

