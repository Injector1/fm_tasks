#----------4-th task----------

def sort(array):
    flag = False
    i = 0
    if len(array) < 2:
        return array
    while flag == False:
        if i == 0:
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                i += 1
        elif i + 1 <= len(array) - 1:
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                i -= 1
            elif array[i] < array[i + 1]:
                i += 1
        else:
            flag = True
    return array
array = [3, 2, 1, 0, -1, 10, 20, -100, 0.5]
print(sort(array))
