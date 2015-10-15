#!/usr/bin/env python

""" Everything.py: Generates every possible alphanumeric string. """

__author__      = "Nathaniel Schmitz"
__copyright__   = "Copyright 2015, Nathaniel Schmitz"


import random # to shuffle string

# all alphanumeric characters
allowable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.?! '
base = len(allowable)

# shuffle allowable characters to randomize output order
chars = ''.join(random.sample(allowable, base))

def baseKEncode(number, k):
    if not isinstance(number, (int, long)):
        raise TypeError('Number must be an integer...')
    if number < 0:
        raise ValueError('Number must be positive...')
    kNumber = ''
    while number:
        number, i = divmod(number, k)   
        kNumber = chars[i] + kNumber
    return kNumber or chars[0]

def baseKDecode(number, k):
    return int(number, k)

# generate base^numberChars combinations
if __name__ == '__main__':
    numberChars = 3
    for i in range(0, base**3):
        print baseKEncode(i, base),
