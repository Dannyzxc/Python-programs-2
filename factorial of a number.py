def factorial(n):
    total = 1
    for i in range(1, n + 1):
        total = i * total
        print('i is ' + str(i) + ', total is ' + str(total))
    # print('End of factorial(%s%%)' % (n))
    return total
print('enter a number to find factorial of:')
number = int(input())
print(factorial(number))
