#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10

if number < 0:
    last_digit *= -1

if (last_digit > 5):
    print("Last digit of {} is {} and is greater than {}".format(number, last_digit, 5))
elif (last_digit == 0):
    print("Last digit of {} is {} and is {}".format(number, last_digit, 0))
else:
    print("Last digit of {} is {} and is less than {} and not {}".format(number, last_digit, 6, 0))
