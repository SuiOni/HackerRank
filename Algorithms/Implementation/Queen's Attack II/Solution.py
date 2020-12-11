#!/bin/python3

import math
import os
import random
import re
import sys

#All possible direction unit vectors
DIRECTIONS = [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1),(1,-1)]

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    map_obstacles=[None] * 8
        
    # fill the list with all the "edge obstacles" of the map 
    # with index denoting the direction
    for i, el in enumerate(map_obstacles):
        map_obstacles[i] = getMapObstacle(i, n, r_q, c_q)
    
    # now for every obstacle check if it is closer 
    # than the map obstacle of the same direction and exchange accordingly
    for obs in obstacles:
        direct = getDirection((r_q,c_q), obs)
        if direct is not None: 
            if sDistance(map_obstacles[direct], (r_q, c_q)) > sDistance(obs, [r_q, c_q]):
                print("found new obstacle closer to queen!")
                print("changed obstacle",map_obstacles[direct], "with", obs)
                map_obstacles[direct] = (obs[0],obs[1])
    
    # sum all the empy squares between the final list of closest obstacles
    attack_possibilities = 0
    for obs in map_obstacles:
        dist = sDistance(obs, (r_q, c_q))
        if dist is not None:
            attack_possibilities += max(dist-1, 0)
        
    return attack_possibilities
                
# get the edge of the map depending on the direction from the queen
def getMapObstacle(step, n, r_q, c_q):
    while r_q <= n and r_q > 0 and c_q <= n and c_q > 0:
        r_q += DIRECTIONS[step][0]
        c_q += DIRECTIONS[step][1]
    return (r_q, c_q)
    
# get the direction index of the unit vectors
def getDirection(a,b):
    dis = sDistance(a,b)
    if dis is None:
        return None
    for i, d in enumerate(DIRECTIONS):
        if a[0] + d[0] * dis == b[0] and a[1] + d[1] * dis == b[1]:
            return i
              
# distance between two squeres (only if they are in one line)
def sDistance(a,b):
    # same row distance
    if a[0] == b[0]:
        return abs(b[1]-a[1])
    # same col distance
    if a[1] == b[1]:
        return abs(b[0]-a[0])
    # vertical line distance
    if abs(b[0]-a[0]) == abs(b[1] - a[1]):
        return abs(b[1]-a[1])
    return None
    
   
    
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()

