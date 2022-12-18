import datetime
import re
# The number of vertices
nV = 4

INF = 999


# Algorithm implementation


def FindNumbersInString(string):    
    """Find all positive AND negative integers in a string """
    res = [int(d) for d in re.findall(r'-?\d+', string)]
    return res
def dim(a):
    if not type(a) == list:
        return []
    return [len(a)] + dim(a[0])
def numSidesTouching(coords):
    touches = 0
    x = coords[0]
    y = coords[1]
    z = coords[2]
    if space[x-1][y][z] == 1:
        touches +=1
    if space[x+1][y][z] == 1:
        touches +=1
    if space[x][y-1][z] == 1:
        touches +=1
    if space[x][y+1][z] == 1:
        touches +=1
    if space[x][y][z-1] == 1:
        touches +=1
    if space[x][y][z+1] == 1:
        touches +=1
    return touches
def isEnclosed(x, y, z):
    # if any of the surrounding blocks are empty, then this
    # block isn't enclosed air
    if space[x-1][y][z] == 0:
        return False
    if space[x+1][y][z] == 0:
        return False
    if space[x][y-1][z] == 0:
        return False
    if space[x][y+1][z] == 0:
        return False
    if space[x][y][z-1] == 0:
        return False
    if space[x][y][z+1] == 0:
        return False
    return True






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
#with open('testinput.txt','r') as f:
    array = f.readlines()
f.close()

# Create blank 3d array
#space = [][][] #xyz
inputCoord = []

xMax =yMax = zMax = 0
#Populate the coordinates list
for i in range(len(array)):
    inputCoord.append(FindNumbersInString(array[i]))
    if inputCoord[i][0] > xMax:
        xMax = inputCoord[i][0]
    if inputCoord[i][1] > yMax:
        yMax = inputCoord[i][1]
    if inputCoord[i][2] > zMax:
        zMax = inputCoord[i][2]

print('Size:',xMax,yMax,zMax)

#create 3d array
space = [[ [0 for cc1 in range(zMax+2)] for cc2 in range(yMax+2)] for r in range(xMax+2)]

print(space)  
print('Type Space:',type(space))
print('dimensions:',dim(space))
spaceDim = dim(space)


#Fill the space
for i in range(len(inputCoord)):
    x = inputCoord[i][0]
    y = inputCoord[i][1]
    z = inputCoord[i][2]
    print(x,y,z)
    space[x][y][z] = 1

print(space) 
totalSides = 0 
#Loop through known points and count number of touches on each side
# I believe there's room on the edges
for i in range(len(inputCoord)):
    totalSides += (6 - numSidesTouching(inputCoord[i]))

print('Part 1, Total Exposed Sides:',totalSides)

airEnclosedSides = 0
# Find any full enclosed air space
# Just search the entire map
for x in range(1,xMax+1):
    for y in range(1,yMax+1):
        for z in range(1,zMax):
            if space[x][y][z] == 0:
                if isEnclosed(x,y,z)==True:
                    print('Enclosed Cell at: ',x,y,z)
                    airEnclosedSides += 6

print('Enclosed pockets: ',airEnclosedSides /6)
print('Part 2: Adjusted Surface Area: ',totalSides - airEnclosedSides)
# I think the hint for part two is incorrect
print(space[1][2][2],space[3][2][2],space[2][1][2],space[2][3][2],space[2][2][1],space[2][2][3])

exit()
#read in the data
#with open('testinput.txt','r') as f:
with open('input.txt','r') as f:
    array = f.readlines()
f.close()


monkeys =[]
# loop through the input to create the initial monkey dictionary array
for i in range(len(array)):
    # Look for the Monkey tag
    if array[i].find('Monkey')>-1:
        # Grab the id, even though we will access it by the dictionary list number
        monkeys.append({ })
        MonkeyId = FindNumbersInString(array[i])[0]
        monkeys[MonkeyId]["ID"] = MonkeyId
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
monkeyOrig = monkeys # Save for later
print(*monkeys, sep='\n')
print(" ")
print(" Start throwning items")
total = [0] * (len(monkeys))

for rnd in range(10000):
    for m in range(len(monkeys)):
        for items in range(len(monkeys[m]['items'])):
            total[m] += 1
            currItem = monkeys[m]['items'][items]
            wLevel = CalcWorryLevelNoDiv(currItem, monkeys[m]['operation'], monkeys[m]['operand'])
            if (wLevel % int(monkeys[m]['test'])) == 0:
                target = int(monkeys[m]['true'])
            else:
                target = int(monkeys[m]['false'])
            # Move the item to the target monkey
            monkeys[target]['items'].append(wLevel)

        #empty the list at the end because they've thrown all their items
        monkeys[m]['items'].clear()
        #print(*monkeys, sep='\n')
        #print(monkeys)
    if(rnd%100)==0:
        print('Round:',rnd)
        print(total)
        print("The date and time is:",datetime.datetime.now())

print(total)

total.sort()
print(total[-1]*total[-2])
print(total)
#print(*monkeys, sep='\n')
