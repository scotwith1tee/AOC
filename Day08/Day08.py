import datetime

def IsVisible(row, col):    
    """Look in all four directions to see if this tree is visible """
    # Look right
    # Look left
    # Look up
    # Look down
    pass

def FindNumbersInString(string):    
    """Move the crates according to the move command """
    res = [int(i) for i in string.split() if i.isdigit()]
    return res

def ConvertStrLstIntoNumLst():
    """Not sure if I need this """
    pass



print("The date and time is:",datetime.datetime.now())

#read in the data
#with open('input.txt','r') as f:
with open('testinput.txt','r') as f:
    array = f.readlines()
f.close()

# What are the inner tree ranges
gridHeight = len(array)
gridWidth = len(array[0])
print(gridHeight, gridWidth)

startX = 1
endX = gridWidth - 3 # extra off because extra char, maybe carriage return
startY = 1
endY = gridHeight - 2
total = 0
print(array[startY][endX])
print(array[endY][endX])
print('grid start:',startX, endX, startY, endY)
# loop through all the inner trees
for x in range(startX,endX):
    for y in range(startY,endY):
        #print(array[x][y])
        total +=1


# remember to add the outer tree ring

# create a 2d list array for crate configuration
# top crate is the last item on the crate list
# Send the moves 1 at a time to modify the crate arrays
# test find all numbers in a string
