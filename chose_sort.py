#----------1-st task----------

def sort(array):
    for i in range(len(array) - 1):
        minimum = i
        index = i + 1
        while index < len(array):
            if array[index] < array[minimum]:
                minimum = index
            index += 1
        array[i], array[minimum] = array[minimum], array[i]
    return array
array = [2, 5, 4, 10, 2, 11, 234, 44, 12, 323, 5, -10, -2, -1]
print(sort(array))
