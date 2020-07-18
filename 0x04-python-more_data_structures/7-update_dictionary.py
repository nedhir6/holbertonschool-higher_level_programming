#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for i in a_dictionary:
        if i == key:
            a_dictionary[key] = value
            flag = 1
    if flag is not 1:    
        a_dictionary[key] = value
