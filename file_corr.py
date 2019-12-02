def read_csv(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)
        
        rainfall = []
        highest_correlated = []
        for row in reader:
            rainfall.append(float(row[1]))
            highest_correlated.append(float(row[2]))
            
        return rainfall, highest_correlated
        

import matplotlib.pyplot as plt
import csv

if __name__ == '__main__':
    rainfall, highest_correlated = read_csv('correalte-Annual_Rainfall.csv')
    corr = find_corr_x_y(rainfall, highest_correlated)
    print('Highest correlation:{0}'.format(corr))
    
