#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 11:13:53 2019

@author: amit
"""

import os
import numpy as np
import pandas as pd

## INPUTTING THE INTEGER VALUES...

N = int(input())
arr = input()   # takes the whole line of n numbers
RA = list(map(int,arr.split(' '))) # split those numbers with space( becomes ['2','3','6','6','5']) and then map every element into int (becomes [2,3,6,6,5]

#data = []
#n = int(raw_input('Enter how many elements you want: '))
#for i in range(0, n):
#    x = raw_input('Enter the numbers into the array: ')
#    data.append(x)
#print(data)

ref_RA = [1,2,3,4,5,6]
counterArr = [] 
count = 1
i=j=0  

for k in range(7):
    print('k=', k)
    if i>j or i==0:
        j=i
        if RA[i]==RA[-i-1] and RA[i]==ref_RA[count-1]:
           
            print('i=',i,'RA= ',RA[i],'count= ', count-1, 'ref_RA=',ref_RA[count-1])
            i+=1
            
        counterArr.insert(count-1, i+1-j)
        count += 1
        print('the "i"={0} and "j"= {1}'.format(i, j))
        print('count=', count)
        continue
    else:
        print("No more Rainbow")
        break
        
else:
    print('out of For-loop')
    
        
        
#for i in range(len(RA)):
#     if(RA[i]==RA[-i-1]):
#         
#     else: print('False')


################################

T = int(input('Enter the number of test cases= '))
for i in range(T):
    N = int(input())
    arr = input()   # takes the whole line of n numbers
    RA = list(map(int,arr.split(' '))) # split those numbers with space( becomes ['2','3','6','6','5']) and then map every element into int (becomes [2,3,6,6,5]

    ref_RA = [1,2,3,4,5,6,7]
    counterArr = [] 
    count = 0
    i=j=0  
        
    
    if RA[int(N/2)] == ref_RA[-1]:
        while i<int(N/2):
            #print('i=',i)
            if RA[i]==ref_RA[count]:
                
                #print('i={0}, RA={1}, ref_RA= {2}'.format(i,RA[i], ref_RA[count]))
                
                if RA[i]==RA[-i-1]:
                    #print('i={0},RA={1},RA_back= {2}'.format(i,RA[i], RA[-i-1]))
                    i+=1
                    continue
            else:
                #print('count=',count)
                count+=1
                
                continue
     
    if i==int(N/2) and N%2==0: 
        print('the given array is a Rainbow Array')
    elif i==int(N/2) and N%2!=0:
        if RA[i]==ref_RA[-1]:
            print('the given array is a Rainbow Array')
            
    else: 
        print('the given array is Not a Rainbow')
        
#else:
#    while i<int(N/2):
#        if RA[i]==ref_RA[count]:
#            if RA[i]==RA[-i-1]:
#                i+=1
#                continue
#        else:
#            count+=1
#            continue
#
#    if i==int(N/2): 
#        print('Rainbow')
#    else: 
#        print('Not Rainbow')



