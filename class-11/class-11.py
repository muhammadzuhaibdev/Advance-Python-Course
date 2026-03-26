numbers = [10,23,33,47,50,60,77,83,90]

def result(num):
    if num % 2 == 0:
        return num * 2

output = list(filter(result,numbers))
print(output)








# numbers = [10,23,33,47,50,60,77,83,90]

# def test(num):
#     if num % 2 == 0:
#         return num

# output = list(map(test, numbers))
# print(output)








# i = 0
# while i < len(userNames):
#     print("While Loop", userNames[i])
#     i += 1