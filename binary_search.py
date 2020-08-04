def binary_search(l, item):
	low = 0
	high = len(l) - 1

	while low <= high:
		mid = (low + high) // 2
		guess = l[mid]
		if guess == item:
			return mid
		if guess < item:
			low = mid + 1
		else:
			high = mid -1

	return None


if __name__ == "__main__":
	my_list =[1,3,5,6,9]

	print (my_list)
	print (binary_search(my_list, 3))
	print (binary_search(my_list, -1))

