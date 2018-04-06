#Program Filename: mergesort.py (Assignment1)
#Author: Mario Franco-Munoz
#Due Date: 4/8/2018
#Description: This file implements the merge sort function. Reads numeric values from a text file
#loads the values into an array and applies the merge sort. Output is then stored to merge.out file.


import random
import sys
import os


numbers = []

f = open('data.txt', 'r')
lines = f.readlines()

#load contents of text file to array
for line in lines:
   
    numbers = [int(num) for num in line.split()]

f.close()

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




n = len(numbers) - 1

#store sorted array
numbersSorted = mergeSort(numbers)


#save results to output file
with open('merge.out', 'w') as outfile:
    for num in numbersSorted:
        outfile.write('%d ' %num)
