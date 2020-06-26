#!/usr/bin/python3
def uppercase(str):
    for asc in str:
        if ord(asc) in range(96, 123):
            asc = chr(ord(asc) - 32)
        print("{}".format(asc), end="")
    print("\n", end="")
