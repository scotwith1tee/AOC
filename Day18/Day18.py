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

def numTouchingEnclosed(coords):
    touches = 0
    x = coords[0]
    y = coords[1]
    z = coords[2]
    if edgeBlocks[x-1][y][z] == 1:
        print('Enclosed:',x,y,z,' is next to edge block: ',x-1,y,z)
        touches +=1
    if edgeBlocks[x+1][y][z] == 1:
        print('Enclosed:',x,y,z,' is next to edge block: ',x+1,y,z)
        touches +=1
    if edgeBlocks[x][y-1][z] == 1:
        print('Enclosed:',x,y,z,' is next to edge block: ',x,y-1,z)
        touches +=1
    if edgeBlocks[x][y+1][z] == 1:
        print('Enclosed:',x,y,z,' is next to edge block: ',x,y+1,z)
        touches +=1
    if edgeBlocks[x][y][z-1] == 1:
        print('Enclosed:',x,y,z,' is next to edge block: ',x,y,z-1)
        touches +=1
    if edgeBlocks[x][y][z+1] == 1:
        print('Enclosed:',x,y,z,' is next to edge block: ',x,y,z+1)
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

def getNumOnes(list3d):
    dims = dim(list3d)
    total=0
    for x in range(dims[0]):
        for y in range(dims[1]):
            for z in range(dims[2]):
                if list3d[x][y][z] == 1:
                    total += 1
                    #print('Edge found at:',x,y,z)
    return total
                
        




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
edgeBlocks = [[ [0 for cc1 in range(zMax+2)] for cc2 in range(yMax+2)] for r in range(xMax+2)]
enclosed = [[ [0 for cc1 in range(zMax+2)] for cc2 in range(yMax+2)] for r in range(xMax+2)]

#print(space)  
#print('Type Space:',type(space))
print('dimensions:',dim(space))
spaceDim = dim(space)


#Fill the space
for i in range(len(inputCoord)):
    x = inputCoord[i][0]
    y = inputCoord[i][1]
    z = inputCoord[i][2]
    space[x][y][z] = 1

#print(space) 
totalSides = 0 
#Loop through known points and count number of touches on each side
# I believe there's room on the edges
for i in range(len(inputCoord)):
    totalSides += (6 - numSidesTouching(inputCoord[i]))

print('Part 1, Total Exposed Sides:',totalSides)

# Part two, look for external surface area
# i don't think we care about the inside
# Simplistic attempt, find the suraces exposed when looking from all
# 6 sides. Won't find items under overhang
# create a 3d array of just edge pieces


#look from the left and right x views
for y in range(1,yMax+1):
    for z in range(1,zMax+1):
        # for each block in the square, see if you can see it from left and then the right
        for x in range(1,xMax+1):
            if space[x][y][z] == 1:
                edgeBlocks[x][y][z] = 1
                #print('edge block', x,y,z)
                break
        for x in range(xMax+1,0,-1):
            if space[x][y][z] == 1:
                edgeBlocks[x][y][z] = 1
                #print('edge block', x,y,z)
                break

#look from the top and bottom y views
for x in range(1,xMax+1):
   for z in range(1,zMax+1):
        # for each block in the square, see if you can see it from left and then the right
        for y in range(1,yMax+1):
             if space[x][y][z] == 1:
                edgeBlocks[x][y][z] = 1
                #print('edge block', x,y,z)
                break
        for y in range(yMax+1,0,-1):
             if space[x][y][z] == 1:
                edgeBlocks[x][y][z] = 1
                #print('edge block', x,y,z)
                break
#look from the front and back z views
for y in range(1,yMax+1):
    for x in range(1,xMax+1):
        # for each block in the square, see if you can see it from left and then the right
        for z in range(1,zMax+1):
            if space[x][y][z] == 1:
                edgeBlocks[x][y][z] = 1
                #print('edge block', x,y,z)
                break
        for z in range(zMax+1,0,-1):
            if space[x][y][z] == 1:
                edgeBlocks[x][y][z] = 1
                #print('edge block', x,y,z)
                break

totalSides = 0
#loop through all the known edge pieces and count up edges
for x in range(xMax+1):
    for y in range(yMax+1):
        for z in range(zMax+1):
            if edgeBlocks[x][y][z] == 1:
                CoordList = [x,y,z]
                totalSides += (6 - numSidesTouching(CoordList))

removeBecauseEnclosed = 0
numEnclosedSpaces = 0
# Find any full enclosed air space
# Just search the entire map
for x in range(1,xMax+1):
    for y in range(1,yMax+1):
        for z in range(1,zMax+1):
            if space[x][y][z] == 0:
                if isEnclosed(x,y,z)==True:
                    #print('Enclosed Cell at: ',x,y,z)
                    numEnclosedSpaces += 1
                    enclosed[x][y][z] = 1
                    #check to see if the enclosed space is next to an edge space
                    removeBecauseEnclosed += numTouchingEnclosed([x,y,z])

print('Edge Blocks Found:',getNumOnes(edgeBlocks))
print('Sides to remove because edge block touches enclosed:',removeBecauseEnclosed)
print('Enclosed gaps: ',numEnclosedSpaces)
print('Total edge piece sides:', totalSides)
# new try - find all the enclosed air cells and see if they are next to an edge cell
# if they are remove 1 side
print('Ajusted Surface Area:', totalSides - removeBecauseEnclosed) # - (42 * 6))
#print(edgeBlocks)
exit()



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
