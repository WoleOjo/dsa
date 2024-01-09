import math
#Works for sorted list
"""
0. check for empty list
	return -1 if empty
1.set two bonds: low and high
2.set mid as the mid point between low and high
3.initial low and high is beginning and end of array idex
4.while high not equal to
	if  mid element == query
		return mid
	if mid element is greater than query, set new high to mid - 1
	if mid element is less than query, set new low to mid + 1

5. return not found
"""

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


