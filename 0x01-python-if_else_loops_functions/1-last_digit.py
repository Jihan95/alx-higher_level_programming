#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f'Last digit of {number:d} is', end=" ")

if (number < 0):
    number = -1 * (abs(number) % 10)
else:
    number %= 10

if (number > 5):
    print(f'{number:d} and is greater than 5')
elif (number == 0):
    print(f'{number:d} and is 0')
elif ((number < 6) and (number != 0)):
    print(f'{number:d} and is less than 6 and not 0')
