#----------3-rd task----------

def sort(array):
	for i in range(len(array)):
		j = i - 1
		element = array[i]
		while array[j] > element and j >= 0:
			array[j + 1] = array[j]
			j -= 1
		array[j + 1] = element
	return array


array = [5, 2, 3, 1, 6, 9, 3, 8, 10]
print(sort(array))
