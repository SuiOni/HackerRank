#!/bin/python3

import math
import os
import random
import re
import sys
import functools

# Complete the plusMinus function below.
def plusMinus(arr):
    p_count = functools.reduce(lambda a,b: a + int(b<0), arr, 0)
    n_count = functools.reduce(lambda a,b: a + int(b>0), arr, 0)
    z_count = functools.reduce(lambda a,b: a + int(b==0), arr, 0)

    print("{:.6f}".format(n_count/len(arr)))
    print("{:.6f}".format(p_count/len(arr)))
    print("{:.6f}".format(z_count/len(arr)))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

