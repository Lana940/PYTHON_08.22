# colors = ['red', '56456', 'green']
# data = open('file.txt', 'a') # ukazali rezhim 'a' raboty
# data.writelines(colors) #razdeliteley ne budet
# data.close()


# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 3\n')
# print(56)

path = 'file.txt'
data = open('file.txt', 'r')
for line in data:
    print(line)
data.close()
