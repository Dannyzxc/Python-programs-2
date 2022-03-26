import pprint

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def inventary(item):
    print(stuff)
    total = 0
    for k, v in item.items():
        print(str(v) + ' ' + k)
        total = total + v
    print('total no. of items are ' + str(total))

inventary(stuff)
