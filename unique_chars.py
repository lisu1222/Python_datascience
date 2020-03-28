class UniqueChars(object):

	def has_unique_chars(self, string):
		if string is None:
			return False
		else:
			return set(string)==len(string)