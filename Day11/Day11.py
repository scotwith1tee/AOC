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
# dictTemplate = dict(ID = 0, items = [9999], operation = "*", operand = "0", test = 51001, true = 100, false = 100)
# dictTemplate1 = dict(ID = 1, items = [9999], operation = "*", operand = "0", test = 51001, true = 100, false = 100)
# monkeys = [dictTemplate,dictTemplate1]
# print("monkeys type: ", type(monkeys))
# print(monkeys)
# print("<<<<<<<")
# monkeys.append(dictTemplate)
# print(monkeys)
# print("<<<<<<<")
# monkeys[0]['ID'] = 2
# monkeys +=dictTemplate
# print(monkeys)
# print("monkeys type: ", type(monkeys))
# print("<<<<<<<")
# monkeys.append(dictTemplate)
# print(monkeys)
# print("monkeys type: ", type(monkeys))
# print("<<<<<<<")
# print("<<<<<<<")
# print("<<<<<<<")
monkeys =[]
# loop through the input to create the initial monkey dictionary array
for i in range(len(array)):
    # Look for the Monkey tag
    print('i: ',i)
    if array[i].find('Monkey')>-1:
        # Grab the id, even though we will access it by the dictionary list number
        monkeys.append({ })
        print(array[i])
        MonkeyId = FindNumbersInString(array[i])[0]
        print('Monkey Id: ', MonkeyId)
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
        # print('Monkey Length',len(monkeys))
        # print(monkeys)
        # if len(monkeys) == 2:
        #     break

print(monkeys)


