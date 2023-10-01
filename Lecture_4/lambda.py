# # def calk(a,b):
# #     return a+b
# def calk2(a,b):
#     return a*b

def math(op, x,y):      #op — операция, воспринимаем её как отдельную функцию. В примере это либо сумма (sum), либо перемножение(mylt):
    print(op(x,y))

# calk1 = lambda a,b : a+b

# math(calk1,5,45)

math(lambda a,b: a*b, 5, 45)

