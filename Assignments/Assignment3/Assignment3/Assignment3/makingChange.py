#Program Filename: makingChanage.py (Assignment3)
#Author: Mario Franco-Munoz
#Due Date: 4/22/2018
#Description: Application of the making change Dynamic Programming problem.


import sys
import os
import math


#function: makingChange
#input: Denomination set of coins used to make change with (V), positive integer value of ammount to add coins for (ammount)
#output: (minimum number of coins to make the exact change, list of coins used)
#description: this function finds the minimum number of coins based on a given denomination to add up to an input ammount.
def makingChange(V, amount):
    if amount == 0:
        return 0, []
    
    n = len(V)
   
    denomUsed = [0 for k in range(0, amount + 1)]

    C = [float('inf') for k in range(0, amount + 1)]
    C[0] = 0

    for j in range(1, amount + 1):
        
        
        for i in range(0, n):
            if j >= V[i]:
                if (1 + C[j - V[i]]) < C[j]:
                    C[j] = 1 + C[j - V[i]]
                    denomUsed[j] = V[i]


    
    
    
    #(minimum) number of coins to make change
    numberOfCoins = C[len(C) - 1]

    #retrace steps starting with the last element entered in the
    #denomUsed tracking array
    denomFinal = []
    p = amount
    while p > 0:
        
        denomFinal.append(denomUsed[p])
        p = p - denomUsed[p]
       
    

    return numberOfCoins, denomFinal


def resultsTally(denomUsed, denominationTypes):
    
    #initialize results list/tally
    results = [0 for k in range(0, len(denominationTypes))]

    numOfDenoms = len(denomUsed)
    numOfDiff_Coins = len(denominationTypes)

    for k in range (0, numOfDiff_Coins):
        for i in range(0, numOfDenoms):
            if (denomUsed[i] == denominationTypes[k]):
                results[k] = results[k] + 1

    return results



#open input data file in read mode
f = open('amount.txt', 'r')
lines = f.readlines()
lineCount = 0
f.close()

#open and truncate the output file
outfile = open('change.txt', 'w')
outfile.close


#read data from file: odd lines contain the denomination, even lines contain the number to sum up to
evenIndex = 0
oddIndex = 1
iterations = int(len(lines) / 2)
for line in range (0, iterations):
    
    
    
    #denomination
    coins = [int(x) for x in (lines[evenIndex].strip().split(" "))]
    
   
    #Value to sum for
    valueToSum = int(lines[oddIndex].strip('\n'))
    
    #call function, store values
    outputCoinCount, outputDenom = makingChange(coins, valueToSum)
    results = resultsTally(outputDenom, coins)
    

    with open('change.txt', 'a') as outfile:
        
        #copy over the denominations used
        numCoins = len(coins)
        for i in range (0, numCoins - 1):
            outfile.write(str(coins[i]))
            outfile.write(" ")
        outfile.write(str(coins[numCoins - 1]) + "\n")

        #copy over the number being added up to
        outfile.write(str(valueToSum) + "\n")

        #add the tally
        for i in range (0, numCoins - 1):
            outfile.write(str(results[i]) + " ")
        outfile.write(str(results[numCoins - 1]) + "\n")

        #output the minimum number of coins used
        outfile.write(str(outputCoinCount) + "\n")
    
    outfile.close()

    evenIndex = evenIndex + 2
    oddIndex = oddIndex + 2







