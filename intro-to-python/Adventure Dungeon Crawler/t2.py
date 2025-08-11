import sys
# import numpy as np
# import pandas as pd
# from sklearn import ...

for line in sys.stdin:
    line = line.strip()
    mult = []
    i = 0
    line = line.split(' | ')

    while i < len(line):
        mult.append(line[i].split(" "))
        i += 1

    j = 0
    while j < len(mult[0]):
        print(int(mult[0][j]) * int(mult[1][j]))
        j += 1





        
