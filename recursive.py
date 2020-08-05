#calculate number of elements in an array using recursive
def lenArr(lst):
	if lst == []:
		return 0
	else:
		return 1 + lenArr(lst[1:])

print (lenArr([1,3,4,2,4]))


#calculate sum of an array
def arrSum(lst):
	if lst == []: 
		return 0
	elif len(lst) == 1:
		return lst[0]
	else:
		return lst[0] + arrSum(lst[1:])

print (arrSum([2,3,4,1,43,21,1]))

#find the largest num in a list
def maxList(lst):
	if len(lst) == 1:
		return lst[0]
	elif len(lst) == 0:
		return None
	else:
		return lst[0] if lst[0] > maxList(lst[1:]) else maxList(lst[1:])

print (maxList([43,2,34,56,31,22,23,19]))


#binary search using recursive
def find(lst, target, start = 0, end = None):
	end = len(lst) if end is None else end
	mid_index = (end - start)//2 + start
	if lst[mid_index] < target:
		find(lst, target, start = mid_index+1, end = end)
	elif lst[mid_index] > target:
		find(lst, target, start = start, end = mid_index-1)
	else:
		print('Found index: {}, value: {}'.format(mid_index, target))

print (find([2,3,5,10,16,18], 5))





