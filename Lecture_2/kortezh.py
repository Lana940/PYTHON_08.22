t = ()
print(type(t))

t = (1 , )
print(type(t))

v = [1, 8, 9]
print(v)
print(type(v))

v = tuple(v)
print(v)
print(type(v))

#razedinim kortezh - raspokovka 

a, b, c = v
print(a,b,c)


t = (1,2,3,4,5)
print(t[1])
 
t = (1,2,3,4,5)
for i in t:
    print(i)

t = (1,2,3,4,5)
for i in range(len(t)):
    print(t[i])