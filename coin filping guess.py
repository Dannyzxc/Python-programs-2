import random
guess = ''
# while guess not in ('heads', 'tails'):
print('Guess the coin toss! Enter heads(1) or tails(0):')
guess = int(input())
toss = random.randint(0, 1)   # 0 is tails, 1 is heads
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guesss = int(input())
    if toss == guesss:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')