"""
for loop to calculate the sum of odd numbers between 1 to 100
"""

sum = 0
for x in range(2,101,2):
    sum += x
print(sum)


"""
Alternatively using for + if
"""

sum = 0
for x in range(1, 101 ):
    if x % 2 == 0:
        sum += x
print(sum)
