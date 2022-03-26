#  split function

things1 = "this is a napkin"
print1 = things1.split()
print(print1)

things2 = "this-is-a-table"
print2 = things2.split('-')
print(print2)

#

spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".
Please do not drink it.
Sincerely,
Bob.'''
a = spam.split('\n')
print(spam)
print(a)

b = '-'.join('There can be only one.'.split())
print(b)