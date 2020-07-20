#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    return sum(list((a * b) for a, b in my_list)) / sum(c[1] for c in my_list)
