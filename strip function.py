spam = '     .Hello World.     '
a =  spam.strip()
print(a)
b = spam.lstrip()
print(b)
c = spam.rstrip()
print(c)

spam = 'SpamSpamBaconSpamEggsSpamSpam'
d = spam.strip('ampS')               # doest matter the order could be Spam or mapS
print(d)                            # strip from the front and end
