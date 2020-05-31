
def fact(n):
	return 1 if n == 0 else n*fact(n-1)


def comb(n, x):
	return  fact(n)/(fact(x) * fact(n-x))


def binomialPdf(x, n, p):
	return comb(n, x)*(p**x)*(1-p)**(n-x)


def binomialCdf_bottom(y, n, p):
	result = 0
	for i in range(y,n+1):
		result += binomialPdf(i, n, p)
	return result

def binomialCdf_up(y, n, p):
	result = 0
	for i in range(y+1):
		result += binomialPdf(i, n, p)
	return result
