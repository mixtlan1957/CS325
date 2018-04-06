#Program Filename: insertsort.py (Assignment1)
#Author: Mario Franco-Munoz
#Due Date: 4/8/2018
#Description: This file implements the insert sort function. Reads numeric values from a text file
#loads the values into an array and applies the merge sort. Output is then stored to insert.out file.


import random
import sys
import os

numbers = []


f = open('data.txt', 'r')
lines = f.readlines()


for line in lines:
    
    numbers = [int(num) for num in line.split()]

f.close()




def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    
   


#insert sort implementation function based on pseudo code
#found on wikipedia: https://en.wikipedia.org/wiki/Insertion_sort
#input: array to be sorted, and length of array
#output: input array is sorted in place
def insertSort(arr, n):
    i = 1
    
    while i < n:
        j = i
        
        while j > 0 and (arr[j-1] > arr[j]):
            
            swap(arr, j, j-1)
            j = j - 1
            
        i = i + 1




n = len(numbers)
insertSort(numbers, n)


#save results to output file
with open('insert.out', 'w') as outfile:
    for num in numbers:
        outfile.write('%d ' %num)
