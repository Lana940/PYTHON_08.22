# Trebuetsya vvyvesti vse celye stepeni dvoyki( t.e chisla vida 2k), ne prevoshodyashie chisla N:

n = int(input("Vvedite chislo: "))
k = 0
while 2**k <= n:
    print(2**k, end= ", ")
    k+=1  
print()
