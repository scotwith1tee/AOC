import datetime
# Array that gives the win/loss/draw points for input of rock/paper/scissors for both opponent and me
matchPts = [[3,6,0], [0,3,6], [6,0,3]]
# Array that picks my choice to match the outcome
# [Opp Play][Lose/Draw/Win]
inputToMatchOutcome = [[3,6,0], [0,3,6], [6,0,3]]

def MatchScore(OppPlay, MyPlay):    
    """What's the score of the the match."""
    # can I define this once outside of the function
    OppIndex = 0
    MyIndex = 0
    #convert the inputs to numbers
    if OppPlay =='A':
        OppIndex = 0
    elif OppPlay == 'B':
        OppIndex = 1
    elif OppPlay == 'C':
        OppIndex = 2
    else:
        OppIndex = 0
        print(OppPlay)
        print("Bad index")

    if MyPlay =='X':
        MyIndex = 0
    elif MyPlay == 'Y':
        MyIndex = 1
    elif MyPlay == 'Z':
        MyIndex = 2
    else:
        MyIndex = 0
        print(MyPlay)
        print("Bad index")

#    print(matchPts)
#    print(type(OppIndex),type(MyIndex))
    print (OppIndex, MyIndex,matchPts[OppIndex][MyIndex])
#    print (matchPts[0][1])
    return (matchPts[OppIndex][MyIndex] + MyIndex + 1)



print("The date and time is:",datetime.datetime.now())

#read in the data
with open('input.txt','r') as f:
    array = f.readlines()
f.close()

print(MatchScore('A','Y'))




# Sum of match points
sum = 0;

for index in range(len(array)):
    # Determine points for that round
    sum += MatchScore(array[index][0],array[index][2])

    # See if we are at the end of an elfs list. add another list item
 
print("total point:",sum)


