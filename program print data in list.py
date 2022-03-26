import random
names = [ ]
print(' how many names you want to enter')
t = int(input())

for i in range(0, t):
    print('enter the names')
    n = input()
    if n == ' ':
        break
    else:
        names = names + [n]

print(names)



