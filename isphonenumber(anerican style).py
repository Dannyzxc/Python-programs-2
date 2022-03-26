# 992-218-1937
# program to check if this looks like a number

import random

def checkNumber(data):
    if len(data) != 12:
        print('phone should have 12 digits only')
        return False
    for i in range(0, 3):
        if not data[i].isdecimal():
            print('enter first 3 digits properly')
            return False
    if data[3] != '-':
        print("did not find '-' after first 3 digits")
        return False
    for i in range(4, 7):
        if not data[i].isdecimal():
            print('enter middle 3 digits properly')
            return False
    if data[7] != '-':
        print("did not find '-' after middle 3 digits")
        return False
    for i in range(8, 12):
        if not data[i].isdecimal():
            print('enter last 3 digits properly')
            return False
    return 'this looks like a phone number'


print("check the number you have is a phone number: ")
number = input()
print(checkNumber(number))
