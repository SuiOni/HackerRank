#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque 

# Complete the matrixRotation function below.
def matrixRotation(matrix, r):
    m = len(matrix) # width of matrix
    n = len(matrix[0]) # heigth of matrix

    # init 2D list containing the circular path to rotate 
    # because of the contraint min(m,n)%2=0 have maximum min(m,n)/2 paths 
    circles = [[]] * int(min(m,n) / 2)

    # fill the circles with the correct walked path
    for c_i in range(len(circles)):
        circles[c_i] = walk(m,n,c_i,matrix)
    
    # rotate them with pythons deque data structure (functional)
    for circle in circles:
        circle.rotate(r)
    
    # now fill the original matrix back up with the shifted cyclic path accordingly
    for i, circle in enumerate(circles):
        unwalk(m,n,i,matrix, circle)

    printMatrix(matrix)
    
# walk the matrix in a circle and save the path
def walk(m,n, c_i,matrix):
    m_len = m - c_i * 2
    n_len = n - c_i * 2
    i= j = c_i
    path=[]
    
    for step in range(2*( m_len + n_len - 2 )):
        path.append(matrix[i][j])
        direction = getDir(m_len,n_len,step)
        i += direction[0]
        j += direction[1]
        
    return deque(path)
        
# walk the path and fill matrix (opposite of walk function)
def unwalk(m,n,c_i,matrix, circle):
    m_len = m - c_i * 2
    n_len = n - c_i * 2
    i = j = c_i
    
    for step, c in enumerate(circle):
        matrix[i][j] = c
        direction = getDir(m_len,n_len,step)
        i += direction[0]
        j += direction[1]
    

# check if were are going: down, left, up or right on the matrix
def getDir(m,n,step):
    directions=[[1,0], [0,1],[-1,0], [0,-1]]
    
    if 0 <= step < m-1:
        return directions[0]
    if m-1 <= step < m+n-2:
        return directions[1]
    if m+n-2 <= step < 2*m+n-3:
        return directions[2]
    return directions[3]
    
    
def printMatrix(matrix):
    for row in matrix:
        print(' '.join(str(x) for x in row))
    
    
if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)

