# 9922181937
# program to check if this looks like a number

import random

def checkNumber(data):
    if len(data) != 10:
        print('phone should have 10 digits only')
        return False
    for i in range(0, 9):
        if not data[i].isdecimal():
            print('shouls have all numbers')
            return False
    if data[0] != '9':
        print("Number starts with 9 ")
        return False

    return data + ' - This looks like a phone number'


print("check the number you have is a phone number: ")
number = input()
print(checkNumber(number))
# 9922181937