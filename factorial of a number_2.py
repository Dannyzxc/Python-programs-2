def fact(n):
    try:
        t = 1
        for i in range(1, n+1):
            t = i * t
        print('factorial of ' + str(n) + ' is ' + str(t))
    except Exception as e:
        print(e)
    return t
print('number is ')
f = int(input())
fact(f)
