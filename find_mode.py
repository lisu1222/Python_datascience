
#find the mode of a list

def mode(data):
	modecnt = 0
	for i in range(len(data)):
		icount = data.count(data[i])
		if icount > modecnt:
			mode = data[i]
			modecnt = icount
	return mode

data1 = [1,2,5,10,-20,5,5]
print mode(data1)
