#!/usr/bin/python3
"""looks up available attributes and methods of an object"""
def lookup(obj):
    """lookup func"""
    list = dir(obj)
    return list
