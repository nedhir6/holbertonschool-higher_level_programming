#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    scores = list(a_dictionary.values())
    best_score = 0
    for i in scores:
        if i > best_score:
            best_score = i
    for name in a_dictionary:
        if a_dictionary[name] == best_score:
            return name
