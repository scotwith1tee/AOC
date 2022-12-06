import datetime
# Array that gives the win/loss/draw points for input of rock/paper/scissors for both opponent and me
matchPts = [[3,6,0], [0,3,6], [6,0,3]]
# Array that picks my choice to match the outcome
# [Opp Play][Lose/Draw/Win]
inputToMatchOutcome = [['Z','X','Y'], ['X','Y','Z'], ['Y','Z','X']]


def IsStrUniqueChars(testStr):    
    """Is the string all unique characters."""
    # Loop through each character and find the occurrences in the string
    # If there's more than 1, it's not unique
    for i in range(len(testStr)):
        letter = testStr[i]
        # We will always find one
        index = testStr.find(letter)
        if testStr.find(letter,index+1) > 0:
            # We found a duplicate
            return False
    
    # No duplicates, it's unique
    return True


print("The date and time is:",datetime.datetime.now())

#read in the data
with open('input.txt','r') as f:
    array = f.readlines()
f.close()

#print(array)
print(len(array))
print(len(array[0]))
print(type(array[0]))
#Part 1
# Find the first 4 non identical letters
sum = 0;
myStr = array[0]
print('Input Length:',len(myStr))
#myStr = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'
for index in range(len(myStr)):
    # the index is the starting character
    # load four characters, starting with the index
    tmpStr = myStr[index:index+4]

    if IsStrUniqueChars(tmpStr):
        print('Part 1:Start of Packet:',index+4)
        break


#Part 2 - Find the Start of Message marker. Fourteen non identical letters
#myStr = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
for index in range(len(myStr)):
    # the index is the starting character
    # load four characters, starting with the index
    tmpStr = myStr[index:index+14]

    if IsStrUniqueChars(tmpStr):
        print('Part 2:Start of message:',index+14)
        break

#    print(tmpStr)
    # Determine points for that round
#    print(myStr[index])

    # See if we are at the end of an elfs list. add another list item

