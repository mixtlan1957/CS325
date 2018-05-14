#Program Filename: babyfacesHeels.py (Assignment5)
#Author: Mario Franco-Munoz
#Due Date: 5/13/2018
#Description: This program implements a graph between wreslers and determines if
# the given rivalries are compatible with the given wrestlers



import sys
import os
from collections import defaultdict
 


class Graph:

    #constructor
    def __init__(self):
        self.graph = {}          #the graph itself
        self.wrestlersMap = {}   #a map for keeping track of which fighter is part of which team

    #takes input as form of a list and adds all nodes with empty type and empty set
    def addVerticies(self, listInput):
        for i in listInput:
            emptySet = set()
            self.graph[i] = emptySet
            self.wrestlersMap[i] = None


    def addConnection(self, origin, destination):
        connections = self.graph[origin]
        connections.add(destination)
        self.graph[origin] = connections


    #citation: https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
    # and https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
    #modified to fit purpose of this assignment
    def BFS(self, wrestlers):
        babies = []
        heels = []
        queue = []

        #self.wrestlersMap[start]["team"] = "baby"
        #self.wrestlersMap[start]["checked"] = True
        #babies.append(start)
        #queue.append(start) 


        while wrestlers:
            start = wrestlers[0]

            self.wrestlersMap[start]["team"] = "baby"
            self.wrestlersMap[start]["checked"] = True
            babies.append(start)
            queue.append(start) 


            wrestlers.remove(start)


            while queue:
                s = queue.pop(0)

                #modification to original BFS:
                #assign neighbors the opposite team, however if the neighboring node already has a team
                #assignment equal to that of the examined node return with not possible.
                for i in self.graph[s]:     #for each neighboring node:

                    if self.wrestlersMap[s]["team"] == self.wrestlersMap[i]["team"]:
                            return "No", [], []

                    if self.wrestlersMap[i]["checked"] == False:
                        queue.append(i)
                        self.wrestlersMap[i]["checked"] = True
                        wrestlers.remove(i)

                    
                        #assign the neighbors the appropriate team (opposite of current node)
                        if self.wrestlersMap[s]["team"] == "baby":
                            self.wrestlersMap[i]["team"] = "heel"
                            heels.append(i)

                        elif self.wrestlersMap[s]["team"] == "heel":
                            self.wrestlersMap[i]["team"] = "baby"
                            babies.append(i)


        #return final result
        babies.sort()
        heels.sort()
        return "Yes", babies, heels



#babyfaces-vs-heels
#input: rivalries must be a list of lists: a node pair forming an edge representing a rivalry.
# for example r[0][0] = wrestler1, r[0][1] = wrestler2
# wrestlers is a list of wrestlers
#output: returns wether it was possible to allocate the rivalries. If allocation was a success, 
# function returns Yes followed by list of babyfaces and subsequently heels.
# otherwise function retrurns "No"
def babyHeel(wrestlers, rivalries):
    
    g = Graph()
    #append the verticies



    #for i in range (1, len(wrestlers)):
    g.addVerticies(wrestlers)
    
    #initialize status map
    for i in range (0, len(wrestlers)):
        g.wrestlersMap[wrestlers[i]] = {"team": None, "checked": False}

     
    #append the connections
    for i in range (0, len(rivalries)):
        g.addConnection(rivalries[i][0], rivalries[i][1])
        g.addConnection(rivalries[i][1], rivalries[i][0])

    #call the modified BFS
    return g.BFS(wrestlers)





def main():

    #open input data file in read mode
    inputFile = sys.argv[1]
    assert os.path.exists(inputFile), "Error file could not be found or opened. Please check input .txt file and try again."
    f = open(inputFile, 'r')
    lines = f.readlines()
    lineCount = 0
    f.close()


    lineCount = int(len(lines))
    wrestlers = []
    rivalries = []

    #read wreslers and rivalries from file
    lineNumber = 0
    while lineNumber < lineCount:
        wrestlerCount = int(lines[lineNumber].strip('\n'))
        lineNumber = lineNumber + 1

        #store the wrestlers
        for i in range(lineNumber, lineNumber + wrestlerCount):
            temp = str(lines[lineNumber].strip('\n'))
            wrestlers.append(temp)
            lineNumber = lineNumber + 1   #update line counter

        #get the rivalry count
        rivalryCount = int(lines[lineNumber].strip('\n'))
        lineNumber = lineNumber + 1

        #store the rivalries in a list of lists
        for i in range(lineNumber, lineNumber + rivalryCount):
            temp2 = [str(x) for x in (lines[i].strip().split(" "))]
            tempList = []
            tempList.append(temp2[0])
            tempList.append(temp2[1])
            rivalries.append(tempList)
            lineNumber = lineNumber + 1

        #force the while loop to ignore any additional information
        lineNumber = lineCount
    

    #call main driver function and print results
    result, babiesList, heelsList = babyHeel(wrestlers, rivalries)
    
    #print results
    if result == "No":
        print("// Impossible")

    #if it is possible, print out the different elements in result arrays
    elif result == "Yes":
        print("Yes Possible")
        print("BabyFaces: ", end ="")
        for i in range(0, len(babiesList)):
            print(babiesList[i], end=" ")

        print("")

        for i in heelsList:
            print(i, end=" ")

        print("")
 
    '''

    #code test
    for i in wrestlers:
        print("%s", i, end=" ")
    print("\n")

    for i in rivalries:
        print("%s %s", i[0], i[1], end=" ")
    print("\n")

    '''

if __name__ == '__main__':
    main()