number = int(input())
students = {}

#Ввод учеников
for i in range(number):
	student = input()
	students[student[:-5]] = student[-5:].split(' ')

#Высчитывание среднего балла
summ = 0
counter = 0
j = 0
student_index = 1
marks = []

for i in students.values():
	while j != len(i):
		summ += int(i[j])
		counter += 1
		j += 1
	marks.append(summ / counter)
	counter = 0
	summ = 0
	j = 0

#Ввод среднего балла в словарь
key = 0
while key != len(marks):
	for name in students.keys():
		students[name] = marks[key]
		key += 1

#Сортировка массива со средними баллами
for i in range(len(marks) - 1):
	minimum = i
	index = i + 1
	while index < len(marks):
		if marks[index] < marks[minimum]:
			minimum = index
		index += 1
	marks[i], marks[minimum] = marks[minimum], marks[i]

#Отсортированный словарь
final_students = {}
marks.reverse()
person = 0
while person != len(marks):
	for name in students.keys():
		if students[name] == marks[person]:
			final_students[name] = marks[person]
	person += 1

#Вывод людей
for item in final_students.keys():
	print(item)
