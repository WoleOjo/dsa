
#SELECTION SORT 1 - BUBBLE SORT

def selection_1(list):
	length = len(list) - 1

	while length > 0 :
		left_index = 0
		right_index = left_index + 1
		while left_index <= (length - 1):
			if list[left_index] > list[right_index]:
				temp = list[left_index]
				list[left_index] = list[right_index]
				list[right_index] = temp
			left_index += 1
			right_index = left_index + 1
		length -= 1
	return list

#SELECTION SORT 2
def selection_2 (list):
	ln = len(list) - 1
	ln2 = len(list) - 1
	list_begin = 0

	while ln > 0 :
		right_index = ln2
		left_index = right_index - 1
		while left_index >= list_begin:
			if list[right_index] < list[left_index]:
				temp = list[right_index]
				list[right_index] = list[left_index]
				list[left_index] = temp
			right_index -=1
			left_index = right_index - 1
		ln -= 1
		list_begin += 1
	return list

def selection_3 (list):
	ln = len(list) - 1
	count = len(list) - 1
	start_index = 0
	while ln > 0:
		prev = start_index
		next = prev + 1
		while next <= count:
			if list[prev] > list[next]:
				temp = list[prev]
				list[prev] = list[next]
				list[next] = temp
			next += 1
		ln -= 1
		start_index += 1
	return list



	pos = 0
	temp = list[pos]


num = [34, 7, 44, 9, 2, 3, 56, 1, 0, 22, 345, 456, 7, 45, 6789, 4, 32, 789]
num2 = [300,78,3]
num3= [1,0]
print(selection_3(num3))
