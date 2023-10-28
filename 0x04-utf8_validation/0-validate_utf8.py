#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Data: This is a list of integers
    Return: True if data is a valid UTF-8
    encoding, else return False
    """
    count = 0

    for j in data:
        if count == 0:
            if j >> 5 == 0b110 or j >> 5 == 0b1110:
                count = 1
            elif j >> 4 == 0b1110:
                count = 2
            elif j >> 3 == 0b11110:
                count = 3
            elif j >> 7 == 0b1:
                return False
        else:
            if j >> 6 != 0b10:
                return False
            count -= 1
    return count == 0
