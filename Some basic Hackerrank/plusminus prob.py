#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
	poscount=0
	negcount=0
	zerocount=0
	for num in arr:
		if num <0:
			negcount+=1
		elif num > 0:
			poscount+=1
		else:
			zerocount+=1
	print (float(poscount)/len(arr))
	print (float(negcount)/len(arr))
	print (float(zerocount)/len(arr))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
