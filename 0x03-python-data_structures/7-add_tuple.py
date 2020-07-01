#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        first = tuple_b[0]
        second = tuple_b[1]
    elif len(tuple_b) == 0:
        first = tuple_a[0]
        second = tuple_a[1]
    elif len(tuple_a) == 1:
        first = tuple_a[0] + tuple_b[0]
        second = tuple_b[1]
    elif len(tuple_b) == 1:
        first = tuple_a[0] + tuple_b[0]
        second = tuple_a[1]
    else:
        first = tuple_a[0] + tuple_b[0]
        second = tuple_a[1] + tuple_b[1]
    new_tuple = (first, second)
    return(new_tuple)
