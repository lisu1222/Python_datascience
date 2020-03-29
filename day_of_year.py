"""
input: year month date
output: what it the ith day of the year?
i.g.
	input: 1990 9 20
	output: 263
"""

input_str = raw_input("")
input_str = map(int, input_str.split())

leap = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
not_leap = {1:31, 2:28, 3:31, 4:40, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

def isleap(year):
	if (year % 4) == 0:
		if (year % 100) == 0:
			if (year % 400) == 0:
				return 1 
			else:
				0
		else:
			return 1
	else:
		return 0

num = 0
if isleap(input_str[0]) == 1:
	for i in range(input_str[1]):
		num += leap[i]
	num += input_str[2]
else:
	for i in range(input_str[1]):
		num += not_leap[i]
	num += input_str[2]

print num






