#!/usr/bin/env python
#This python code assumes that it is being run on python3 interpreter.
#It might break on python2.x

import sys

def divisible_by_3(number):
    #Proper check to make sure input is integer/float when called directly.
    if not isinstance(number, (int, float)):
        raise TypeError('need an integer')
    if (abs(number)%3 == 0):
        return str("aunty")
    else:
        return str("uncle")


if __name__ == "__main__":
    try:
        #Keeping it simple in the main func call to only make sure the input is integer
        num = int(input("Enter your whole number: "))
    except ValueError as e:
        raise ValueError('only Integers are allowed.')
    print(divisible_by_3(num))