#I have no idea why i doing that, but the monkeys do
#First of all, we need to generate the combination btw numbers and letters, maybe like Steam Guard do(using 5 characters). But a little bit slower


import string
from random import choice
import time

# string.ascii_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# string.digits = "0123456789"

time.sleep(3)
size = 5
values = string.ascii_uppercase + string.digits
password = ''
for i in range(size):
    password += choice(values)
print(f"A senha da vez é {password}")

# for i in range(1,10+1):
#     time.sleep(1)
#     size = 5
#     values = string.ascii_uppercase + string.digits
#     attempt = ''
#     for i in range(size):
#         attempt += choice(values)
#         print(attempt)

time.sleep(3)
size = 5
values = string.ascii_uppercase + string.digits
attempt = ''
for i in range(size):
    attempt += choice(values)
print(attempt)

max_attempts = 0

while attempt != password:
    attempt = ''
    time.sleep(1)
    for elements in range(size):
        attempt += choice(values)
    print(attempt)
    max_attempts += 1
    if attempt == password or max_attempts == 9:
        print('Chega fi, cabô')
        break


##Repetition
if max_attempts == 9:
    max_attempts = 0
    time.sleep(3)
    size = 5
    values = string.ascii_uppercase + string.digits
    password = ''
    for i in range(size):
        password += choice(values)
print(f"A senha da vez é {password}")

while attempt != password:
    attempt = ''
    time.sleep(1)
    for elements in range(size):
        attempt += choice(values)
    print(attempt)
    max_attempts += 1
    if attempt == password or max_attempts == 9:
        print('Chega fi, cabô')
        break






    
#def function = define

# def combination_generator(
# size=5, 
# chars=string.ascii_uppercase + string.digits):
#  return ''.join(random.choice(chars) for _ in range(size))
# print(combination_generator()) # M4ICUV
