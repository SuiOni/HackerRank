#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):

  

    type = s[-2:]
    
    print(type)
    h = int(s.split(":")[0])
    if h == 12:
        if type == 'AM':
            return '00' + s[2:-2]
        return s[:-2]

    print(h)
    if type=='PM':
        return '{:02d}{}'.format((h + 12) % 24, s[2:-2])
    return s[:-2]

    # Write your code here.
    #

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()

