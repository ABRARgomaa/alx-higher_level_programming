#!/usr/bin/python3
def print_last_digit(number):
    n = abs(number)
    m = n % 10
    print("{}" .format(m), end="")
    return (m)
