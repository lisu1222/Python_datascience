"""
Task
The interquartile range of an array is the difference between its first () and third () quartiles (i.e., ).

Given an array, , of  integers and an array, , representing the respective frequencies of 's elements, construct a data set, , where each  occurs at frequency . Then calculate and print 's interquartile range, rounded to a scale of  decimal place (i.e.,  format).

Tip: Be careful to not use integer division when averaging the middle two elements for a data set with an even number of elements, and be sure to not include the median in your upper and lower data sets.

Input Format

The first line contains an integer, , denoting the number of elements in arrays  and .
The second line contains  space-separated integers describing the respective elements of array .
The third line contains  space-separated integers describing the respective elements of array .

Constraints

, where  is the  element of array .
, where  is the  element of array .
The number of elements in  is equal to .
Output Format

Print the interquartile range for the expanded data set on a new line. Round your answer to a scale of  decimal place (i.e.,  format).

Sample Input

6
6 12 8 10 20 16
5 4 3 2 1 5
Sample Output

9.0
"""

def get_nums(x,w):
    nums = []
    for i,j in zip(x,w):
        num = [i]*j 
        for element in num:
            nums.append(int(element))
    nums.sort()
    return nums


def median(nums):
    if len(nums) % 2 == 0:
        return sum(nums[len(nums)//2-1 : len(nums)//2+1])/2
    else:
        return nums[len(nums)//2]

def quartile(nums):
    Q2 = median(nums)
    Q1 = median(nums[:len(nums)//2])
    Q3 = median(nums[(len(nums)+1)//2:])
    return Q1, Q2, Q3


n = int(input())
x = list(map(int, input().split(' ')))
w = list(map(int, input().split(' ')))
nums = get_nums(x, w)
Q1, Q2, Q3 = quartile(nums)
IQR = Q3 - Q1

print (IQR)
