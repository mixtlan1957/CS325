#Program Filename: mergesort.py (Assignment1)
#Author: Mario Franco-Munoz
#Due Date: 4/8/2018
#Description: This file implements the merge sort function. Reads numeric values from a text file
#loads the values into an array and applies the merge sort. Output is then stored to merge.out file.


import random
import sys
import os
import random
import time


def merge2(arr, left, right):
    for i in range(len(left)):
        arr[i]=left[i]
    i += 1
    for j in range(len(right)):
        arr[i]=right[j]
        i+=1




#function: worstCaseMergeFill
def worstCaseMergeFill(arr):
    

    if(len(arr) <= 1):
        return
    if(len(arr)==2):
        arr[0], arr[1] = arr[1], arr[0]
        return

    
    #m = int((len(arr) + 1) /2)
    left = []
    right = []

    #i = 0
    j = 0
    for i in range(0, len(arr), 2):
 
         left.append(arr[i])
         j+=1
    
    #i = 1
    j = 0
    for i in range(1, len(arr), 2):
        
        right.append(arr[i])
        j += 1
    
    worstCaseMergeFill(left)
    worstCaseMergeFill(right)

    return merge2(arr, left, right)
    





#function: randArrayFill
#simple function to populate a predefined array with integers between 1 and 10,000
#generate random numbers between 1 and 10,000
def randArrayFill(arr, n):
    for i in range(n):
        arr.append(random.randint(1, 10001))


#function: mergeSort
#merge sort in python code based on pseduo code found on wikipedia mergesort article:
# https://en.wikipedia.org/wiki/Merge_sort
#input: input array to be sorted
#output: sorted array (original array is not modified)
def mergeSort(numbers):
	if len(numbers) <= 1:
		return numbers

	middle = int(len(numbers)/2)
	left = mergeSort(numbers[:middle])
	right = mergeSort(numbers[middle:])

	return merge(left, right)

def merge(left, right):
    if len(left) == 0 or len(right) == 0:
        return left or right
    
    
    result = []
    i = 0
    j = 0


    while (len(result) < len(left) + len(right)):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break


    return result



numbers = []
for i in range(10):
    numbers.append(i)


#randArrayFill(numbers, 15000)

worstCaseMergeFill(numbers)
for i in range(len(numbers)):
    print("%d " %numbers[i], end="")
print()

start = time.clock()


#store sorted array
numbersSorted = mergeSort(numbers)


end = time.clock()

milSeconds = float((end-start) *1000)

#display run time
print("Algorithm took %f milliseconds" %milSeconds)

