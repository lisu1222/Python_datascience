"""
Determine whether the input length of three sides can make a triangle,
if yes calculate the perimeter and area of that triangle.
"""
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    print('Perimeter: %f' % (a + b + c))
    p = (a + b + c) / 2
    area = (p * (p - a) * (p -b) * (p - c)) ** 0.5
    print('Area: %f' % (area))
else:
    print("Can't make a triangle") 
