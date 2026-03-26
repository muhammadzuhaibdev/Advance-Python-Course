# i = 10
# while i > 1:
#     print(i)
#     i -= 1

inputList = [10, 23, 30, 27,15, 8, 7 ] 
outputList = []

i = 0
while i < len(inputList):
    if inputList[i] % 2 == 0:
        result = inputList[i] * 2
        outputList.append(result)
    else:
        result = inputList[i]
        outputList.append(result)
    i += 1

print(outputList)