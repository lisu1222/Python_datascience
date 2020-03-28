class Permutations(object):

	def is_permutation(self, str1, str2):
	"""
	Return whether a string is permutation of another string's characters
	"""	
	if str1 == None or str2 == None:
		return False
	else:
		return sorted(str1) == sorted(str2)