'''
create classes and return grouped frequency table
'''
def create_classes(numbers, n): 
    low = min(numbers)
    high = max(numbers)
    # Width of each class
    width = (high - low)/n
    classes= []
    a = low 
    b = low + width
    classes= []
    while a< (high-width):
        classes.append((a, b)) 
        a= b
        b = a + width
# The last class may be of a size that is less than width
    classes.append((a, high+1))
    return classes

def grouped_freq(numbers,classes,n=3):
    count_class_1 = 0
    count_class_2 = 0
    count_class_3 = 0
    for i in numbers:
        if i<= classes[0][1]:
            count_class_1+=1
        elif i>classes[0][1] and i<= classes[1][1]:
            count_class_2+=1
        else:
            count_class_3+=1
    freq = [count_class_1, count_class_2, count_class_3]
    for ci,fi in zip(classes,freq):
        print (ci,fi)
    
if __name__=='__main__':
    donations = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
    classes = create_classes(donations,3)
    print('Class\tFrequency')
    grouped_freq = grouped_freq(donations, classes, n=3)
    print(grouped_freq)
   
