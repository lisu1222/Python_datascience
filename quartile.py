"""
Task
Given an array, , of  integers, calculate the respective first quartile (), second quartile (), and third quartile (). It is guaranteed that , , and  are integers.

Input Format

The first line contains an integer, , denoting the number of elements in the array.
The second line contains  space-separated integers describing the array's elements.

Constraints

, where  is the  element of the array.
Output Format

Print  lines of output in the following order:

The first line should be the value of .
The second line should be the value of .
The third line should be the value of .
Sample Input

9
3 7 8 5 12 14 21 13 18
Sample Output

6
12
16
"""


def median(nums):
	if len(nums) % 2 == 0:
		return int(sum(nums[len(nums)//2 - 1 : len(nums)//2 + 1])/2)
	else:
		return nums[len(nums)//2]


def quartile(N, nums):
	Q2 = median(nums)
	Q1 = median(nums[:N//2])
	arg = list(filter(lambda x: x > Q2, nums))
	Q3 = median(arg)
	return Q1, Q2, Q3

N = int(input())
nums = sorted(map(int, input().split(' ')))
Q1, Q2, Q3 = quartile(N, nums)

print (Q1)
print (Q2)
print (q3)



