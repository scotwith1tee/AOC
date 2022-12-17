import datetime
import re

def CalcWorryLevel(num, oper, operand):    
    """Perform the opeation on the number then div 3 and round"""
    if oper == '+':
        if operand == 'old':
            result = 2 * num
        else:
            result = num + int(operand)
    elif oper == '*':
        if operand == 'old':
            result = num * num
        else:
            result = num * int(operand)
    # get the floor of a divide by 3
    result = result // 3
    return int(result)

def CalcWorryLevelNoDiv(num, oper, operand):    
    """Perform the opeation on the number then div 3 and round"""
    if oper == '+':
        if operand == 'old':
            result = 2 * num
        else:
            result = num + int(operand)
    elif oper == '*':
        if operand == 'old':
            result = num * num
        else:
            result = num * int(operand)
    # get the floor of a divide by 3
    #result = result // 3
    return int(result)

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


monkeys =[]
# loop through the input to create the initial monkey dictionary array
for i in range(len(array)):
    # Look for the Monkey tag
    print('i: ',i)
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
total = [0] * (len(monkeys)+1)
for rnd in range(20):
    for m in range(len(monkeys)):
        for items in range(len(monkeys[m]['items'])):
            total[m] += 1
            currItem = monkeys[m]['items'][items]
            wLevel = CalcWorryLevel(currItem, monkeys[m]['operation'], monkeys[m]['operand'])
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
print(total)

total.sort()
print(total[-1]*total[-2])
print(total)
print(*monkeys, sep='\n')

print(" Part 2: start with orig, no divide by three")
monkeys = monkeyOrig
total = [0] * (len(monkeys)+1)
for rnd in range(20):
    for m in range(len(monkeys)):
        for items in range(len(monkeys[m]['items'])):
            total[m] += 1
            currItem = monkeys[m]['items'][items]
            wLevel = CalcWorryLevel(currItem, monkeys[m]['operation'], monkeys[m]['operand'])
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
    if(rnd % 1000)==0:
        print(rnd)
        print(total)

print(total)

total.sort()
print(total[-1]*total[-2])
print(total)
print(*monkeys, sep='\n')


