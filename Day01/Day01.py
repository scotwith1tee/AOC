import datetime
from turtle import end_fill
print("The date and time is:",datetime.datetime.now())
print(datetime.datetime.now())

with open('input.txt','r') as f:
    array = f.readlines()


#f.close()

#print(lines)



#with open('input.txt','r') as f:
#    w, h = [int(x) for x in next(f).split()] # read first line
#    array = []
#    for line in f: # read rest of lines
#        array.append([float(x) for x in line.split()])

# Sum per elf
sum = 0;
print(type(sum))
elflist = []

temp = '100'
print (type(array))
sum = 0
emptyCnt = 0
numCnt = 0

for index in range(len(array)):
    # See if we are at the end of an elfs list. add another list item
    if array[index] != "\n":
        numCnt+=1
        sum = sum + int(array[index])
    else:
        emptyCnt +=1
        elflist.append(sum)
        sum = 0

print(emptyCnt,numCnt)
#print(elflist)
print(max(elflist))
#print(type(elflist))
#print(type(elflist[0]))
#print(array)


#part 2
elflist.sort()
topThree = elflist[-1] + elflist[-2] +elflist[-3]
print(topThree)
