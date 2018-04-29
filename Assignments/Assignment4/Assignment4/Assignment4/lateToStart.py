#Program Filename: lateToStart.py (Assignment4)
#Author: Mario Franco-Munoz
#Due Date: 4/29/2018
#Description: This file implements a late-to-start greedy algorithm that allocates activities
# based on the latest available start time.




def lateToStart(activitiesMap):
    greedySolution = []

    #sort activities based on starting time and then reverse so that we may
    #select activities based on latest start time
    taskList = sorted(activitiesMap, key=lambda k: k['start'])
    taskList.reverse()

    #first activity always gets selected
    i = 0
    greedySolution.append(taskList[i]['id'])
    
    #if the activity being considered has a end time less than or equal to the start time
    #of previously selected activity, select it
    for j in range(1, len(taskList)):
        if taskList[j]['end'] <= taskList[i]['start']:
            greedySolution.append(taskList[j]['id'])
            i = j

    #since activities were added to the solution list "backwards," reverse the list prior to return
    greedySolution.reverse()
    return greedySolution
   


#open input data file in ready mode
f = open('act.txt', 'r')
lines = f.readlines()
lineCount = 0
f.close()


lineCount = int(len(lines))
activities = []
setCounter = 0;
lineNumber = 0;
#for lineNumber in range(0, lineCount):
while lineNumber < lineCount:
    #read how many activites need to be stored/saved
    numOfEntries = int(lines[lineNumber].strip('\n'))
    setCounter = setCounter + 1
    
    lineNumber = lineNumber + 1
   
    #store the values of each activity
    for i in range(lineNumber, lineNumber + numOfEntries):
        temp = [int(x) for x in (lines[i].strip().split(" "))]
        activities.append({'id': temp[0], 'start': temp[1], 'end': temp[2]})
        lineNumber = lineNumber + 1   #update line counter


    #call lateToStart
    greedyOutput = lateToStart(activities)

    #output results
    print("Set " + str(setCounter))
    print("Number of activities selected = " + str(numOfEntries))
    print("Activities:", end=" ")
    for i in greedyOutput:
        print(i, end=" ")
    print("\n")

    #reset/clear activities list
    activities = []  



