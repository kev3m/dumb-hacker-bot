#I have no idea why i doing that, but the monkeys do
#First of all, we need to generate the combination btw numbers and letters, maybe like Steam Guard do(using 5 characters). But a little bit slower


import string
from random import random, choice
import time

# string.ascii_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# string.digits = "0123456789"

time.sleep(3)

size = 5
values = string.ascii_uppercase + string.digits
password = ''
for i in range(size):
    password += choice(values)

print(password)
    
#def function = define

# def combination_generator(
# size=5, 
# chars=string.ascii_uppercase + string.digits):
#  return ''.join(random.choice(chars) for _ in range(size))
# print(combination_generator()) # M4ICUV
