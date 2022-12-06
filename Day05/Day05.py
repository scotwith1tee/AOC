import datetime

def MoveCrates(currMove):    
    """Move the crates according to the move command """
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
with open('testinput.txt','r') as f:
    array = f.readlines()
f.close()

# find crate configuration
# find move list
# create a 2d list array for crate configuration
# top crate is the last item on the crate list
# Send the moves 1 at a time to modify the crate arrays
# test find all numbers in a string
test_string = ' 1   2   3   4   5   6   7   8   9'
res = [int(i) for i in test_string.split() if i.isdigit()]
print(res) 
test_string = 'move 14 from 1 to 2'
res = [int(i) for i in test_string.split() if i.isdigit()]
print(res) 
print(type(res))
print(len(res))
print(res[0])
print(type(res[0]))
print(res[1])
print(res[2])

print(array)
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

