#bystrayq sortirovka razdelyay i vlastvuy

def quick_sort(array):
    if len(array)<=1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i>= pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)
print(quick_sort([14,5,9,3,677,6,89,443,32]))