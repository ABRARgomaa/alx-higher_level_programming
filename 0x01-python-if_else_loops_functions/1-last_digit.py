#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
abslute = abs(number)
l_d = abslute % 10
if (number < 0):
    l_d = -l_d
if (l_d == 0):
    print(f"Last digit of {number} is {l_d} and is 0")
if (l_d < 6 and l_d != 0):
    print(f"Last digit of {number} is {l_d} and is less than 6 and not 0")
if (l_d > 5):
    print(f"Last digit of {number} is {l_d} and is greater than 5")
