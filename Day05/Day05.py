import datetime
import re

def MoveCrates(currMove):    
    """Move the crates according to the move command """
    # Loop through each character and find the occurrences in the string
    # If there's more than 1, it's not unique
    pass

def FindNumbersInString(string):    
    """Find all positive AND negative integers in a string """
    res = [int(d) for d in re.findall(r'-?\d+', string)]
    return res

def PopulateStartingPileArrays(pileStr,numPiles):
    startIndex = 1
    stepIndex = 4
    rowIndex = 0
    piles = []

    #Create a 2d array where [pile][stack]
    # the stack list is built from the bottom to the top
    for pile in range(0,numPiles):
        stackList = []
        for height in range(len(pileStr)-1,-1,-1):
            #print(height)
            #print(pileStr[height])
            rowStr = pileStr[height]
            char = rowStr[startIndex + (stepIndex*pile)]
            if char.isalpha():
                # it's a character, put it on the 
                #print(char)
                #print('pile=',pile,'row=', rowIndex)
                stackList.append(char)
                 #Put the crates in the rows and piles
    
        piles.append(stackList)
    return piles  

print("The date and time is:",datetime.datetime.now())

#read in the data
with open('input.txt','r') as f:
    array = f.readlines()
f.close()

# find crate configuration
for i in range(len(array)):
    if(array[i].find(' 1 ',0,4))>=0 :
        print(array[i])
        numPiles = max(FindNumbersInString(array[i]));
        print('Num Piles:',numPiles)
        pileConfigStr = array[0:i]
        # find move list
        moveList = array[i+2:]
        print(pileConfigStr)
        break

# create a 2d list array for crate configuration
pileArray = PopulateStartingPileArrays(pileConfigStr,numPiles)
print(moveList)
print(pileArray)   
partPiles = [x[:] for x in pileArray] # save a copy for later

# top crate is the last item on the crate list
# Send the moves 1 at a time to modify the crate arrays
for i in range(len(moveList)):
    if moveList[i].find('move') < 0:
        break
    move = FindNumbersInString(moveList[i])
    numCrates = move[0]
    startPile = move[1]-1
    destPile = move[2]-1
    print(moveList[i])
    print(move)
    for j in range(move[0]):
        #Move a box from the start pile to the dest
        crate = pileArray[startPile].pop()
        pileArray[destPile].append(crate)

print (pileArray)



# test find all numbers in a string
outputList = []
for i in range(numPiles):
    outputList.append(pileArray[i][-1])

print ('Part 1:',*outputList)


pileArray =  [x[:] for x in partPiles]
#Part 2: Now we can move multiple items at once
# Send the moves 1 at a time to modify the crate arrays
for i in range(len(moveList)):
    if moveList[i].find('move') < 0:
        break
    move = FindNumbersInString(moveList[i])
    numCrates = move[0]*-1
    startPile = move[1]-1
    destPile = move[2]-1
    endIndex = len(pileArray[destPile])
    print(moveList[i])
    print(move)
    crates = pileArray[startPile][numCrates::1]
    pileArray[destPile][endIndex:endIndex] = crates
    numCrates = numCrates * -1
    # Pop off the number of crates
    for j in range(numCrates):
        junk = pileArray[startPile].pop()

print (pileArray)



# test find all numbers in a string
outputList = []
for i in range(numPiles):
    outputList.append(pileArray[i][-1])

print ('Part 2:',*outputList)



