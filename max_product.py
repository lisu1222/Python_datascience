'''
Input a list of strings, find two strings with only different characters and 
output the maximum product of lenghs of the two strings.
e.g. 
words = ['abcd','wxyh','defgh'], then the two strings with only different 
characters are 'abcd' and 'wxyh', output 16.
words = ['a','aa','aaaaa'], no two strings meet the requirement, output 0.

'''

import sys

def have_same_char(a,b):
	for i in a:
		if i in b:
			return True
	return False


if __name__ == "__main__":
	s = [ word[1:-1] for word in input().strip()[1:-1].split(',')]
	ans = 0
	for i in range(len(s)):
		for j in range(i+1, len(s)):
			if not have_same_char(s[i], s[j]):
				ans = max(ans, len(s[i])*len(s[j]))
	print (ans)
