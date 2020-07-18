#!/usr/bin/python3
def search_replace(my_list, search, replace):
        return [(num if num is not search else replace) for num in my_list]
