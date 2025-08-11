import sys
# import numpy as np
# import pandas as pd
# from sklearn import ...

for line in sys.stdin:
    #print(line, end="")
    i = 0
    longest_word = []
    current_word = []


    while i < len(line):

        if line[i] == " " or i == (len(line) - 1):

            if len(current_word) > len(longest_word):
                longest_word = current_word

            current_word = []
            i += 1
            continue

        else:
            current_word.append(line[i])

        i += 1



    print(''.join(longest_word))
