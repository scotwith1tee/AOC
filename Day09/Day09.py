import datetime
import re
X = 1
cycleIndex = 1
# This might fix the offset so array 20 is the 20th cycle
cycleList=[1,1]

def AddInstr(adder):    
    """Add a number to X and fill out the cycle log"""
    # Hard code the dissassembling of the instruction
    global X
    #Copy and add the last value in the list
    cycleList.append(cycleList[-1])
    #    X += adder
    #Copy and add the last value in the list
    X = cycleList[-1] + adder
    cycleList.append(X)

def NoopInst():    
    """Noop instruction implementation """
    # Hard code the dissassembling of the instruction
    global cycleIndex
    global cycleList
#    print("NOOP")
#    print(cycleIndex)
    #Copy and add the last value in the list
    cycleList.append(cycleList[-1])

def FindSpriteIndexes(cycle, spriteMidPt, lastCycle):    
    """Find sprite indexes """
    # Make it a function incase we need to handle rows
    #spriteMidPt -= 1  # Adjust for zero based indexes
    rowindex = cycle //  40
    spriteMidPt += rowindex * 40
    start = spriteMidPt-1;
    end = spriteMidPt+1;
    if(start < 0):
        start = 0
    if(end > lastCycle):
        end = lastCycle
    return start, end


def FindNumbersInString(string):    
    """Find all positive AND negative integers in a string """
    res = [int(d) for d in re.findall(r'-?\d+', string)]
    return res

print(" ")
print(" ")
print(" ")
print("*************************************************************")
print("*************************************************************")
print("The date and time is:",datetime.datetime.now())
print("*************************************************************")
print("*************************************************************")

#read in the data
with open('input.txt','r') as f:
    array = f.readlines()
f.close()


# loop through the instructions to create a cycle by cycle log
for i in range(len(array)):
    #print('Comand:',array[i])
    if(array[i].find('noop'))>=0 :
        NoopInst()    
    elif(array[i].find('addx'))>=0 :
        Adder = FindNumbersInString(array[i])
        AddInstr(Adder[0])


#print(cycleList)

sum = 0
for i in range(6):
    index = i*40 + 20
    sum += (index * cycleList[index])

#sum = cycleList[20] + cycleList[60] + cycleList[100] + cycleList[140] + cycleList[180] + cycleList[220]
print("Part1: Final Sum = ",sum)

#remove the first item in cycleList so that we are zero based.
del cycleList[0]
pixel = '.'* len(cycleList)
pixLst = list(pixel)

# Go through the cycle and see when the sprite overlaps the current cycle
# I think we have to ignore the edges. Try without that first
for i in range(0,len(cycleList)):
#for i in range(0,39):
    start, end = FindSpriteIndexes(i, cycleList[i], len(cycleList))  
    # Now determine if the current index falls in the sprite window
    match = 0
    if(i>=start)and(i<=end):
        match=1
    #for j in range(start,end):
    #    print('j: ',j)
    #    if i == j:
    #        match = 1
    #        break
    if match == 1:
        pixLst[i]='#'
    #print('Cycle: ',i,' X=',cycleList[i],'Sprite Indexes: ',start,end,' Pixel: ',pixLst[i])


#Print out the list, line by line
#print(pixLst[0:39])
print(' '.join(pixLst[0:39]))
print(' '.join(pixLst[40:79]))
print(' '.join(pixLst[80:119]))
print(' '.join(pixLst[120:159]))
print(' '.join(pixLst[160:199]))
print(' '.join(pixLst[200:399]))

