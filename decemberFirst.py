import numpy

textFile = open("elfList.txt", "r")
data = textFile.read()

newElfList = []
calorieList = []
elfCalorie = 0

numbersToList = data.split('\n\n')

for elf in numbersToList:
    newElfList.append(elf.split('\n'))

# add calories of each elf
for elf in newElfList:
    calorieCount = 0
    for item in elf:
        calorieCount += int(item)
    calorieList.append(calorieCount)

print(calorieList[0])
   
# elf with most calories
fatElf = numpy.max(calorieList)
print(fatElf)



    

#print(newElfList)


    #totalOfElf = numpy.sum(elfs)
    #print(totalOfElf)

        
# print(numbersToList[1])
# print(numbersToList[-1])

# find index of elf with most calories
# elfWithMostCalories = numpy.argmax(numbersToList)
# print(elfWithMostCalories)

# find how many calories that elf is carrying
# print(numbersToList[elfWithMostCalories])