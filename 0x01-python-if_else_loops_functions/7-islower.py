#!/usr/bin/python3
def islower(c):
    "this checks for lower case character"
    asc = ord(c)
    if asc in range(97, 123):
        return True
    else:
        return False
