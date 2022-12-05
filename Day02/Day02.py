import datetime
# Array that gives the win/loss/draw points for input of rock/paper/scissors for both opponent and me
matchPts = [[3,6,0], [0,3,6], [6,0,3]]
# Array that picks my choice to match the outcome
# [Opp Play][Lose/Draw/Win]
inputToMatchOutcome = [['Z','X','Y'], ['X','Y','Z'], ['Y','Z','X']]

def MatchScore(OppPlay, MyPlay):    
    """What's the score of the the match."""
    # Find the reference into the array that determines the win/lose/draw points
    OppIndex = ord(OppPlay) - ord('A')
    MyIndex = ord(MyPlay) - ord('X')

    # win/lose/draw points + the points for the play
    return (matchPts[OppIndex][MyIndex] + MyIndex + 1)

def FindPlay(OppPlay, ExpectedOutcome):    
    """What move to enter to get the expected outcome based on the opponents move."""
    # Find the reference into the array that determines what move I should make
    OppIndex = ord(OppPlay) - ord('A')
    MyIndex = ord(ExpectedOutcome) - ord('X')

    # return the XYZ move that should be made to meet the expected outcome
    # Use the opponents play and expected outcome.
    return (inputToMatchOutcome[OppIndex][MyIndex])



print("The date and time is:",datetime.datetime.now())

#read in the data
with open('input.txt','r') as f:
    array = f.readlines()
f.close()


#Part 1
# Sum of match points
sum = 0;

for index in range(len(array)):
    # Determine points for that round
    sum += MatchScore(array[index][0],array[index][2])

    # See if we are at the end of an elfs list. add another list item
 
print("Part 1: total point:",sum)


#Part 2
# Sum of match points
sum = 0;
myMove = ' '
for index in range(len(array)):
    #First determine with move to make to match the expected outcome of the game
    myMove = FindPlay(array[index][0], array[index][2])

    # Determine points for that round using the functon from Part 1
    sum += MatchScore(array[index][0],myMove)

print("Part 2: total point:",sum)

