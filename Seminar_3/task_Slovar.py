# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

dictionary =  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001","VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]

print("Original list:", dictionary)

result_set = set()
for cur_dict in dictionary:
    for key in cur_dict:
        result_set.add(cur_dict[key])
print(result_set)
print(*result_set)

print(*result_set, sep = '\n', )#s novoy stroki 


#reshenie cherez values i funct update 

lst = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001", "VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]

print("Original list:", lst)
result_set = set()

for cur_dict in lst:
    result_set.update(cur_dict.values())
print(*result_set, sep = '\n')
