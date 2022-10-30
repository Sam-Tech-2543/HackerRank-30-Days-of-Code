#https://www.hackerrank.com/challenges/30-2d-arrays/problem

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    # for Testing
    arr=[[1, 1, 1, 0, 0, 0], 
         [0, 1, 0, 0, 0, 0], 
         [1, 1, 1, 0, 0, 0], 
         [0, 0, 2, 4, 4, 0], 
         [0, 0, 0, 2, 0, 0], 
         [0, 0, 1, 2, 4, 0]]

        
    lst=[]

    s=0
    r=0
    for z in range(4):
        s=0
        for i in range(4):
            ans=0
            for j in range(3):
                ans+=(arr[r][s+j]+arr[r+2][s+j])
            ans+=arr[r+1][i+1]
            s+=1
            lst.append(ans)
        r+=1

    print(max(lst))




        