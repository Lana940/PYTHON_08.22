#def function_name

def sumnumbers(n):
    summa = 0
    for i in range (1, n+1):
        summa+=i
    return summa
    print(summa)  #return zavershit cikl funkcii

print(sumnumbers(5))