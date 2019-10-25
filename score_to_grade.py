"""
Convert Percent Score to Letter Grade
"""

score = float(input('Percent Score: '))
if score >= 90:
    grade  = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print('Corresponding letter grade is: ', grade)
    
