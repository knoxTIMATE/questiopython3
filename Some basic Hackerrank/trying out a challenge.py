#!/bin/python3

import math
import os
import random
import re
import sys
global n
#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here

    pdiag_sum=0
    sdiag_sum=0
    for i in range (0, n):
        for j in range (0, len(arr[i])):
            if i==j:
                pdiag_sum+=arr[i][j]
                print (arr[i][j])
            else:
                continue

    for i in range (0, n):
        for j in range ( 0, len(arr[i])):
            if i+j==2:
                sdiag_sum+=arr[i][j]
                print (arr[i][j])
            else:
                continue

    diff=pdiag_sum-sdiag_sum

    if diff<0:
        diff*=-1
    
    
    return diff 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
