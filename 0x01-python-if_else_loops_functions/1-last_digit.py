#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastNumber = 0

if number >= 0:
    lastNumber = number % 10
else:
    lastNumber = (-number % 10) * -1

message = f"last digit of {number} is {lastNumber}"

if lastNumber == 0:
    print(f"{message} and is 0")
elif lastNumber > 5 and lastNumber % 10 != 0:
    print(f"{message} and is greater than 5")
else:
    print(f"{message} and is less than 6 and not 0")
