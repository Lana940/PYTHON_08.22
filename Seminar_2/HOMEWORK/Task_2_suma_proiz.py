#Polzovatel vvodit 2 chisla postrochno, pervoe summa dvuh chisel, vtoroe proizvedenie. Nuzhno vvyvesti izhodnie chisla:
# 4 4 -> 2 2
# 5 6 -. 2 3

num_1 = int(input("Vvedite 1 chislo:"))
num_2 = int(input("Vvedite 2 chislo:"))

x = 0
y = 0
for x in range(1000):
    for y in range(1000):
        if (x+y == num_1) and (x*y == num_2):
           print(x, y)
    
     





