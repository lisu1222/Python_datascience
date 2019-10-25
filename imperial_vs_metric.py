"""
British Imperial System vs. Metric System
"""

value = float(input('Length: '))
unit = input('Measurement unit: ')
if unit == 'in' or unit == 'inch':
    print('%.5finch = %.5fcm' % (value, value * 2.54))
elif unit == 'cm' or unit == 'centimeter':
    print('%.5fcm = %.5finch' % (value, value/2.54))
else:
    print('Please put in valid unit')
