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
with open('testinput.txt','r') as f:
#with open('input.txt','r') as f:
    array = f.readlines()
f.close()

#Make the first dictionary item
dictTemplate = dict(ID = 0, items = [9999], operation = "*", operand = "0", test = 51001, true = 100, false = 100)
monkeys = [dictTemplate,dictTemplate]
print("monkeys type: ", type(monkeys))
print(monkeys)
monkeys.append(dictTemplate)
print(monkeys)
dictTemplate["ID"] = 1
monkeys.append(dictTemplate)
print(monkeys)
print("monkeys type: ", type(monkeys))

# loop through the input to create the initial monkey dictionary array
for i in range(len(array)):
    # Look for the Monkey tag
    print('i: ',i)
    if array[i].find('Monkey')>-1:
        # Grab the id, even though we will access it by the dictionary list number
        print(array[i])
        MonkeyId = FindNumbersInString(array[i])[0]
        print('Monkey Id: ', MonkeyId)
        monkeys.append(dictTemplate)
        monkeys[MonkeyId]["ID"] = MonkeyId
        print('Monkey Id from Dict:',monkeys[MonkeyId]["ID"])
        # Load items from next line
        monkeys[MonkeyId]["items"] = FindNumbersInString(array[i+1])
        # Load operation and operand
        tmpStr = array[i+2]
        monkeys[MonkeyId]["operation"] = tmpStr[23]
        if tmpStr[23:].find('old') >-1:
            monkeys[MonkeyId]["operand"] = 'old'
        else:
            monkeys[MonkeyId]["operand"] = str(FindNumbersInString(tmpStr)[0])
        # Load divisible test
        monkeys[MonkeyId]["test"] = str(FindNumbersInString(array[i+3])[0])
        # Load true and false monkey recipient
        monkeys[MonkeyId]["true"] =  FindNumbersInString(array[i+4])[0]
        monkeys[MonkeyId]["false"] = FindNumbersInString(array[i+5])[0]
        print('Monkey Length',len(monkeys))
        print(monkeys)
        if len(monkeys) == 2:
            break
print(monkeys)
print(monkeys[0])

print(monkeys[1])
exit()
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

