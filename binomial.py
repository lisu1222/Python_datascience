"""
Objective
In this challenge, we go further with binomial distributions. We recommend reviewing the previous challenge's Tutorial before attempting this problem.

Task
A manufacturer of metal pistons finds that, on average,  of the pistons they manufacture are rejected because they are incorrectly sized. What is the probability that a batch of  pistons will contain:

No more than  rejects?
At least  rejects?
Input Format

A single line containing the following values (denoting the respective percentage of defective pistons and the size of the current batch of pistons):

12 10
If you do not wish to read this information from stdin, you can hard-code it into your program.

Output Format

Print the answer to each question on its own line:

The first line should contain the probability that a batch of  pistons will contain no more than  rejects.
The second line should contain the probability that a batch of  pistons will contain at least  rejects.
Round both of your answers to a scale of  decimal places (i.e.,  format).
"""

def fac(n):
    return 1 if n == 0 else n*fac(n-1)

def comb(x,n):
    return fac(n)/(fac(x)*fac(n-x))

def bi_pdf(x,n,p):
    return comb(x,n)*(p**x)*(1-p)**(n-x)


p, n = list(map(int, input().strip().split(' ')))

print(round(sum([bi_pdf(i,n,p*0.01) for i in range(3)]), 3))
print(round(sum([bi_pdf(i,n,p*0.01) for i in range(2,n+1)]),3))