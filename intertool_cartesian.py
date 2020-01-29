# Example
# A = [1, 2]
# B = [3, 4]
# AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]
# Note: A and B are sorted lists, and the cartesian product's tuples should be output in sorted order.

# Input Format
# The first line contains the space separated elements of list A. 
# The second line contains the space separated elements of list B.

# Both lists have no duplicate integer elements.

# Constraints
# 0 < A < 30
# 0 < B < 30
 
# Output Format
# Output the space separated tuples of the cartesian product.

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

A = input("Please enter two digits separated by space").split()
A = list(map(int, A))
B = input("Please enter two digits separated by space").split()
B = list(map(int, B))

for i in product(A, B):
    print (i)