# 992-218-1937
# program to find phone number in massage

import random
def findNumber(data):
    if len(data) != 12:
        return False
    for i in range(0, 3):
        if not data[i].isdecimal():
            return False
    if data[3] != '-':
        return False
    for i in range(4, 7):
        if not data[i].isdecimal():
            return False
    if data[7] != '-':
        return False
    for i in range(8, 12):
        if not data[i].isdecimal():
            return False
    return True

# print("enter massage : ")
# number = input()
message = "call me tomorrow at 987-654-1230 or day after tomorrow at 784-125-6541,good night"
# print(findNumber(number2))

for i in range(len(message)):
    chunk = message[i:i + 12]
    if findNumber(chunk):
        print('phone number found : ' + chunk)
print('done')
