'''
creating a frequency table
'''

from collections import Counter

def frequency_table(numbers):
    table = Counter(numbers).most_common()
    print('Number\tFrequency')
    for num in table:
        print('{0}\t{1}'.format(num[0],num[1]))
        
if __name__ == '__main__':
    scores = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
    frequency_table(scores)
    
