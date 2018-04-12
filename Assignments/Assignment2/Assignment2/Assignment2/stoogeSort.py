
#Program Filename: stoogesort.py (Assignment2)
#Author: Mario Franco-Munoz
#Due Date: 4/15/2018
#Description: This file implements the "stooge sort" function. Reads numeric values from a text file
#loads the values into an array and applies the sort. Output is then stored to merge.out file.


import random
import sys
import os
import math



numbers = []

#open input data file in read mode
f = open('data.txt', 'r')
lines = f.readlines()

#load contents of text file to list
for line in lines:
   
    numbers = [int(num) for num in line.split()]

f.close()


#last stooge attempt
def stoogeSort2(A):
    n = len(A)
    if n == 2 and A[0] > A[1]:
        temp = A[0]
        A[0] = A[1]
        A[1] = temp
        return A
    elif n > 2:
        m = math.ceil(2*n/3)
        A = A[0:m]
        stoogeSort2(A)
        A = A[n-m:]
        stoogeSort2(A)
        A = A[0:m]
        stoogeSort2(A)
    else:
        return A
        


#function: stoogeSort
#input: input list to be sorted
#output: input list is modified (sorted)
#The solution for this problem was in part realized with the help of:
#https://www.geeksforgeeks.org/python-program-for-stooge-sort/
#(although the implementation here is different since we are swapping at adjacent array elements)
def stoogeSort(arr, start, end):
    #base case
    if start >= end:
        return
  
   #swap if applicable (check if indexes are adjacent: A[0], A[1]
    elif end - start == 1: 
        if arr[start]>arr[end]:
            arr[start], arr[end] = arr[end], arr[start]
            
    
    if end-start+1 > 2:
        t = (int)((end-start+1)/3)
        oneThird = math.ceil((end - start)/3)
  
        # Recursively sort first 2/3 elements
        stoogeSort(arr, start, (end-oneThird))
  
        # Recursively sort last 2/3 elements
        stoogeSort(arr, start + oneThird, end)
  
        # Recursively sort first 2/3 elements
        # again to confirm
        stoogeSort(arr, start, (end - oneThird))



#call stoogeSort
#stoogeSort2(numbers)
stoogeSort(numbers, 0, len(numbers) - 1)

#save results to output file
with open('stooge.out', 'w') as outfile:
    for num in numbers:
        outfile.write('%d ' %num)