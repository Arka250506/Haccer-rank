import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    jumlah = len(arr)
    positif,negatif,nol = 0,0,0
    for bil in arr :
        if bil > 0 :
            positif += 1
        elif bil < 0 :
            negatif += 1
        else :
            nol += 1 
    print (positif/jumlah)        
    print (negatif/jumlah)  
    print (nol/jumlah)  
    #n = len(arr)
    #positif = len([bil for bil in arr if bil > 0])
    #negatif = len([bil for bil in arr if bil < 0])
    #nol = len ([bil for bil in arr if bil == 0])
    #print(positif/n)
    #print(negatif/n)
    #print(nol/n)
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
