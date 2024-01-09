import math
def bin_s (list,query):
	low = 0
	high = len(list) - 1
	if len(list) == 0:
		return -1
	while low != high:
		mid = math.floor((low + high)/2)
		if list[mid] == query:
			return mid
		elif list[mid] > query:
			high = mid - 1
		else:
			low = mid + 1
	if list[low] == query:
		return low
	return 'NOT FOUND'

print(bin_s([2],2))


