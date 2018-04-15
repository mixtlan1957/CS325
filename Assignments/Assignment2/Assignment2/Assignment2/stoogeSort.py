
#Program Filename: stoogesort.py (Assignment2)
#Author: Mario Franco-Munoz
#Due Date: 4/15/2018
#Description: This file implements the "stooge sort" function. Reads numeric values from a text file
#loads the values into an array and applies the sort. Output is then stored to merge.out file.


import random
import sys
import os
import math
import random




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



output_lines = []

#open input data file in read mode
f = open('data.txt', 'r')
lines = f.readlines()
lineCount = 0


for line in lines:
    lineCount = lineCount + 1
    numbersToSort = line[0]
    numbers = [int(x) for x in line.strip().split(" ")]
    numbers.pop(0)
    stoogeSort(numbers, 0, len(numbers) - 1)
    #print("Sorted numbers in line " + str(lineCount) + ":   " + str(len(numbers)) + " numbers.")
    output_lines.append(" ".join([str(x) for x in numbers]))



f.close()

with open('stooge.out', 'w') as outfile:
    for line in output_lines:
        outfile.write(line + "\n")

outfile.close()
        


