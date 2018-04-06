#Program Filename: insertsort.py (Assignment1)
#Author: Mario Franco-Munoz
#Due Date: 4/8/2018
#Description: This file implements the insert sort function. Reads numeric values from a text file
#loads the values into an array and applies the merge sort. Output is then stored to insert.out file.



import random
import sys
import os
import random
import time


#function: reverseArrayFill
#this function fills an array with a decreasing order
#with this reverse ordering we can obtain the worst case run time scenario
#for the insert sort as requried for the extra credit portion of assignment1
def reverseArrayFill(arr, n):
    for i in range(n):
        arr.append(n-i)



#function: randArrayFill
#simple function to populate a predefined array with integers between 1 and 10,000
#generate random numbers between 1 and 10,000
def randArrayFill(arr, n):
    for i in range(n):
        arr.append(random.randint(1, 10001))


#simple swap function for implementation of insert sort
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


numbers = []

#randArrayFill(numbers, 15000)

reverseArrayFill(numbers, 10)


start = time.clock()

#execute the insert sort algorithm
n = len(numbers)
insertSort(numbers, n)

end = time.clock()

milSeconds = float((end-start) *1000)

#display run time
print("Algorithm took %f milliseconds" %milSeconds)