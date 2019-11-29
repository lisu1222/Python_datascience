"""
Is prime or not?
6x+1 or 6x+5 is prime

"""

from math import sqrt
num = int(input('Insert an integar: '))
end = int(sqrt(num))

#3个较小的数另外处理
if (num in range(1,3)):
    print('%d is not prime.' % num)
#不在6的倍数两侧的一定不是质数
elif num % 6 !=1 and num % 6 != 5:
    print('%d is not prime.' % num)
#在6的倍数两侧的也可能不是质数
    
elif num
    for i in range(1, end+1):
        if num % i == 0:
            print('%d is not prime.' % num)
            break
else:
    print('%d is prime.' % num)

          

          
