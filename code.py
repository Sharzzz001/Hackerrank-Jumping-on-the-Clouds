#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    count=0
    n = len(c)-1
    i=0
    while(i<n):
        if(i+2<=n and c[i+2]==0):
            i+=2
            count+=1
        elif(i+1<=n and c[i+1]==0):
            i+=1
            count+=1
        else:
            return count
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
