#I have no idea why i doing that, but the monkeys do
#First of all, we need to generate the combination btw numbers and letters, maybe like Steam Guard do(using 5 characters). But a little bit slower


import string
import random

#def function = define

def combination_generator(
size=5, 
chars=string.ascii_uppercase + string.digits):
 return ''.join(random.choice(chars) for _ in range(size))
print(combination_generator()) # M4ICUV
