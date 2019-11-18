def sort(array):
    i = 0
    tof = None
    if len(array) < 2:
        return array
    while i < len(array):
        if i + 1 != len(array) and array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
            tof = True
        i += 1
        if tof == True and i == len(array):
            tof, i = False, 0
    return array

print(sort([1, 3, 8, 9, 1]))
