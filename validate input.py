while True:
    print('enter your age(no spacees) : ')
    age = input()
    if age.isdecimal():
        break
    print('age can only have numbers.')

while True:
    print('enter password (letters and numbers only)')
    password = input()
    if password.isalnum():
        break
    print('password can only have numbers and letters')
