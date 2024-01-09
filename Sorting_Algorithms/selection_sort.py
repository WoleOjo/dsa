'''
While len(list) - 1
	set left index to first number
	set right index to left index + 1
	while left index <= len(list) - 1
		if list[left_index] > list[right_index]
			swap numbers
		left_index plus 1
		right_index = left index plus 1
	len(list) - 1

'''


def selection_s(list):
	length = len(list) - 1

	while length - 1 :
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

num = [34,7,44,9,2,3,56,1,0,22,345,456,7,45,6789,4,32,789]
print(selection_s(num))
