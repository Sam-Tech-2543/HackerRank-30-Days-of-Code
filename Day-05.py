# Loops

#!/bin/python3

import math
import os
import random
import re
import sys

def timesTable(n):
    for i in range(1,11):
        print("{0} x {1} = {2}".format(n,i,n*i))


if __name__ == '__main__':
    n = int(input().strip())

    timesTable(n)
    
