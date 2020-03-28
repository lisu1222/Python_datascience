class Rotatiion(object):
	"""
	to tell whether a string is the rotation of another string - rotation 
	means to slice s1 at any place, then swap the two slices to make a new string as s2
	"""
	def is_substring(self, s1, s2):
		"""output whether s1 is the substring of s2"""
		return s1 in s2

	def is_rotation(self, s1, s2):
		"""
		output whether s2 is the rotation of s1
		"""
		if s1 == None or s2 == None:
			return False
		if len(s1) != len(s2):
			return False
		else:
			return self.is_substring(s1, s2+s2)